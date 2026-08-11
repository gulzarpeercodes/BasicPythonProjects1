print("Welcome to amazing roller coaster ride!")
user_height = int(input("Write down your height in centimeters: "))
bill = 0

if user_height >= 150:
    print("You can ride the roller coaster.")
    user_age = int(input("Write down your age: "))
    if user_age <= 12:
        bill = 5
        print("Child tickets are $5")
    elif user_age <= 18:
        bill = 10
        print("Youth tickets are $10")
    else:
        bill = 15
        print("Adult tickets are $15")

    photo = input("Do you want to have your photo taken? if YES type 'yes' and if NO type 'no': ").upper()
    if photo == "YES":
        bill += 3
        print(f"You have to pay ${bill} (Photos included)")
    else:
        print(f"You have to pay ${bill} (photos not included)")
else:
    print("Sorry you cannot ride the roller coaster.")