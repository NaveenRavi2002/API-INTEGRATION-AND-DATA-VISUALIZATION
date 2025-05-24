import requests

# Your OpenWeatherMap API key (replace with your actual key)
api_key = "YOUR_API_KEY"

# City to get weather for
city = "Makhnahi"

# Base URL for OpenWeatherMap API
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Build the complete URL with the city and API key
complete_url = base_url + "appid=" + api_key + "&q=" + city

# Send the request to the API
response = requests.get(complete_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the JSON data from the response
    data = response.json()

    # Extract relevant weather data
    weather_description = data['weather'][0]['description']
    temperature = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']

    # Print the weather information
    print(f"Weather in {city}:")
    print(f"  Description: {weather_description}")
    print(f"  Temperature: {temperature:.2f}°C")
    print(f"  Humidity: {humidity}%")
    print(f"  Pressure: {pressure} hPa")

else:
    print(f"Error: Could not retrieve weather data for {city}.  Status code: {response.status_code}")