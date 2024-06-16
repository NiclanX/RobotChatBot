const toggles = document.querySelectorAll('.material-symbols-outlined');

toggles.forEach(element => {
    element.addEventListener('click', btnClicked);
});

function btnClicked() {
    alert("Btns Clicked");
}