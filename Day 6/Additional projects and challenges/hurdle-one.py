# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# This function is already defined in the Reeborg's World~
def turn_left():
    return

# This function is already defined in the Reeborg's World~
def move():
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

for _ in range(6):
    move_over_obstacle()
