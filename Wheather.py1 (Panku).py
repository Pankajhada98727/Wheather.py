import requests
def get_weather(city_name):
    """Gets the weather for the specified city."""
    api_key = "YOUR_API_KEY"
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name, api_key)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"]
        return temperature
    else:
        return None

def main():
    """Main function."""
    city_name = input("Enter the city name: ")
    temperature = get_weather(city_name)
    if temperature is not None:
        temperature = temperature - 273.15
        print("The temperature in {} is {} degree celcius.".format(city_name, temperature))
    else:
        print("Invalid city name or error in fetching data.")

if __name__ == "__main__":
    main()