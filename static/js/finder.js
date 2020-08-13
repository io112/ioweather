document.getElementById('wf-form-weather-Form').addEventListener("submit", onSearch)


function onSearch(event) {
    $.ajax({
        type: "POST",
        url: '/api/search',
        data: {
            'country': document.getElementById('country').value,
            'region': document.getElementById('region').value,
            'city': document.getElementById('city').value
        },
        success: function (e) {
            document.getElementById('result-div').innerHTML = e;
        },
        error: function (e) {
            console.log('ajax error');
            window.alert("Город не найден или сервис прогноза погоды недоступен")
        }
    })
      event.preventDefault();
}
