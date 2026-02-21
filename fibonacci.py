"""
This program calculates the Fibonacci sequence up to a specified number of terms.
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones. Here, it is starting with 0 and 1. The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, and so on.

Date: 21 Feb 2026
Written By: Vishesh Karn
"""

# Function to calculate and print the Fibonacci sequence
def fibonacci(num):
    # Variable to store the first two terms of the Fibonacci sequence
    a, b = 0, 1
    
    # Printing the first term
    if num >= 1:
        print(a, end=" ")

    # Printing the second term
    if num >= 2:
        print(b, end=" ")

    # Generating and printing the remaining terms
    for i in range(2, num):
        c = a + b
        print(c, end=" ")
        a, b = b, c
    print()


# Main function
def main():
    # Taking input from the user
    num = int(input("Enter the number of terms for Fibonacci sequence: "))

    # Printing the Fibonacci sequence
    fibonacci(num)


# Program execution starts here
if __name__ == "__main__":
    main()


# Thanks for using this program! It calculates the Fibonacci sequence based on the number of terms you specify. You can run this code in a Python environment to see how it works.