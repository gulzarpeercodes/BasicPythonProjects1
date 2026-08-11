print("Welcome to amazing roller coaster ride!")
user_height = int(input("Write down your height in centimeters: "))

if user_height >= 150:
    print("You can ride the roller coaster.")
    user_age = int(input("Write down your age: "))
    if user_age <= 12:
        print("Please pay $5")
    elif user_age <= 18:
        print("Please pay $10")
    else:
        print("Please pay $15")
else:
    print("Sorry you cannot ride the roller coaster.")