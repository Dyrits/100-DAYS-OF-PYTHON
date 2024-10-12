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
def wall_on_right():
    return

def turn_right():
    for _ in range(3):
        turn_left()

while not at_goal():
    if wall_on_right() and front_is_clear():
        move()
    elif not wall_on_right():
        turn_right()
        move()
    else:
        turn_left()