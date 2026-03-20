#Checklist
#Show year-by-year growth
#Show both interest earned and amount
#Allowing different compounding frequency

#v1.1 - Error handling issues addressed (Mar 20, 2026 - 01:44)
#v1.2 -

import webbrowser
import time


def main():
    print("Compound Interest Calculator")
    print(" 1. Calulate compound interest")
    print(" 2. How compound interest works")
    print(" 3. How to use this app")
    print(" 4. Check for updates")
    print(" 5. Quit")

    try:
        user_choice = int(input("\nYour choice: "))

        if user_choice in range(1, 6):
            if user_choice == 1:
                calc_interest()
            elif user_choice == 4:
                check_for_updates()
                time.sleep(0.8)
                main()
            elif user_choice == 5:
                quit()
            else:
                print("UNDER MAINTENANCE! Try again after next update\n\n")
                time.sleep(0.8)
                main()
        else:
            print("Option must be within menu!\n\n")
            time.sleep(0.8)
            main()
    except ValueError:
        print("Invalid input. Kindly try again!\n\n")
        time.sleep(0.8)
        main()



#Mar 14, 2026 - 03:39
def calc_interest():
    try:
        principal = float(input("\nEnter principal amount: "))
        time_period = int(input("Enter time(in years): "))
        rate = float(input("Enter rate(%): "))
    except ValueError:
        print("Invalid input! Kindly try again\n")
        calc_interest()

    time.sleep(0.8)
    print("\nSelect compounding frequency:")
    print("1. Annually")
    print("2. Semi-annually")
    print("3. Quartely")
    print("4. Monthly") 
    print("5. Daily")

    n = 1

    try:
        cf = int(input("\nYour choice: "))
        if cf in range(1, 6):
            if cf == 2:
                n = 2
            elif cf == 3:
                n = 4
            elif cf == 4:
                n = 12
            elif cf == 5:
                n = 365
        else:
            print("Choice not in menu\n")
            calc_interest()
    except ValueError:
        print("Invalid input! Kindly try again\n")
        calc_interest()

    print("")
    t = 1

    while t <= time_period:
        amount = principal * (1 + (rate/100)/n) ** (n*t)
        period_interest = amount - principal

        print(f"Year {t}: Interest earned = GHc{period_interest:.2f}, Total amount = GHc{amount:.2f}")
        time.sleep(1)
        t += 1

    end = input("\nPress ENTER to continue or type quit to end the program\n\n")
    if end.lower() == "quit":
        quit()
    time.sleep(0.8)
    main()


#check for updates
def check_for_updates():
    print("Checking for updates...\n\n")
    webbrowser.open("https://github.com/self-reliantkid/Compound-Interest-Calculator/releases/latest")


#quit program
def quit():
    print("Program quit successful!")
    time.sleep(0.5)
    return



if __name__ == "__main__":
    main()