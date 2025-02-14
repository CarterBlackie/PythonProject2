# Import the functions from my_functions.py
import my_functions

# Main function to handle user interaction
def main():
    option = 0  # Initialize option to control the loop
    while option != 6:  # Continue looping until the user selects exit
        my_functions.display_menu()  # Display menu options
        option = int(input("Enter your option: "))  # Get user input

        # Option 1: Get the day of the week
        if option == 1:
            number = int(input("Enter a number (1-7): "))
            print("Day: ", my_functions.day_of_week(number))

        # Option 2: Get the air quality category
        elif option == 2: 
            aqi = int(input("Enter Air Quality Index (AQI): "))
            print("Pollution Level:", my_functions.air_quality(aqi))

        # Option 3: Compute the largest product from three numbers
        elif option == 3: 
            value1 = float(input("Enter first number: "))
            value2 = float(input("Enter second number: "))
            value3 = float(input("Enter third number: "))
            print("Largest Product:", my_functions.largest_product(value1, value2, value3))

        # Option 4: Mix two RGB colors
        elif option == 4: 
            color1 = input("Enter first RGB color (red, green, blue): ")
            color2 = input("Enter second RGB color (red, green, blue): ")
            print("Mixed Color:", my_functions.colour_mixer(color1, color2))

        # Option 5: Play the "Yee Ha" game based on number divisibility
        elif option == 5: 
            number = int(input("Enter a number: "))
            print("Result:", my_functions.yee_ha(number))

        # Option 6: Exit the program
        elif option == 6: 
            print("Exiting the program!")
            break  # Exit the loop

        # Handle invalid input
        else: 
            print("Invalid option. Please try again.")

# Run the main function
main()
