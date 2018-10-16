from Prac_8.unreliable_car import UnreliableCar


def main():
    """Test some UnreliableCars."""
    # Different Cars
    good_car = UnreliableCar("Not Bad Boss", 100, 89)
    bad_car = UnreliableCar("You Ain't Getting Anywhere", 100, 9)
    for i in range(1, 12):
        print("Attempting to drive {}km:".format(i))
        print("{:12} drove {:2}km".format(good_car.name, good_car.drive(i)))
        print("{:12} drove {:2}km".format(bad_car.name, bad_car.drive(i)))
    # print the final states of the cars
    print(good_car)
    print(bad_car)


main()
