# Example
from main import add_numbers, convert_to_fahrenheit


def test_addition():
    assert add_numbers(2, 3) == 5
    assert add_numbers(-1, 1) == 0
    assert add_numbers(0, 0) == 0


def test_conversion():
    assert convert_to_fahrenheit(0) == 32.0  # Freezing point of water
    assert convert_to_fahrenheit(100) == 212.0  # Boiling point of water
    assert convert_to_fahrenheit(-40) == -40.0  # -40°C is -40°F
    assert convert_to_fahrenheit(37) == 98.6  # Average human body temperature

 
from unittest.mock import Mock, patch
from main import fetch_weather

@patch("main.requests.get")
def test_normal_case(mock_get):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "current": {
            "temp_k": 300.15,
            "condition": {
                "text": "Sunny",
            }
        }
    }

    mock_get.return_value = mock_response
    result = fetch_weather("New York")
    assert result["temp_c"] == 27
    assert result["description"] == "Sunny"