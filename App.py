from flask import Flask, render_template, request, jsonify
import requests
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

app = Flask(__name__)

# Your OpenWeatherMap API Key
API_KEY = "599c43067d70a6efa0a8609e10215968"


def fetch_weather_data(api_key, city):
    """Fetches weather data for a specific city."""
    url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }
    try:
        response = requests.get(url, params=params)
        logging.info(f"API Request URL: {response.url}")
        response.raise_for_status()

        data = response.json()
        logging.info(f"Weather data for {city}: {data}")
        return data
    except requests.exceptions.HTTPError as http_err:
        logging.error(f"HTTP error occurred: {http_err}, Response: {response.text}")
        return None
    except Exception as err:
        logging.error(f"An error occurred: {err}")
        return None


@app.route('/')
def home():
    """Render the main page."""
    return render_template('index.html')


@app.route('/weather', methods=['GET'])
def get_weather():
    """Fetch and return weather data for a given city."""
    city = request.args.get('city')
    if not city:
        return jsonify({"success": False, "message": "City name is required!"}), 400

    weather_data = fetch_weather_data(API_KEY, city)
    if weather_data:
        report = {
            "city": weather_data.get("name"),
            "temperature": weather_data["main"]["temp"],
            "feels_like": weather_data["main"]["feels_like"],
            "humidity": weather_data["main"]["humidity"],
            "weather": weather_data["weather"][0]["description"].capitalize(),
            "wind_speed": weather_data["wind"]["speed"]
        }
        return jsonify({"success": True, "report": report})
    else:
        return jsonify({"success": False, "message": "Failed to retrieve weather data."}), 404


if __name__ == '__main__':
    app.run(debug=True)
