print("-"*40)
print("Welcome to TIP calculator !!")
print("-"*40)
while True:
    total = float(input("What is your total bill ? :$ "))
    tip = float(input("How much is the tip do you like to give (12,15,20) ? : "))
    total += tip/100
    mem = int(input("How many members to split the bill ? : "))
    bill = round(total / mem,2)
    print(f"Each person should pay $ {bill}")
    en = input("Do you want to end the Transaction ? (Yes/No) : ")
    if en == "Yes" or en == "yes":
        break

