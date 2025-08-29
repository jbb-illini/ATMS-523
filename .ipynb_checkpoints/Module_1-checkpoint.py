def calculate_rectangle_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle

    Returns:
    float: The area of the rectangle (length * width)
    """
    return length * width


def main():
    """
    Main function to handle user input, calculation, and output display.
    
    Takes length and width inputs from the user, calculates the rectangle's
    area using the calculate_rectangle_area function, and displays the
    inputs and result.
    """
    # Get user inputs
    print("Rectangle Area Calculator")
    print("-----------------------")
    
    try:
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        
        # Validate inputs
        if length <= 0 or width <= 0:
            print("Error: Length and width must be positive numbers.")
            return
            
        # Calculate area using the function
        area = calculate_rectangle_area(length, width)
        
        # Display inputs and output
        print("\nResults:")
        print(f"Length: {length}")
        print(f"Width: {width}")
        print(f"Area: {area}")
        
    except ValueError:
        print("Error: Please enter valid numbers for length and width.")


if __name__ == "__main__":
    main()