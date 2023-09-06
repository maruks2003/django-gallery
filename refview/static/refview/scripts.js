// Toggles visibility of all the children of the element whose
// id is provided as the argument
function show_menu(id){
    var els = document.getElementById(id).children;
    for (var i = 0; i < els.length; i++){
        els[i].classList.toggle("hidden");
    }
}
