def main():
    
    driver()
    
def driver():
    
    battery_level = int(input("What is the battery level of the car:  "))

    if 10 < battery_level <= 20:
        print("Battery low")
    elif battery_level < 5:
        print("Engine off")
        return

    battery()


def battery():

    seatbelt_fastened = False

    while not seatbelt_fastened:
        response = input("Is your seatbelt fastened? (yes/no): ").strip().lower()
        if response == "yes":
            seatbelt_fastened = True
            print("\033[94mSeatbelt fastened, car is starting.\033[0m")
        else:
            print("Car will start when you fasten your seatbelt.")

    belt()


def belt():

    print("\033[5;93mChecking belt-...\033[0m")

    warnimg_light()

    car_motion = True

    while car_motion:
        drivers_response = input("did you remove your seatbelt? (yes/no): ").strip().lower()
        if drivers_response == "yes":
            print("\033[91mWARNING⚠️⚠️ PLEASE PUT YOUR SEATBELT ON\033[0m")
        else:
            car_motion = False
            print("\033[92mSAFE DRIVE\033[0m")


def warnimg_light():
    return


main()
