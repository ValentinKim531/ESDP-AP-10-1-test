var fd = new FormData();
fd.append("refresh", localStorage.getItem('refreshToken'));

$.ajax({
    url: '/api/token/refresh/',
    type: "POST",
    data: fd,
    processData: false,
    contentType: false,
    success: function(data, status) {
        console.log(data);
        if (data.access) {
            localStorage.setItem('accessToken', data.access);
        }
    }
});
