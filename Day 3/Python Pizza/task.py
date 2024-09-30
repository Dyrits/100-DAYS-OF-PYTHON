print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M or L: ").upper()

prices = {
    "S": 15,
    "M": 20,
    "L": 25
}

bill = 0

if size == "S" or size == "M" or size == "L":
    bill += prices[size]
else:
    print("You have chosen an invalid size.")

if bill > 0:
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()

    if pepperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3

    extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

    if extra_cheese == "Y":
        bill += 1

    print(f"Your final bill is: ${bill}.")
