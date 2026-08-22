
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


loop = True
while True:
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

        first_number = float(input("What is the first number?: "))

        for operation in operations:
            print(operation)

        user_operation = input("Pick an operation: ")

        second_number  = float(input("What is the second number?: "))

        result = operations[user_operation](first_number,second_number)

        loop_result = result

        print(f"{first_number} {user_operation} {second_number} = {result}")

        user_choice = input(f"Type 'Yes' to continue calculating with {result}, or type 'No' to start a new calculation: ").lower()
        if user_choice == "yes":
            loop = True
            while loop:
                for operation in operations:
                    print(operation)
                user_operation2 = input("Pick an operation: ")

                next_number = float(input("What is the next number?: "))

                result2 = operations[user_operation2](loop_result, next_number)

                print(f"{loop_result} {user_operation2} {next_number} = {result2}")

                loop_result = result2

                user_choice2 = input(f"Type 'Yes' to continue calculating with {result2}, or type 'No' to start a new calculation: ").lower()
                if user_choice2 == "no":
                    loop = False
                    print("\n"*20)


"""| Your code                                | Problem                                  | Correct                                 |
| ---------------------------------------- | ---------------------------------------- | --------------------------------------- |
| `loop_result += result`                  | Adds to old result                       | `loop_result = result`                  |
| `loop_result = result2` before `print()` | Changes value before displaying it       | Print first, then update                |
| `loop = True` outside everything         | Can cause problems when reusing the loop | Put it inside `if user_choice == "yes"` |
| `muti = ...`                             | Unused variable                          | Remove it                               |
 These were the mistakes i had made"""
