/*Disable f12 build*/
window.onkeydown = window.onkeyup = window.onkeypress = function (event) {
    if (event.keyCode === 123) {
        event.preventDefault(); // Block default event behavior
        window.event.returnValue = false;
    }
}

// Add a custom event for the right button, you can disable
window.oncontextmenu = function() {
    event.preventDefault(); // Block default event behavior
    return false;
}


window.onselectstart=function(){
    return false;
};


window.oncopy=function(){
    console.log("copied");
}

window.addEventListener("resize", function() {
    console.log(window.innerHeight);
    console.log(window.innerWidth);
});

$(document).bind('keydown', function(e) {
    if(e.ctrlKey && (e.which == 83)) {
      return false;
    }
  });

  $(document).bind('keydown', function(e) {
    if(e.ctrlKey && (e.which == 85)) {
      return false;
    }
  });