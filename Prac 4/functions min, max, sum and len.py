

def main():
    numbers = []
    for i in range(5):
        number = int(input("Enter a Number:"))
        numbers.append(number)
    print("Number:", numbers[0], "\nNumber:", numbers[1], "\nNumber:", numbers[2], "\nNumber:", numbers[3], "\nNumber:",
          numbers[4])
    print("The first number is", numbers[0])
    print("The last number is", numbers[-1])
    print("The smallest number is", min(numbers))
    print("The largest number is", max(numbers))
    print("The average of the numbers is", sum(numbers) / len(numbers))


main()
