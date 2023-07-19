function logout() {
    fetch('/auth/logout/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        credentials: 'include',
    })
    .then(() => {
        window.location.href = "/auth/login";
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}