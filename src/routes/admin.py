import os
from datetime import datetime

from flask import Blueprint, redirect, render_template, url_for, flash, request, current_app
from werkzeug.utils import secure_filename

from src.wtforms.create_service_form import ServiceForm
from src.database.service import delete_service_by_id, get_all_service, create_service, get_service_by_id, \
    update_service

admin = Blueprint('admin_routes', __name__, template_folder='templates/admin', url_prefix='/admin')


@admin.route('/media')
def media():
    media_files = os.listdir('static/uploads')
    media_files2 = []
    for item in media_files:
        media_files2.append("uploads/" + item)
    return render_template('admin/media.html', media_files=media_files2, plus_icon="images/plus.png")


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'jpg', 'jpeg', 'png', 'gif', 'svg', 'webp'}


@admin.route('/delete_service/<int:id>')
def delete_service(service_id):
    delete_service_by_id(current_app.config.get('DATABASE'), service_id)
    return redirect(url_for('admin_routes.get_all_services'))


@admin.route('/')
def get_all_services():
    all_services = get_all_service(current_app.config.get('DATABASE'))
    return render_template('admin/admin.html', all_services=all_services)


def save_file_to_server(form, default_image, default_icon):
    image_file = form.image.data
    icon_file = form.icon.data
    image_url = default_image
    icon_url = default_icon

    if image_file and allowed_file(image_file.filename):
        image_filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{secure_filename(image_file.filename)}"
        image_path = os.path.join('static/uploads', image_filename)
        image_file.save(image_path)
        image_url = f"uploads/{image_filename}"  # Сохраняем относительный путь
    else:
        flash('Недопустимый формат изображения', 'error')

    if icon_file and allowed_file(icon_file.filename):
        icon_filename = f"{datetime.now().strftime('%Y%m%d%H%M%S')}_{secure_filename(icon_file.filename)}"
        icon_path = os.path.join('static/uploads', icon_filename)
        icon_file.save(icon_path)
        icon_url = f"uploads/{icon_filename}"  # Сохраняем относительный путь
    else:
        flash('Недопустимый формат иконки', 'error')
    return image_url, icon_url


@admin.route('/edit_service/<int:service_id>', methods=['GET', 'POST'])
def edit_service(service_id):
    service = get_service_by_id(current_app.config.get('DATABASE'), service_id)
    form = ServiceForm(
        title=service[1],
        service_type=service[2],
        description=service[3],
        price=service[4],
        development_time=service[5],
        route=service[6],
        image=service[7],
        icon=service[8],
        published=service[9],
    )
    if form.validate_on_submit():
        image_url, icon_url = save_file_to_server(form, service[7], service[8])
        if image_url == "" or icon_url == "":
            return redirect(request.url)
        update_service(
            current_app.config.get('DATABASE'),
            form.title.data,
            form.service_type.data,
            form.description.data,
            form.price.data,
            form.development_time.data,
            form.route.data,
            image_url,
            icon_url,
            form.published.data,
            service_id
        )

        flash('Услуга успешно добавлена!', 'error')
        return redirect(url_for('admin_routes.get_all_services'))
    return render_template('admin/add_service.html', form=form, big_preview=service[7],
                           icon_preview=service[8])


@admin.route('/add_service/', methods=['GET', 'POST'])
def add_service():
    form = ServiceForm()
    if form.validate_on_submit():
        image_url, icon_url = save_file_to_server(form, "", "")
        if image_url == "" or icon_url == "":
            return redirect(request.url)
        create_service(
            current_app.config.get('DATABASE'),
            form.title.data,
            form.service_type.data,
            form.description.data,
            form.price.data,
            form.development_time.data,
            form.route.data,
            image_url,
            icon_url,
            form.published.data
        )

        flash('Услуга успешно добавлена!', 'error')
        return redirect(url_for('admin_routes.get_all_services'))

    return render_template('admin/add_service.html', form=form, preview_src="", icon_preview="")
