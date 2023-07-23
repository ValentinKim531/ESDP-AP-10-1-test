document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();

    var email = document.getElementById('email').value;
    var password = document.getElementById('password').value;

    fetch('/auth/login/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({
            email: email,
            password: password,
        }),
        credentials: 'include',
    })
    .then(response => response.json())
    .then(data => {
        console.log('Login response: ', data);
        if (data.access && data.refresh) {
            console.log('Received Data: ', data);
            document.getElementById('message').style.display = 'block';
            document.getElementById('message').innerText = 'Login successful!';
            window.location.href = "/newsline/";
        } else {
            document.getElementById('message').style.display = 'block';
            document.getElementById('message').innerText = 'Login failed.';
            console.error(data);
        }
    })
    .catch((error) => {
        console.error('Error:', error);
        document.getElementById('message').style.display = 'block';
        document.getElementById('message').innerText = 'An error occurred.';
    });
});
