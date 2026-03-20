#Checklist
#Show year-by-year growth
#Show both interest earned and amount
#Allowing different compounding frequency

#v1.1 - Error handling issues addressed (Mar 20, 2026 - 01:44)


#Mar 14, 2026 - 03:39
def calc_interest():
    try:
        principal = float(input("Enter principal amount: "))
        time = int(input("Enter time(in years): "))
        rate = float(input("Enter rate(%): "))
    except ValueError:
        print("Invalid input! Kindly try again\n")
        calc_interest()

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

    while t <= time:
        amount = principal * (1 + (rate/100)/n) ** (n*t)
        period_interest = amount - principal

        print(f"Year {t}: Interest earned = GHc{period_interest:.2f}, Total amount = GHc{amount:.2f}")
        t += 1

    end = input("\nPress ENTER to continue or type quit to end the program\n\n")
    if end.lower() == "quit":
        print("Program quit successful!")
        return
    calc_interest()


if __name__ == "__main__":
    calc_interest()