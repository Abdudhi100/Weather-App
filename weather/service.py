import requests

API_KEY = "15cb9238a3b14ca7b3f232433242611"
BASE_URL = "https://api.weatherapi.com/v1/current.json"  # Corrected base URL

def fetch_weather(city):
    params = {
        'q': city,       # City name
        'key': API_KEY,  # Correct API key parameter
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=5)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        return response.json()       # Correctly call the .json() method
    except requests.exceptions.RequestException as e:
        return {'error': f"Error fetching weather data: {str(e)}"}
