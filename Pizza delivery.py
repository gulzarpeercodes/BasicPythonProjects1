print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size of Pizza do you want? Small , Medium or Large?\n").lower()
if size == "small":
    bill = 15
    print(f"Small Pizza is ${bill} ")
    pineapple = input("Do you want Pineapple on your Pizza? Yes or No?\n ").lower()
    if pineapple == "yes":
        bill += 2
        print(f"You have to pay ${bill} with Pineapple on top.")
    extra_cheese = input("Do you want Extra Cheese on your Pizza? Yes or No?\n").lower()
    if extra_cheese == "yes":
        bill += 1
        print(f"Your total bill is ${bill}")
    else:
        print(f"Your total bill is ${bill}")


elif size == "medium":
    bill = 20
    print(f"Medium Pizza is ${bill}")
    pineapple = input("Do you want Pineapple on your Pizza? Yes or No?\n ").lower()
    if pineapple == "yes":
        bill += 3
        print(f"You have to pay ${bill} with Pineapple on top.")
    extra_cheese = input("Do you want Extra Cheese on your Pizza? Yes or No?\n").lower()
    if extra_cheese == "yes":
        bill += 1
        print(f"Your total bill is ${bill}")
    else:
        print(f"Your total bill is ${bill}")

elif size == "large":
    bill = 25
    print(f"Large Pizza is ${bill}")
    pineapple = input("Do you want Pineapple on your Pizza? Yes or No?\n ").lower()
    if pineapple == "yes":
        bill += 3
        print(f"You have to pay ${bill} with Pineapple on top.")
    extra_cheese = input("Do you want Extra Cheese on your Pizza? Yes or No?\n").lower()
    if extra_cheese == "yes":
        bill += 1
        print(f"Your total bill is ${bill}")
    else:
        print(f"Your total bill is ${bill}")

else:
    print("You typed the wrong input.")



