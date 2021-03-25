//AJAX setup
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue =   decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

export function ajaxRequest(title, msg, lat, lng) {
    $.ajax({
        type: 'POST',
        url: "addMarker/",
        datatype: 'JSON',
        data: {'title': title, 'msg': msg, 'latitude': lat, 'longitude': lng,'csrfmiddlewaretoken': $('input[name="csrfmiddlewaretoken"]').val()},
        success: function(result){
        console.log('PONG')
        },
        error : function (xmlHttpRequest, textStatus, errorThrown) {
            console.log(errorThrown);
        }
    });
}