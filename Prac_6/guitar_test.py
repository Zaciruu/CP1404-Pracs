from Prac_6.guitar import Guitar

guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
other_guitar = Guitar("Another Guitar", 2012, 1500)

print("{} get_age() - Expected 96. Got {}".format(guitar.name,
                                                  guitar.get_age()))

print("{} get_age() - Expected 6. Got {}".format(other_guitar.name,
                                                 other_guitar.get_age()))

print()
print("{} is_vintage() - Expected True. Got {}".format(guitar.name,
                                                       guitar.is_vintage()))
print("{} is_vintage() - Expected False. Got {}".format(other_guitar.name,
                                                        other_guitar.is_vintage()))
