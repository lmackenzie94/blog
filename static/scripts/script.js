const password = document.getElementById('password');
const confirmPassword = document.getElementById('confirmPassword');
const match = document.querySelector('.passwordMatch');
const checkbox = document.getElementById('togglePassword');

const togglePassword = () => {
    password.type === "password" ? password.type = "text" : password.type = "password";
    confirmPassword.type === "password" ? confirmPassword.type = "text" : confirmPassword.type = "password";
}

const passwordMatch = () => {
    password.value === confirmPassword.value ? (match.innerHTML = '<i class="fas fa-check-circle"></i>') : (match.innerHTML = '<i class="fas fa-times-circle"></i>');
}

password.addEventListener('change', passwordMatch);
confirmPassword.addEventListener('change', passwordMatch);
checkbox.addEventListener('click', togglePassword);