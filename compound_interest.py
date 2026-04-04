#Checklist
#Show year-by-year growth
#Show both interest earned and amount
#Allowing different compounding frequency

#v1.1 - Error handling issues addressed (Mar 20, 2026 - 01:44)
#v1.2 -

import webbrowser
import time
import sys
#import math



#main menu
def main():
    print("Compound Interest Calculator")
    print(" 1. Calulate compound interest")
    print(" 2. How compound interest works")
    print(" 3. How to use this app")
    print(" 4. Change default currency")
    print(" 5. Check for updates")
    print(" 6. Quit")


    try: #error handling for user inputs
        user_choice = int(input("\nYour choice: "))

        if user_choice in range(1, 7):
            if user_choice == 1:
                interest_menu()
            elif user_choice == 2:
                print(how_it_works)
                time.sleep(3)
                in_app()
            elif user_choice == 3:
                print(how_to_use)
                time.sleep(3)
                in_app()
            elif user_choice == 4:
                change_currency()
                time.sleep(0.8)
                in_app()
            elif user_choice == 5:
                check_for_updates()
                time.sleep(0.8)
                main()
            elif user_choice == 6:
                quit()
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



#explanation on how users can use this app
how_to_use = """
INTRODUCTION:
This is a simple command-line app for calculating compound interest. The app is also able to compound based on certain time frequencies and shows the snowball effect through yearly breakdowns.


NAVIGATING THE APP:

A. Main Menu
I. Option 1 - Calculate compound interest
This is the first noticeable option from the menu. This option allows you to perform compound interest calculations. A series of sub-menus appear requesting for information such as principal amount, time period and rate(%). There is also a sub-menu which follows to decide on the compounding frequency.
After completing the sub-menus, the app then generates the interest earned and the total amount for each year until the final year or in selected intervals for longer time periods.

II. Option 2 - How compound interest works
This is the second option on the main menu. This option explains the core about calculating compound interest and how compounding works over time. It also states the exact formula used for calculations and an example for users to appreciate.

III. Option 3 - How to use this app
This is the currently selected option. It provides a comprehensive guide on how to effectively use the app and troubleshooting in case of any difficulties.

IV. Option 4 - Change default currency
This option allows users to set a currency for compound interet calculations. Users can choose between five different currencies with GHc as default.

V. Option 5 - Check for updates
This option allows users to fetch the latest update to this app. Users are directed to the app's releases page on GitHub and can check for any available updates.

VI. Option 6 - Quit
This is the final option on the main menu. Users can quit the app seamlessly using this option.


B. In-app Menu
The in-app menu is a sub-menu which appears after executing the first three options in the main menu. This menu allows users to seamlessly switch back to the main menu or directly quit the app.
"""



currency = "GHc"



#Mar 14, 2026 - 03:39
def interest_menu():
    #variables made global to access in other functions
    global principal
    global time_period
    global rate
    global n

    try: #error handling
        principal = float(input(f"\nEnter principal amount({currency}): "))
        time_period = int(input("Enter time(in years): "))
        rate = float(input("Enter rate(%): "))
    except ValueError:
        print("Invalid input! Kindly try again\n")
        interest_menu()

    time.sleep(0.4)

    #selecting compounding frequency
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
            interest_menu()
    except ValueError:
        print("Invalid input! Kindly try again\n")
        interest_menu()

    print("")

    #logic to handle time periods above 50 years

    if time_period > 50:
        i1 = round(time_period//10, len(str(time_period))-2) #first interval
        i2 = i1 * 2 #second interval

        time.sleep(0.3)

        print("Time period is too huge. Choose preferred interval:")
        print(f" 1. {i1} years")
        print(f" 2. {i2} years")
        print(" 3. First year and last year only")

        intervals = [1, i1, i2, time_period]
        try:
            user_choice = int(input("\nYour choice: "))
            time.sleep(0.2)

            if user_choice in range(1, 4):
                if user_choice == 1 or user_choice == 2:
                    print(f"\nGenerating interest for first year, last year and every {intervals[user_choice]}th year", end="")
                else:
                    print("\nGenerating interest for first year and last year only", end="")

            else:
                print("Option not in menu\n")
                interest_menu()
                
        except ValueError:
            print("Invalid input! Kindly try again\n")
            interest_menu()

        delay()

        time.sleep(0.5)
        calc_interest(1)
        calc_interest(intervals[user_choice], time_period)

        if time_period%5 != 0 and user_choice != 3:
            calc_interest(time_period, time_period)

    else:
        calc_interest(dur=time_period)

    time.sleep(0.8)
    in_app()



#calculation of compound interest
def calc_interest(i=1, dur=1):
    t = i
    try:
        while t <= dur:
            amount = principal * (1 + (rate/100)/n) ** (n*t)
            period_interest = amount - principal
            
            time.sleep(0.5)
            print(f"Year {t}: Interest earned = {currency}{period_interest:.2f}, Total amount = {currency}{amount:.2f}")
            t += i
    except OverflowError:
        time.sleep(0.5)
        print("\nInvalid computation. Answer is too huge")



#change of currency
def change_currency():
    global currency

    print(f"\nCurrent default currency is '{currency}'. Select an option from the menu below:")
    print(" 1. $ - US Dollar")
    print(" 2. € - Euro")
    print(" 3. £ - British Pound")
    print(" 4. ¥ - Japanese Yen")
    print(" 5. GHc - Ghana Cedi")

    user_choice = int(input("\nYour choice: "))

    currency_list = ["", "$", "€", "£", "¥", "GHc"]

    try:
        if user_choice in range(1, 6):
            if currency_list[user_choice] == currency:
                print("Default currency maintained!\n\n")
            else:
                print("Currency change successful!\n\n")
                currency = currency_list[user_choice]
            time.sleep(0.6)
            main()
        else:
            print("Option not in menu\n")
            time.sleep(0.5)
            change_currency()
    
    except ValueError:
        print("Invalid input. Kindly try again!\n")
        time.sleep(0.8)
        change_currency()



#check for updates
def check_for_updates():
    print("Checking for updates", end="")
    delay()
    webbrowser.open("https://github.com/self-reliantkid/Compound-Interest-Calculator/releases/latest")



#quit program
def quit():
    print("Quiting program", end="")
    delay(0)

    time.sleep(0.5)
    print("Program quit successful!")
    sys.exit()



def in_app():
    print("\nReturn to main menu?")
    print(" 1. Yes")
    print(" 2. Quit")

    try:
        user_choice = int(input("\nYour choice: "))

        if user_choice in range(1, 3):
            if user_choice == 1:
                print("\n")
                time.sleep(1)
                main()
            else:
                quit()
        else:
            print("Option not in menu\n")
            time.sleep(0.5)
            in_app()

    except ValueError:
        print("Invalid input. Kindly try again!\n")
        time.sleep(0.8)
        in_app()



#delay function
def delay(i=2):
    for _ in range(6):
        time.sleep(0.6)
        print(".", end="")
        sys.stdout.flush()
    print('\n' * i)



if __name__ == "__main__":
    main()