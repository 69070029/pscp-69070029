"""rain"""
cloud = input()
wind = input()

if cloud == "Gloomy" and wind == "High" or wind == "Medium":
    print("100%")
elif cloud == "Cloudy":
    print("50%")
elif cloud == "Clear" and wind == "Low":
    print("0%")
else:
    print("Not sure.")
