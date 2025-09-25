# temp_conversion_tool.py

# ✅ Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using global factor."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using global factor."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

if __name__ == "__main__":
    try:
        # ✅ User interaction
        temp_input = input("Enter the temperature to convert: ")
        if not temp_input.replace('.', '', 1).isdigit() and not (temp_input.startswith('-') and temp_input[1:].replace('.', '', 1).isdigit()):
            raise ValueError("Invalid temperature. Please enter a numeric value.")

        temperature = float(temp_input)
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature}°F is {result}°C")
        elif unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {result}°F")
        else:
            raise ValueError("Invalid unit. Please enter C or F.")

    except ValueError as e:
        print(e)
