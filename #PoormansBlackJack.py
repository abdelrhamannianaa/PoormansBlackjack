#PoormansBlackJack
import random
from art import logo
def deal_card():
    # this returns a card randomly pulled from the deck
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

def draw_and_calculate(card_list):
    ''' this function calculates the total score
      of the cards and accounts for the 
      edge case of the Ace being both 1 and 11
    '''
    card_list.append(deal_card())
    ace_check(card_list)
    return sum(card_list)

def populate_card(card_list):
    '''this function starts off both decks with 2 cards'''
    for _ in range(2):
        card_list.append(deal_card())
        ace_check(card_list)

def ace_check(card_list):
    ''' checks the ace edge case where an ace could be both 1 and 11 depending on your score'''
    while sum(card_list) > 21 and (11 in card_list):
        card_list.remove(11)
        card_list.append(1)
    return card_list
def winner_winner(user_total,computer_total,computer_cards):
        while computer_total < 17 and user_total < 21:
            print("Your dealer decided to draw one more card")
            computer_total = draw_and_calculate(computer_cards)
        print(f"Your dealer's cards are {computer_cards}")
        if (player_total == computer_total) or (player_total > 21 and computer_total > 21):
            print("You drew, what are the odds huh")
        elif (player_total <= 21 and player_total > computer_total) or (computer_total > 21):
            print("Who would've thought luck was on your side. You win!")
        elif (computer_total > player_total) or (player_total > 21):
            print("IDK why you even played, we know you suck. You lost. ")
print(logo)   
print("Welcome to the official poorman's Blackjack")

#ask the player if they want to play
continueGame = True
while continueGame:
    playerChoice1 = input("Would you like to play a game of Blackjack?: y/n ").lower()
    if playerChoice1 == "n":
        print("Goodbye, you were gonna lose anyway!")
        continueGame = False
    else:
        # populating each player's deck
        user_cards = []
        computer_cards =[]
        populate_card(user_cards)
        populate_card(computer_cards)
        print(f"these are your cards {user_cards} ")
        print(f"Your opponent has {computer_cards[0]} ")
        computer_total = sum(computer_cards)
        player_total = sum(user_cards)
        anotherCard = input("Do you want to draw another card? y/n :").lower() # first card draw option
        if anotherCard == "n":
            winner_winner(player_total,computer_total,computer_cards)
        else:
            player_total = draw_and_calculate(user_cards)
            print(f"Your cards are {user_cards}. Your total score is {player_total}")
            draw_another = True
            while computer_total < 21 and player_total <21 and draw_another:
                userDeal = input("Do you want to draw another card? y/n: ").lower()
                if userDeal == "y":
                    player_total = draw_and_calculate(user_cards)
                    print(f"Your cards are {user_cards}. Your total score is {player_total}")
                elif userDeal == "n":
                    draw_another = False
            winner_winner(player_total,computer_total,computer_cards)
            

    
        

