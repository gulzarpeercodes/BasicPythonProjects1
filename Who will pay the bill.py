import random
#edit this
friends = ["Rayaan", "Shahzan", "Sanan", "Kamraan", "Hishaam"]
index_friends = random.randint(0,4)
if index_friends == 0:
    print(f"{friends[4]} is going to pay.")
elif index_friends == 1:
    print(f"{friends[3]} is going to pay.")
elif index_friends == 2:
    print(f"{friends[2]} is going to pay.")
elif index_friends == 3:
    print(f"{friends[1]} is going to pay.")
elif index_friends == 4:
    print(f"{friends[0]} is going to pay.")