$.ajax({
    url: '/api/newsline/',
    type: "GET",
    headers: {
        "Accept": "application/json",
        "Authorization": "JWT " + localStorage.getItem('accessToken'),
    },
    success: function(data, status) {
        console.log(data);
    }
});
