"""
CP1404/CP5632 - Practical - Suggested Solution
Fill in the TODOs to complete the task
"""

finished = False
result = 0
while not finished:
    try:
        result = int(input("Please Enter an integer: "))
        finished = True
    except ValueError:
        print("Please enter an integer.")
print("Valid result is:", result)