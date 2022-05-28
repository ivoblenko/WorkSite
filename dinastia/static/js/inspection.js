$(document).ready(function ($) {

    $("#id_patient").select2({
        language: "ru",
        width: '200px'
    })

    $("#id_patient").change(function () {
        let patient_id = this.value;
        $.ajax({
            url: "/patient/get_patient_files",
            data: {
                patient_id: patient_id
            },
            success: function (data) {
                let html = "";
                for (let key in data['files']) {
                    html += '<li file_id="' + data.files[key].id + '">' +
                        '<a href="' + data.files[key].url + '" target="_blank">' + data.files[key].name + '</a>' +
                        '<i class="fa fa-close fa-lg" style="color: red;cursor: pointer"></i>' +
                        '</li>'
                }
                $('#patient_files').html(html);
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
            },
            error: function (data) {
                $('#patient_files').html('<span>Файлы отсутствуют</span>');
            }
        })
    })

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