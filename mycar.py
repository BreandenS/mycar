import time


def main():
    authorized_drivers = ["Breanden", "Kudzi", "Bryan"]

    driver_name = input("Please enter your name to start the car: ")

    if driver_name not in authorized_drivers:
        print("Car won't start. Unauthorized driver.")
        return
    else:
        print(f"\033[94mWelcome, {driver_name}!\033[0m")

    driver()
    battery()
    belt()


def driver():
    battery_level = int(input("What is the battery level of the car:  "))

    if battery_level < 5:
        print("Car off. Please charge to start your drive.")
        return
    elif 10 < battery_level <= 20:
        print("Battery low,Please charge so that your journey wont be interrupted")

    return


def battery():
    seatbelt_fastened = False

    while not seatbelt_fastened:
        response = input("Is your seatbelt fastened? (yes/no): ").strip().lower()
        if response == "yes":
            seatbelt_fastened = True
            print("\033[94mSeatbelt fastened, car is starting.\033[0m")
        else:
            print("Car will start when you fasten your seatbelt.")

    return


def belt():
    print("\033[5;93mChecking belt-...\033[0m")

    manage_car_motion()


def manage_car_motion():
    car_motion = True

    time.sleep(2)

    while car_motion:
        drivers_response = (
            input("Did you remove your seatbelt? (yes/no): ").strip().lower()
        )

        if drivers_response == "yes":
            print("\033[91mWARNING⚠️⚠️ PLEASE PUT YOUR SEATBELT ON\033[0m")

            seatbelt_status = (
                input("Have you put your seatbelt back on? (yes/no): ").strip().lower()
            )
            if seatbelt_status == "yes":
                car_motion = False
                print("\033[92mSAFE DRIVE\033[0m")
            else:
                print("\033[91mWARNING⚠️⚠️ PLEASE PUT YOUR SEATBELT ON\033[0m")
        elif drivers_response == "no":
            car_motion = False
            print("\033[92mSAFE DRIVE\033[0m")
        else:
            print("\033[91mINVALID RESPONSE. PLEASE ANSWER 'yes' OR 'no'\033[0m")


if __name__ == "__main__":
    main()
