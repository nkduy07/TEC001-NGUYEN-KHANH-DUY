import requests


def get_weather():
    api_key = "d6e8806d141f590ea1453c0e04b95515"
    url_ = "https://api.openweathermap.org/data/2.5/weather"

    city_name = input("Enter the name of the municipality: ")

    params = {
        "q": city_name,
        "appid": api_key,
    }

    try:
        response = requests.get(url_, params=params)
        response.raise_for_status()
        data = response.json()

        full_city_name = data['name']
        description = data['weather'][0]['description']
        temp = data['main']['temp']
        tempC = temp - 273.15

        print(f"City: {full_city_name}")
        print(f"Weather: {description}")
        print(f"Temperature: {tempC}°C")

    except requests.exceptions.HTTPError:
        print("Error: City not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    get_weather()