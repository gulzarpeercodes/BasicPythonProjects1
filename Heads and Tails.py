import random
print("Welcome to Heads and Tails game!")
call = input("What is your call? 'Heads' or 'Tails'?\n").capitalize()
random_integer = random.randint(1,2)
if random_integer == 1:
    random_integer = "Heads"
    print("Heads")
else:
    random_integer = "Tails"
    print("Tails")

print(f"{call} is the call and {random_integer} it is. ")