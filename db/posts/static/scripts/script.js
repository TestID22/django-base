

var first = document.getElementById("first");
var comments = document.getElementsByClassName("comments");
var tasknumber = 1;

function addTask(){
        var data = $("input").val();
        $(".comments").append('<p><b>'+ tasknumber + " - " + data + '</b></p>')
        tasknumber++;
}

function removeTask(){
    console("TODO");
}

removeTask();