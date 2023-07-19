var fd = new FormData();
fd.append("email", "admin@gmail.com");
fd.append("password", "root");
$.ajax({
    url: '/api/token/',
    type: "POST",
    data: fd,
    processData: false,
    contentType: false,
    success: function(data, status) {
        console.log(data);
    }
});