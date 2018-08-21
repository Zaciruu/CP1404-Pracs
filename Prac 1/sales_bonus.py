"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
sales = float(input("Enter sales: $"))
if sales < 1000:
    print("Your Bonus is 10% ", str(sales * .1).format(sales))
else:
    print("Your Bonus is 15% $", str(sales * .15).format(sales))



