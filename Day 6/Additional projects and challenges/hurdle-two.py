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

def turn_right():
    for _ in range(3):
        turn_left()

def move_and_turn_left():
    move()
    turn_left()

def move_and_turn_right():
    move()
    turn_right()

def move_over_obstacle():
    move_and_turn_left()
    move_and_turn_right()
    move_and_turn_right()
    move_and_turn_left()

while not at_goal():
    move_over_obstacle()
