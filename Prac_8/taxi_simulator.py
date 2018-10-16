from Prac_8.car import Car
from Prac_8.taxi import Taxi
from Prac_8.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
             SilverServiceTaxi("Hummer", 200, 4)]

    print("Let's Drive")
    print(MENU)
    user_input = input(">>>").lower()
    while True:
        try:
            selection = (input(">>>"))
            if selection.upper() == 'Q':
                quit()
                break
            elif selection.upper() == 'C':
                choose_taxi()
                break
            elif selection.upper() == 'D':
                drive()
                break
            else:
                print("Invalid menu choice")
                print(MENU)
        except ValueError:
            print("Invalid menu choice")


main()
