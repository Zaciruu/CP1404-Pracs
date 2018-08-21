# A shop requires a small program that would allow them to quickly work out total price for a number of items, each with different prices.
#
# The program allows the user to enter the number of items and the price of each different item.
# Then the program computes and displays the total price of those items.
# If the total price is over $100, then a 10% discount is applied to that total before the amount is displayed on the screen.
#
# The output should look something like (bold text represents user input):
#
# Number of items: 3
# Price of item: 100
# Price of item: 21.56
# Price of item: 4
# Total price for 3 items is $113.10
number_of_items = 3
print("Please enter amount for item")
item_1 = float(input("Amount of Item 1:"))
item_2 = float(input("Amount of Item 2:"))
item_3 = float(input("Amount of Item 3:"))
total = item_1 + item_2 + item_3
if total > 100:
    print(total)
else:
    print(str(total - .10))