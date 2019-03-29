const input = document.getElementById('password');
const checkbox = document.getElementById('togglePassword');

const togglePassword = () => {
    input.type === "password" ? input.type = "text" : input.type = "password";
}

checkbox.addEventListener('click', togglePassword);