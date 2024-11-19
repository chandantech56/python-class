# Simple Python Calculator

# Function to add two numbers
def add(x, y):
    return x + y

# Function to subtract two numbers
def subtract(x, y):
    return x - y

# Function to multiply two numbers
def multiply(x, y):
    return x * y

# Function to divide two numbers
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

# Displaying the menu
def display_menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Main program
def main():
    while True:
        display_menu()

        # Taking user input for operation
        choice = input("Enter choice (1/2/3/4/5): ")

        # Check if the user chose to exit
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        
        # Ensure the input is valid
        if choice in ('1', '2', '3', '4'):
            # Taking user input for the numbers
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            # Perform the chosen operation
            if choice == '1':
                print(f"The result is: {add(num1, num2)}\n")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}\n")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}\n")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}\n")
        else:
            print("Invalid input! Please select a valid operation.\n")

if __name__ == "__main__":
    main()
