city = input("Enter a city name: ")
temperature = float(input("Enter the temperature: "))

if temperature >= 75:
    status = "warm"
else:
    status = "cool"

print(f"The weather in {city} is {status}.")
