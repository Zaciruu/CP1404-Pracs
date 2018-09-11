from Prac_6.guitar import Guitar


def main():
    guitars = []

    print("My Guitars")
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        add_guitar = Guitar(name, year, cost)
        guitars.append(add_guitar)
        print("{} added".format(add_guitar))
        name = input("Name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))

    print("These are my guitars:")

    if guitars is not None:
        for i, guitar in enumerate(guitars):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = "(vintage)"
            print("Guitar {}: {} ({}), worth ${}{}".format(i + 1, guitar.name, guitar.year,
                                                           guitar.cost,
                                                           vintage_string))
    else:
        print("No guitars :( Quick, go and buy one!")


main()
