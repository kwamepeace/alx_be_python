FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
value = float(input("Enter the temperature to convert: "))
temp = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()

def convert_to_celsius():
    result = (value - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{value} is {result}")


def convert_to_fahrenheit():
    result = (value * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{value} is {result}")



if temp == "F":
    convert_to_celsius()
elif temp == "C":
    convert_to_fahrenheit()
else:
    print("Invalid temperature. Please enter a numeric value.")

