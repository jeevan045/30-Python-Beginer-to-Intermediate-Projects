import random
print("-"*40)
print("Welcome to Rock Paper and Scissors!")
print("-"*40)
while True:
    user_input = input("Choose Rock , Paper or Scissor : ").capitalize()
    lis = ['Rock','Scissor', 'Paper']
    computer_choice = random.choice(lis)
    print(f"Your choice = {user_input} and computer choice = {computer_choice}")
    if user_input == computer_choice:
        result = "Draw !"
    elif (user_input == "Rock" and computer_choice == "Scissor") or \
            (user_input == "Scissor" and computer_choice == "Paper") or \
            (user_input == "Paper" and computer_choice == "Rock"):
        result = "You Win !!"
    else:
        result = "You Lose !!"
    print("-" * 10)
    print(result)
    print("-" * 10)
