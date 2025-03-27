from flask import Blueprint, render_template, current_app

from src.database.service import get_all_service, get_service_by_type, get_service_by_route, get_limit_random_service

page = Blueprint('page_routes', __name__, template_folder='templates', url_prefix='/')


@page.context_processor
def utility_processor():
    def web_services():
        links = get_service_by_type(current_app.config.get('DATABASE'), 0)
        return links

    def design_services():
        links = get_service_by_type(current_app.config.get('DATABASE'), 1)
        return links

    def promotion_services():
        links = get_service_by_type(current_app.config.get('DATABASE'), 2)
        return links

    def development_services():
        links = get_service_by_type(current_app.config.get('DATABASE'), 3)
        return links

    def services_items():
        links = get_service_by_type(current_app.config.get('DATABASE'), 4)
        return links

    return dict(
        web_services=web_services,
        design_services=design_services,
        promotion_services=promotion_services,
        development_services=development_services,
        services_items=services_items,
    )


@page.route('/')
def home():
    return render_template('pages/main.html')


@page.route('/services/<string:route>')
def services(route):
    service = get_service_by_route(current_app.config.get('DATABASE'), route)
    service_recommendation = get_limit_random_service(current_app.config.get('DATABASE'), 4)
    return render_template('pages/service.html', service=service, service_recommendation=service_recommendation)


@page.route('/portfolio')
def portfolio():
    return render_template('pages/portfolio.html')


@page.route('/express-solutions')
def express_solutions():
    return render_template('pages/express_solution.html')


@page.route('/about-us')
def about():
    return render_template('pages/about_us.html')


@page.route('/contacts')
def contacts():
    return render_template('pages/contacts.html')
