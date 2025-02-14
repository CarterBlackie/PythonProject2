import my_functions

def display_menu():
    print("\nMenu:")
    print("1 - Day of the Week")
    print("2 - Air Quality Index")
    print("3 - Largest Product")
    print("4 - Colour Mixer")
    print("5 - Yee Ha")
    print("6 - Exit Program")


def main():
    option = 0  # Initialize the option
    while option != 6:
        display_menu()  # Display menu each time
        option = int(input("Enter your option: "))  # Prompt for input inside the loop

        if option == 1:
            number = int(input("Enter a number (1-7): "))
            print("Day: ", my_functions.day_of_week(number))
        elif option == 2: 
            aqi = int(input("Enter Air Quality Index (AQI): "))
            print("Pollution Level:", my_functions.air_quality(aqi))
        elif option == 3: 
            value1 = float(input("Enter first number: "))
            value2 = float(input("Enter second number: "))
            value3 = float(input("Enter third number: "))
            print("Largest Product:", my_functions.largest_product(value1, value2, value3))
        elif option == 4: 
            #colour_mixer()
            print("Added option 4")
        elif option == 5: 
            #yee_ha()
            print("Added option 5")
        elif option == 6: 
            print("Exiting the program!")
            break  # Properly exit the loop
        else: 
            print("Invalid option. Please try again.")


main()