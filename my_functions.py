# Function to return the day of the week based on the given number (1-7)
def day_of_week(day_number):
    if day_number == 1: 
        return 'Sunday'
    elif day_number == 2: 
        return 'Monday'
    elif day_number == 3: 
        return 'Tuesday'
    elif day_number == 4: 
        return 'Wednesday'
    elif day_number == 5: 
        return 'Thursday'
    elif day_number == 6: 
        return 'Friday'
    elif day_number == 7: 
        return 'Saturday'
    else:
        return 'Error'  # Return error if the input is out of range

# Function to determine air quality based on the Air Quality Index (AQI)
def air_quality(air_quality_index):
    if air_quality_index < 0: 
        return 'Error'  # Negative values are invalid
    elif air_quality_index <= 50:
        return 'Good'
    elif air_quality_index <= 100:
        return 'Moderate'
    elif air_quality_index <= 150:
        return 'Unhealthy for Sensitive Groups'
    elif air_quality_index <= 200:
        return 'Unhealthy'
    elif air_quality_index <= 300:
        return 'Very Unhealthy'
    else: 
        return 'Hazardous'  # AQI above 300 is hazardous

# Function to find the largest product of two numbers from three given values
def largest_product(value1, value2, value3):
    if value1 < value2 and value1 < value3:
        return value2 * value3  # Smallest number is value1, multiply the other two
    elif value2 < value3:
        return value1 * value3  # Smallest number is value2, multiply value1 and value3
    else:
        return value1 * value2  # Smallest number is value3, multiply value1 and value2

# Function to mix two primary RGB colors and return the resulting color
def colour_mixer(rgb_colour1, rgb_colour2):
    rgb_colour1 = rgb_colour1.lower()  # Convert input to lowercase for consistency
    rgb_colour2 = rgb_colour2.lower()

    # If both colors are the same, return that color
    if rgb_colour1 == rgb_colour2:
        return rgb_colour1
    # Mixing primary colors
    elif (rgb_colour1, rgb_colour2) in [('red', 'blue'), ('blue', 'red')]:
        return 'fuchsia'  # Red + Blue = Fuchsia
    elif (rgb_colour1, rgb_colour2) in [('red', 'green'), ('green', 'red')]:
        return 'yellow'   # Red + Green = Yellow
    elif (rgb_colour1, rgb_colour2) in [('green', 'blue'), ('blue', 'green')]:
        return 'aqua'     # Green + Blue = Aqua
    else:
        return 'Error'  # Invalid color combination

# Function that returns a phrase based on divisibility by 3 and/or 7
def yee_ha(number):
    if number % 3 == 0 and number % 7 == 0: 
        return 'Yee Ha'  # Divisible by both 3 and 7
    elif number % 7 == 0: 
        return 'Ha'  # Divisible only by 7
    elif number % 3 == 0: 
        return 'Yee'  # Divisible only by 3
    else: 
        return 'Nada'  # Not divisible by either 3 or 7

# Function to display the menu options
def display_menu():
    print("\nMenu:")
    print("1 - Day of the Week")
    print("2 - Air Quality Index")
    print("3 - Largest Product")
    print("4 - Colour Mixer")
    print("5 - Yee Ha")
    print("6 - Exit Program")
