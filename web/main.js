function getWeather() {
    var city = document.getElementById('user_input').value
    eel.get_weather(city)(setText)
    
}

function setText(weather) {
    var text = `${weather}`
    document.getElementById('temp').innerText = text
}