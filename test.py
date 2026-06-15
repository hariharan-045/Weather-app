import requests

API_KEY="weatherblaster007"
url = f"https://api.openweathermap.org/data/2.5/weather?q=Chennai&appid={API_KEY}&units=metric"

response = requests.get(url)

print(response.status_code)

print(response.json())

