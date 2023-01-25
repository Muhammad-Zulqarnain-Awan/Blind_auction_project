# import OS library and logo from art.py file 
import os
from art import logo

# Defining clear function for clearing screen 
def clear():
    return os.system('cls')

# Defining function which can find highest bid
def highest_bid(bidders_detail):
    winner_name = ''
    highest_amount = 0
    for name in bidders_detail:
        if bidders_detail[name] > highest_amount:
            highest_amount = bidders_detail[name]
            winner_name = name
    print(f"\nThe highest bid is ${highest_amount} from {winner_name}.")

# Initialize an empty dictionary for storing bidder name and amount 
bidders_detail = {}

# Created a variable name end and assigned False 
end = False

# Run a while loop until end become true 
while not end:
    print(logo)
    bidder_name = input("\nWhat's your name?\nName: ")
    bidding_amount = int(input("\nWhat's your bidding amount?\nAmount: "))
    bidders_detail[bidder_name] = bidding_amount

    # Check if there is any other bidder or not 
    run_again = input("\nIs there any other bidder?\nType 'Y' for YES or 'N' for NO.\nEnter: ").lower()

    # if there is no bidder then end the program and show the highest bidder 
    if run_again == 'n':
        end = True
        clear()
        highest_bid(bidders_detail)
    
    # if there is bidder left, then simply clear the screen and ask for his name and bidding amount 
    elif run_again == 'y':
        clear()