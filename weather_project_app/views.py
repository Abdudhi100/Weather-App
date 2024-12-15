import requests
from django.shortcuts import render

# Helper function to fetch weather data
def fetch_weather(city, api_key):
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {'error': str(e)}

# Main weather view
def weather_view(request):
    city = request.GET.get('city', 'London')  # Default city is London
    api_key = '3648eef8d07bbc76a3bc70ef807be3cf'
    
    weather_data = {}
    try:
        data = fetch_weather(city, api_key)
        if 'error' in data:
            weather_data['error'] = data['error']
        else:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'icon': data['weather'][0]['icon']
            }
    except Exception as e:
        weather_data['error'] = "Error fetching weather data."

    return render(request, 'weather/weather.html', {'weather': weather_data})
