print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15 ?" + "\n"))
people = int(input("How many people to split the bill?" + "\n"))

total = (bill + (bill * tip / 100)) / people

print(f"Each person should pay: ${total:.2f}")