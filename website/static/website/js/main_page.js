function AboutMe() {
    $.ajax({
        url: "about_me",
        type: 'GET',
        success: function(ret) {
            $("#context-box").html(ret);
        }
    })
    $("#context-box").css("background", "#FFFFF0");
    $("#flanker").css("background-image", "url('../static/images/blog/oziel-gomez.jpg')");
    $("#masker").css("background", "rgba(0, 0, 0, 0.25)");
}

function Article() {
    $.ajax({
        url: "article",
        type: 'GET',
        success: function(ret) {
            $("#context-box").html(ret);
        }
    })
    $('#context-box').css("background-image", "url('../static/images/blog/alchemy.gif')");
    $("#flanker").css("background-image", "url('../static/images/blog/Preview.png')");
    $("#masker").css("background", "rgba(0, 0, 0, 0.1)");
}

function Sources() {
    $.ajax({
        url: "sources",
        type: 'GET',
        success: function(ret) {
            $("#context-box").html(ret);
        }
    })
    $("#context-box").css("background-image", "url('../static/images/blog/13.png')");
    $("#flanker").css("background-image", "none");
    $("#masker").css("background", "rgba(0, 0, 0, 0.5)");
}

$(document).ready(function(){
    $("#flanker").css("background-image", "url('../static/images/blog/Preview.png')");
})
