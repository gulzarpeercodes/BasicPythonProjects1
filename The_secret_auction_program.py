print('''                ___________
                         I         I
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         I_________I
                         `'-------'`
                       .-------------.
                      I_______________I
''')


empty_dict = {}
loop = True
while loop:
    bidder_dict = {}

    user_name = input("What is your name?: ").capitalize()
    bid_amount = int(input("What is your bid?: $"))

    bidder_dict[user_name] = bid_amount
    empty_dict.update(bidder_dict)
    continue_bidding = input("Are there any other bidders? Type 'Yes' or 'No': ").lower()

    if continue_bidding == "no":
        loop = False
        winner = max(empty_dict, key=empty_dict.get)
        print(f"The winner is {winner} with a bid of {empty_dict[winner]}.")
    elif continue_bidding == "yes":
        loop = True
        print("\n" *100)
    else:
        loop = False
        print("You typed an invalid command!")
