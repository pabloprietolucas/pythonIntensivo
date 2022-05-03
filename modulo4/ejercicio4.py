import requests
ciudad = input("Escriba un nombre válido de ciudad: ")
response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={ciudad}&APPID=e3422ebcdaeb38d3e97acef43ad3a75f&units=metric")
datos = response.json()["main"]
temp_max = datos["temp_max"]
temp_min = datos["temp_min"]
print(f"La temperatura máxima en {ciudad} será de {temp_max}ºC y la mínima de {temp_min}ºC")