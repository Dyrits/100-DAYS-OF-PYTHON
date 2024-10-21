from art import logo

bids = {}

def add_bidder():
    name = input("What is your name?" + "\n")
    price = int(input("What's your bid?" + "\n" + "$"))
    bids[name] = price

def compare_bids():
    max_bid = max(bids.values())
    winners = [name for name, bid in bids.items() if  bid == max_bid]
    if len(winners) > 1:
        print("There is a tie. Please try again.")
    else:
        print(f"The winner is {winners[0]} with a bid of ${max_bid}.")

def repeat():
    more_bids = input("Are there any other bidders? (Yes/No)" + "\n").upper()
    if more_bids == "YES":
        add_bidder()
        return True
    elif more_bids == "NO":
        return False
    else:
        print("Invalid input. Please try again.")
        repeat()

if __name__ == "__main__":
    print(logo)
    print("Welcome to the secret auction program.")
    add_bidder()
    while repeat():
        pass
    else:
        compare_bids()

