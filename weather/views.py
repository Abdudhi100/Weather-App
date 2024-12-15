import requests
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .service import fetch_weather  # Ensure this service file exists

# API view for fetching weather data
@api_view(['GET'])
def get_weather(request):
    city = request.GET.get('city', 'London')  # Fetch city from query params
    try:
        data = fetch_weather(city)  # Pass city dynamically
        return Response(data)  # Return JSON response
    except Exception as e:
        return Response({'error': str(e)}, status=500)

# HTML rendering view
def weather_view(request):
    city = request.GET.get('city', 'London')  # Default city is London
    api_key = '3648eef8d07bbc76a3bc70ef807be3cf'
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    weather_data = {}
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        data = response.json()
        weather_data = {
            'city': data['name'],  # Correct key for city name
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],  # Fixed typo
            'icon': data['weather'][0]['icon']
        }
    except requests.exceptions.RequestException as e:
        weather_data['error'] = f"Error fetching weather data: {str(e)}"

    return render(request, 'weather/weather.html', {'weather': weather_data})
def Home(request):
    return render(request, 'home.html')