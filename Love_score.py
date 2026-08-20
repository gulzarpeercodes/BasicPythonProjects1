def calculate_love_score(name1, name2):
    combined_names = name1 + name2
    lower_names = combined_names.lower()

    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")

    true = t + r + u + e

    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")

    love = l + o + v + e

    score = str(int(true)) + str(int(love))
    print(f"Your love score is {score}")

calculate_love_score(name1="", name2="")
