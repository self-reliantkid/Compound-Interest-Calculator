#Checklist
#Show year-by-year growth
#Show both interest earned and amount
#Allowing different compounding frequency


#Mar 14, 2026 - 03:39
def calc_interest():
    principal = int(input("Enter principal amount: "))
    time = int(input("Enter time(in years): "))
    rate = float(input("Enter rate(%): "))

    print("\nSelect compounding frequency:")
    print("1. Annually")
    print("2. Semi-annually")
    print("3. Quartely")
    print("4. Monthly") 
    print("5. Daily")

    cf = int(input("\nYour choice: "))

    n = 1

    try:
        if cf == 2:
            n = 2
        elif cf == 3:
            n = 4
        elif cf == 4:
            n = 12
        elif cf == 5:
            n = 365
    except ValueError:
        print("Invalid input!")

    print("")
    t = 1

    while t <= time:
        amount = principal * (1 + (rate/100)/n) ** (n*t)
        period_interest = amount - principal

        print(f"Year {t}: Interest earned = GHc{period_interest:.2f}, Total amount = GHc{amount:.2f}")
        t += 1


if __name__ == "__main__":
    calc_interest()