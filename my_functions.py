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
        return 'Error'

def air_quality(air_quality_index):
    if air_quality_index < 0: 
        return 'Error'
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
        return 'Hazardous'

def largest_product(value1, value2, value3):
    if value1 < value2 and value1 < value3:
        return value2 * value3
    elif value2 < value3:
        return value1 * value3
    else:
        return value1 * value2
    
    
def colour_mixer(rgb_colour1, rgb_colour2):
    rgb_colour1 = rgb_colour1.lower()
    rgb_colour2 = rgb_colour2.lower()
    
    if rgb_colour1 == rgb_colour2:
        return rgb_colour1
    elif (rgb_colour1, rgb_colour2) in [('red', 'blue'), ('blue', 'red')]:
        return 'fuchsia'
    elif (rgb_colour1, rgb_colour2) in [('red', 'green'), ('green', 'red')]:
        return 'yellow'
    elif (rgb_colour1, rgb_colour2) in [('green', 'blue'), ('blue', 'green')]:
        return 'aqua'
    else:
        return 'Error'

def yee_ha(number):
    if number % 3 == 0 and number % 7 == 0: 
        return 'Yee Ha'
    elif number % 7 == 0: 
        return 'Ha'
    elif number % 3 == 0: 
        return 'Yee'
    else: 
        return 'Nada'