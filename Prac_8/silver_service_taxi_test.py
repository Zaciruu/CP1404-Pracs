from Prac_8.silver_service_taxi import Silver_Service_Taxi


def main():
    new_taxi = Silver_Service_Taxi("Test Silver Taxi", 100, 1)
    new_taxi.drive(18)
    print(new_taxi)
    print(new_taxi.get_fare())


main()
