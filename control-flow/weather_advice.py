# Script to ask users about the current weather conditions and provide clothing recommendations based on the input

# Prompt user for weather input
weather = input("What's the weather like today? (sunny/rainy/cold): ").lower()

# Provide clothing recommendations
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
