// ===============================
// Show / Hide Password
// ===============================

const password = document.getElementById("loginPassword");
const eye = document.getElementById("loginEye");

eye.addEventListener("click", function () {

    if (password.type === "password") {

        password.type = "text";
        eye.classList.remove("fa-eye");
        eye.classList.add("fa-eye-slash");

    } else {

        password.type = "password";
        eye.classList.remove("fa-eye-slash");
        eye.classList.add("fa-eye");

    }

});


// ===============================
// Login Validation
// ===============================

document.querySelector("form").addEventListener("submit", function (e) {

    const email = document.querySelector("input[name='email']").value.trim();
    const passwordValue = password.value.trim();

    if (email === "" || passwordValue === "") {

        e.preventDefault();
        alert("Please fill all fields.");

    }

});