print("Welcome to Tip Calculator! \nCalculate your Tip just by few clicks!")

total_bill = float(input("What is the total bill? $"))
tip = int(input("What percentage of tip would you like to give? 5 , 10 or 15? "))
people = int(input("How many people to split the bill? "))

calculated_tip = tip/100
calculated_bill_tip = calculated_tip * total_bill
total_calculated_bill = calculated_bill_tip + total_bill
bill_split = total_calculated_bill /people

final_bill = round(bill_split, 2)

print(f"Each person should pay: ${final_bill}, Thank you.")

