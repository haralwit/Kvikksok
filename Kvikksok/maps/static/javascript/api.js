function test() {
    $.ajax({
        type: 'GET',
        url: "google.com", 
        success: function(result){
        console.log(result)
        },
        error : function (xmlHttpRequest, textStatus, errorThrown) {
            console.log("not ok " + errorThrown);
        }
    });
}