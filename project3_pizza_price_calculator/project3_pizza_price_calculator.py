print("-"*40)
print("Welcome to the Pizza price Calculator !!")
print("-"*40)
while True:
    total = 0
    pizza_size = input("Which type of Pizza do you want? (S, L, or M  )? : ")
    if pizza_size == "S":
        total += 15
    elif pizza_size == "L":
        total += 25
    else :
        total += 20
    pepperoni = input("Do you want pepperoni over pizza ?(Y/N) : ")
    if pepperoni == "Y":
        if pizza_size == "M" or pizza_size == "L":
            total += 3
        else:
            total += 2
    cheeze = input("Do you want cheeze over pizza ?(Y/N) : ")
    if cheeze == "Y":
        total += 1
        print("-"*40)
    print(f"Your total Order Bill Amount is - ${total}")
    print("-" * 40)