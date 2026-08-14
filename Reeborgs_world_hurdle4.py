def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif right_is_clear() == True and front_is_clear() or wall_in_front() == True:
        if front_is_clear() and right_is_clear():
            turn_right()
            move()
        else:
            turn_right()
            move()

