#Checklist
#Show year-by-year growth
#Show both interest earned and amount
#Allowing different compounding frequency

#v1.1 - Error handling issues addressed (Mar 20, 2026 - 01:44)
#v1.2 -

import webbrowser
import time
import sys



#main menu
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
            # elif user_choice == 2:
            #     print(how_it_works)
            #     time.sleep(3)
            #     input("Press ENTER to continue\n\n")
            #     main
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



#explanation on compound interest
how_it_works = """
Compound interest is the process of earning interest on both your initial principal and the accumulated interest from previous periods, often described as "interest on interest". Unlike simple interest, it causes investments or debts to grow at an accelerating rate over time, acting like a snowball effect. 

The formula for calculating compound interest is A = P(1+r/n)\u207f\u1d57
where, A = Final amount, P = Principal, r = Annual interest rate, n = Compounding frequency per year, t = Time in years

Compound Interest Example (GHc 1,000 at 10% annually for 3 years,)
Y1: Interest = GHc100.00, Total amount = GHc1100.00
Y2: Interest = GHc210.00, Total amount = GHc1210.00
Y3: Interest = GHc331.00, Total amount = GHc1331.00
"""



#Mar 14, 2026 - 03:39
#calculation of compound interest
def calc_interest():
    try:
        principal = float(input("\nEnter principal amount: "))
        time_period = int(input("Enter time(in years): "))
        rate = float(input("Enter rate(%): "))
    except ValueError:
        print("Invalid input! Kindly try again\n")
        calc_interest()

    time.sleep(0.4)
    print("\nSelect compounding frequency:")
    print("1. Annually")
    print("2. Semi-annually")
    print("3. Quartely")
    print("4. Monthly") 
    print("5. Daily")

    frequencies = [0, 1, 2, 4, 12, 365]
    n = 1

    try:
        cf = int(input("\nYour choice: "))
        if cf in range(1, 6):
            n = frequencies[cf]
        else:
            print("Choice not in menu\n")
            calc_interest()
    except ValueError:
        print("Invalid input! Kindly try again\n")
        calc_interest()

    print("")
    t = 1

    try:
        while t <= time_period:
            amount = principal * (1 + (rate/100)/n) ** (n*t)
            period_interest = amount - principal
            
            time.sleep(0.5)
            print(f"Year {t}: Interest earned = GHc{period_interest:.2f}, Total amount = GHc{amount:.2f}")
            t += 1
    except OverflowError:
        time.sleep(0.5)
        print("\nInvalid computation. Answer is too huge")


    time.sleep(0.5)
    end = input("\nPress ENTER to continue or type quit to end the program\n\n")
    if end.lower() == "quit":
        quit()
    time.sleep(0.8)
    main()



#check for updates
def check_for_updates():
    print("Checking for updates", end="")
    for _ in range(6):
        time.sleep(0.6)
        print(".", end="")
        sys.stdout.flush()
    print("\n\n")
    webbrowser.open("https://github.com/self-reliantkid/Compound-Interest-Calculator/releases/latest")



#quit program
def quit():
    print("Program quit successful!")
    time.sleep(0.5)
    sys.exit()



if __name__ == "__main__":
    main()