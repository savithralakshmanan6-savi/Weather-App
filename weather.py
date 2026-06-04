import requests

city = input("Enter city name: ")

api_key = "YOUR_API_KEY"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(url)

data = response.json()

if response.status_code == 200:
    temp = data["main"]["temp"]
    weather = data["weather"][0]["description"]

    print("City:", city)
    print("Temperature:", temp, "°C")
    print("Condition:", weather)
else:
    print("City not found!")
