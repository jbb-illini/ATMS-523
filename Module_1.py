def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle

    Returns:
    float: The area of the rectangle (length * width)
    """
    # Returns the product of length and width to find the area.
    return length * width


def main():
    """
    Main function to handle user input, calculation, and output display.
    
    Takes length and width inputs from the user, calculates the rectangle's
    area using the calculate_rectangle_area function, and displays the
    inputs and result.
    """
    # Prints a header for the program.
    print("Rectangle Area Calculator")
    print("-----------------------")
    
    try:
        # Prompts the user to enter the length and width and converts them to floats.
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        
        # Validates if the length and width are positive numbers.
        if length <= 0 or width <= 0:
            print("Error: Length and width must be positive numbers.")
            return
            
        # Calls the calculate_rectangle_area function to compute the area.
        area = calculate_rectangle_area(length, width)
        
        # Prints the final results, including the length, width, and calculated area.
        print("\nResults:")
        print(f"Length: {length}")
        print(f"Width: {width}")
        print(f"Area: {area}")
        
    except ValueError:
        # Handles the case where the user input is not a valid number.
        print("Error: Please enter valid numbers for length and width.")


# Checks if the script is being run directly and not imported.
if __name__ == "__main__":
    # Calls the main function to start the program execution.
    main()