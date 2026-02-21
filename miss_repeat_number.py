"""
Finding the missing and repeating number in an array of size n containing numbers from 1 to N.

Assumptions:
    • Numbers are in range 1 to N
    • Exactly one number missing
    • Exactly one number repeated

Date: 21 Feb 2026
Author: Vishesh
"""

# Function to find the missing and repeating number
def single_repeat_and_single_miss_finder(arr):
    # Getting the size of the array
    n = len(arr)

    # Initializing a frequency array to count occurrences of each number
    frequency = [0] * (n + 1)

    # Counting the frequency of each number in the input array
    for num in arr:
        frequency[num] += 1
    
    # Initializing variables to store the missing and repeating numbers
    missing = None
    repeating = None

    # Iterating through the frequency array to find the missing and repeating numbers
    for i in range(1, n + 1):
        if frequency[i] == 0: missing = i
        elif frequency[i] == 2: repeating = i
    
    return (missing, repeating)


# Program execution starts here
if __name__ == "__main__":
    a_list = [6, 4, 3, 5, 5, 1]
    print(f"(M, R) = {single_repeat_and_single_miss_finder(a_list)}")

