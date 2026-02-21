"""
This program simply gives the factorial of a number.
Date: 11 Feb 2026
Written By: Vishesh Karn
"""

# Function to calculate the factorial recursively
def factorial_recursive(num : int) -> int:
    if num <= 1:
        return 1
    return num * factorial_recursive(num - 1)

# Function to calculate the factorial iteratively
def factorial_iterative(num : int) -> int:
    factorial = 1
    if num <= 1:
        return 1
    for i in range(2, num + 1):
        factorial = factorial * i
    return factorial

# Main function to run the program
def main():
    status = '1'
    print("Program to Show the Factorial of a number.")

    while(status == '1'):
        # Taking input from the user
        num = int(input("\nEnter a positive integer: "))

        # Showing output to the user
        print(f"Ans: {num}! = {factorial_recursive(num)}")
        print(f"Ans: {num}! = {factorial_iterative(num)}")

        # Asking from the user to Re-Run the program
        print("Would you like to calculate another factorial?")
        status = input("Enter 1 for 'Yes', anything else for 'No': ")

# Program execution starts here
if __name__ == "__main__":
    main()


# Thanks for your time.