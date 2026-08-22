
def add(n1,n2):
    return n1 + n2

def subtract(n1,n2):
    return n1 - n2

def multiply(n1,n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {"+" : add,
              "-" : subtract,
              "*" : multiply,
              "/" : divide }

def calculator():
    print(''' 
 _____________________
|  _________________  |
| |Gulzar peer Cal  | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|''')
    should_accumulate = True
    first_number = float(input("What is the first number?: "))
    while should_accumulate:
       for operation in operations:
            print(operation)
       user_operation = input("Pick an operation: ")
       second_number  = float(input("What is the next number?: "))
       result = operations[user_operation](first_number,second_number)
       print(f"{first_number} {user_operation} {second_number} = {result}")

       user_choice = input(f"Type 'Yes' to continue calculating with {result}, or type 'No' to start a new calculation: ").lower()

       if user_choice == "yes":
            first_number = result
       else:
           should_accumulate = False
           print("\n" * 20)
           calculator()


calculator()