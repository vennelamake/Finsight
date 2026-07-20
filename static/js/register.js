// =============================
// Show / Hide Password
// =============================

const password = document.getElementById("password");
const confirmPassword = document.getElementById("confirmPassword");

const togglePassword = document.getElementById("togglePassword");
const toggleConfirm = document.getElementById("toggleConfirm");

togglePassword.addEventListener("click", () => {

    if(password.type === "password"){

        password.type = "text";
        togglePassword.classList.remove("fa-eye");
        togglePassword.classList.add("fa-eye-slash");

    }

    else{

        password.type = "password";
        togglePassword.classList.remove("fa-eye-slash");
        togglePassword.classList.add("fa-eye");

    }

});

toggleConfirm.addEventListener("click", () => {

    if(confirmPassword.type === "password"){

        confirmPassword.type = "text";
        toggleConfirm.classList.remove("fa-eye");
        toggleConfirm.classList.add("fa-eye-slash");

    }

    else{

        confirmPassword.type = "password";
        toggleConfirm.classList.remove("fa-eye-slash");
        toggleConfirm.classList.add("fa-eye");

    }

});

// =============================
// Password Validation
// =============================

password.addEventListener("keyup", function(){

    let value = password.value;

    let upper = /[A-Z]/;
    let lower = /[a-z]/;
    let number = /[0-9]/;
    let special = /[!@#$%^&*(),.?":{}|<>]/;

    document.getElementById("length").style.color =
    value.length >= 8 ? "green" : "red";

    document.getElementById("length").innerHTML =
    value.length >= 8 ? "✔ Minimum 8 Characters"
                      : "❌ Minimum 8 Characters";

    document.getElementById("upper").style.color =
    upper.test(value) ? "green" : "red";

    document.getElementById("upper").innerHTML =
    upper.test(value) ? "✔ One Uppercase"
                      : "❌ One Uppercase";

    document.getElementById("lower").style.color =
    lower.test(value) ? "green" : "red";

    document.getElementById("lower").innerHTML =
    lower.test(value) ? "✔ One Lowercase"
                      : "❌ One Lowercase";

    document.getElementById("number").style.color =
    number.test(value) ? "green" : "red";

    document.getElementById("number").innerHTML =
    number.test(value) ? "✔ One Number"
                       : "❌ One Number";

    document.getElementById("special").style.color =
    special.test(value) ? "green" : "red";

    document.getElementById("special").innerHTML =
    special.test(value) ? "✔ One Special Character"
                        : "❌ One Special Character";

});

// =============================
// Form Validation
// =============================

document.getElementById("registerForm").addEventListener("submit",function(e){

    

    let valid = true;

    // Name

    const fullname = document.getElementById("fullname").value.trim();

    if(!/^[A-Za-z ]+$/.test(fullname)){

        document.getElementById("nameError").innerHTML =
        "Only alphabets are allowed.";

        valid = false;

    }

    else{

        document.getElementById("nameError").innerHTML = "";

    }

    // Email

    const email = document.getElementById("email").value.trim();

    if(!/^[^ ]+@[^ ]+\.[a-z]{2,3}$/.test(email)){

        document.getElementById("emailError").innerHTML =
        "Enter a valid email.";

        valid = false;

    }

    else{

        document.getElementById("emailError").innerHTML = "";

    }

    // Mobile

    const mobile = document.getElementById("mobile").value.trim();

    if(!/^[6-9][0-9]{9}$/.test(mobile)){

        document.getElementById("mobileError").innerHTML =
        "Enter a valid 10-digit mobile number.";

        valid = false;

    }

    else{

        document.getElementById("mobileError").innerHTML = "";

    }

    // Confirm Password

    if(password.value !== confirmPassword.value){

        document.getElementById("confirmError").innerHTML =
        "Passwords do not match.";

        valid = false;

    }

    else{

        document.getElementById("confirmError").innerHTML = "";

    }

    // Password Strength

    const strongPassword =
        /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&]).{8,}$/;

    if(!strongPassword.test(password.value)){

        alert("Password does not meet all requirements.");

        valid = false;

    }

    // Success

    if(valid){

        document.getElementById("registerForm").submit();

    }

});