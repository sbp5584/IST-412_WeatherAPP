import pytest
from main import generate_weather_report

def test_generate_weather_report_valid_data():
    data = {
        "current": {
            "temp": 20.5,
            "feels_like": 19.0,
            "humidity": 60,
            "wind_speed": 5.5,
            "weather": [{"description": "clear sky"}]
        }
    }
    report = generate_weather_report(data)
    assert "Weather Report:" in report
    assert "Temperature: 20.5°C" in report
    assert "Feels Like: 19.0°C" in report
    assert "Humidity: 60%" in report
    assert "Wind Speed: 5.5 m/s" in report

def test_generate_weather_report_no_data():
    report = generate_weather_report(None)
    assert report == "No data available to generate report."
