print("-"*50)
print("Welcome to the Blind Bidder !!")
print("-"*50)
def calculate_bid_amount(bidding_dictionary):
    winner = ""
    maximum_amount = 0
    for bid in bidding_dictionary:
        am = bidding_dictionary[bid]
        if am > maximum_amount:
            maximum_amount = am
            winner = bid
    print("-"*50)
    print(f"The winner is {winner} with amount ${maximum_amount} 🎉")
    print("-" *50)
bids = {}
while_con = True
while while_con:
    user = input("Enter your name : ")
    bid_amount = int(input("Enter the bidding amount ($): "))
    bids[user] = bid_amount
    continuation = input("Is there any players left to Bid ? (y/n) : ").lower()
    if continuation == "n":
        while_con = False
        print("Thank you for Bidding! 🙌")
        calculate_bid_amount(bids)
    elif continuation == "y":
        print("\n" * 40)

