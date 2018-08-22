numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[0] = 10
print(numbers)

numbers = [3, 1, 4, 1, 5, 9, 2]
numbers[-1] = 1
print(numbers)

numbers = [3, 1, 4, 1, 5, 9, 2]
print(str(numbers[-1]), str(numbers[-2]))

numbers = [3, 1, 4, 1, 5, 9, 2]
if numbers.index(9):
    print("true")
else:
    print("false")