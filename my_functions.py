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