def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif right_is_clear() and wall_in_front():
        turn_right()
        move()
    elif right_is_clear():
        if right_is_clear() and wall_in_front():
            turn_right()
        elif front_is_clear() and right_is_clear():
            turn_right()
            move()
        else:
            move()

