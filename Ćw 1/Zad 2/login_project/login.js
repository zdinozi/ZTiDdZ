const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    //Wyciągnięcie wartości username i password z form'a
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    // walidacja username i password z form'a
    if (username === "" && password === "") {
        alert("You have successfully logged in.");
        location.reload();
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})