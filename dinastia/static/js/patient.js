$(document).ready(function ($) {

    $(".datepicker").datepicker({
        language: "ru-RU",
        format: 'yyyy-mm-dd',
        days: ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота'],
        daysShort: ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'],
        daysMin: ['Вс', 'Пн', 'Вт', 'Ср', 'Чт', 'Пт', 'Сб'],
        months: ['Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь', 'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь'],
        monthsShort: ['Янв', 'Фев', 'Мар', 'Апр', 'Май', 'Июн', 'Июл', 'Авг', 'Сен', 'Окт', 'Ноя', 'Дек'],
        weekStart: 1,
        startView: 0,
        yearFirst: false,
        yearSuffix: ''
    });

    $('.fa-close').click(function () {
        let parent = this.parentNode;
        let file_id = parent.getAttribute('file_id');

        $.confirm({
            title: 'Предупреждение!',
            draggable: true,
            content: 'Файл будет удален безвозвратно! Вы уверены, что хотите его удалить?',
            buttons: {
                confirm: {
                    text: 'Да',
                    action: function () {
                        $.ajax({
                            url: "/patient/delete_patient_files",
                            data: {
                                file_id: file_id
                            },
                            success: function (data) {
                                parent.remove();
                            }
                        })
                    }
                },
                cancel: {
                    text: 'Нет',
                    action: function () {
                    }
                },

            }
        });


    })

})