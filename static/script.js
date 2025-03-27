document.addEventListener('DOMContentLoaded', function() {
    const burger = document.getElementById('burger');
    const menu = document.getElementById('mobile-menu');

    burger.addEventListener('click', function() {
        burger.classList.toggle('active');
        menu.classList.toggle('active');
    });

    // Открытие/закрытие dropdown-меню
    const dropdownToggle = document.querySelector('.dropdown-toggle');
    const dropdownMenu = document.querySelector('.dropdown-menu');
    const dropdown = document.querySelector('.dropdown');

    dropdownToggle.addEventListener('click', function(e) {
        e.preventDefault(); // Отменяем переход по ссылке
        dropdown.classList.toggle('active');
    });

    // Закрытие dropdown при клике вне его области
    document.addEventListener('click', function(e) {
        if (!dropdown.contains(e.target)) {
            dropdown.classList.remove('active');
        }
    });


//    const fileInput = document.getElementById('serviceImageForm');
//    fileInput.addEventListener('change', (e) => {
//        // обрабатываем e.target.files[0]
//        fileInput.value = ''; // Сброс поля
//    });

});