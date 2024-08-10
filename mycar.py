def main():
    battery_level = int(input("What is the battery level of the car:  "))


    if 10 < battery_level <= 20:
         print("battery low")
    elif battery_level < 5:
         print("engine off")
         return  

    battery()

def battery():

    belt()

    seatbelt_fastened = False

    while not seatbelt_fastened:
        response = input("Is your seatbelt fastened? (yes/no): ").strip().lower()
        if response == "yes":
            seatbelt_fastened = True
            print("\033[94mSeatbelt fastened, car is starting.\033[0m")
        else:
           print("Car will start when you fasten your seatbelt.")


def belt():
    
    print("\033[5;93mChecking belt-.........\033[0m")


    
main()
