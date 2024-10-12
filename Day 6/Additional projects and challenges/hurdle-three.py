# https://reeborg.ca/

# This function is already defined in the Reeborg's World~
def turn_left():
    return

# This function is already defined in the Reeborg's World~
def move():
    return

# This function is already defined in the Reeborg's World~
def at_goal():
    return

# This function is already defined in the Reeborg's World~
def front_is_clear():
    return

# This function is already defined in the Reeborg's World~
def wall_in_front():
    return

def turn_right():
    for _ in range(3):
        turn_left()

def move_and_turn_right():
    move()
    turn_right()

def move_over_obstacle():
    turn_left()
    move_and_turn_right()
    move_and_turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        move_over_obstacle()