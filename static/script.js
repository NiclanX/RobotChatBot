const toggles = document.querySelectorAll('.material-symbols-outlined');
const body = document.querySelector('body');
const chatContainer = document.querySelector('.chat-container');
const personalizeInput = document.querySelector('input');


toggles.forEach(element => {
    element.addEventListener('click', btnClicked);
});

function btnClicked() {
    body.classList.toggle('night-mode');
    chatContainer.classList.toggle('night-mode');
    personalizeInput.classList.toggle('night-mode');
    // alert("Btns Clicked");

    if (body.classList.contains('night-mode')) {
        toggles.forEach(element => {
            element.innerHTML =`light_mode`;
    
    });
    } else {
        toggles.forEach(toggle => {
            toggle.innerHTML = `mode_night`;
        });
    }

}