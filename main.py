import requests


def fetch_weather_data(api_key, lat=39.9526, lon=-75.1652, exclude="hourly,minutely", units="metric", lang="en"):
    """Fetches detailed weather data using OpenWeatherMap One Call 3.0 API."""
    url = "https://api.openweathermap.org/data/3.0/onecall"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "exclude": exclude,
        "units": units,
        "lang": lang
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 401:
        print("Error 401: Unauthorized. Please check your API key and ensure it has access to One Call 3.0.")
        return None
    else:
        print("Failed to retrieve data:", response.status_code)
        return None


def generate_weather_report(data):
    """Generates a readable weather report from the One Call API data."""
    if data:
        current = data["current"]
        temperature = current["temp"]
        feels_like = current["feels_like"]
        humidity = current["humidity"]
        wind_speed = current["wind_speed"]
        weather = current["weather"][0]["description"]

        report = (
            f"Weather Report:\n"
            f"Weather: {weather.capitalize()}\n"
            f"Temperature: {temperature}°C\n"
            f"Feels Like: {feels_like}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s\n"
        )
        return report
    else:
        return "No data available to generate report."


# Main Program
api_key = "599c43067d70a6efa0a8609e10215968"  # Replace with your actual API key

# Fetch weather data
weather_data = fetch_weather_data(api_key)
weather_report = generate_weather_report(weather_data)
print(weather_report)