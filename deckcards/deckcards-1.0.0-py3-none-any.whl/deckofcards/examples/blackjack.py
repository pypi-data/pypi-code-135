import os
import time
import deckofcards as dc
from typing import List

def clear_console():
    """Use this function to delete the last line in the STDOUT
    """
    os.system("clear")

def get_score(hand: List[dc.Card], name='player', log=True, show_all=True) -> int:
    """Computes and return score
    By default logs hands
    """
    score = sum([c.value for c in hand])
    ranks = [c.rank for c in hand]
    # Ace score = 11 if any picture card in hand
    if 'A' in ranks:
        if any([c.rank in ['J', 'Q', 'K'] for c in hand]):
            score += 10
    if log:
        last_card = hand[-1]
        cards = ''.join([f"|{str(h)}|" for h in hand[:-1]])
        if not show_all:
            last_card = "? ?"
            score -= hand[-1].value
        message = f"{name}'s cards: {cards}|{str(last_card)}|{'':5s}"
        message += f"\t-> score: {score}"
        print(message)
    return score

def playBlackJack():
    deck = dc.Deck()
    # set acctual values for ranks
    for card in deck.pack:
        if card.rank in dc.Card.pictures:
            card.value = 10
        elif card.rank == 'A':
            card.value = 1
    # two cards each
    player, dealer = deck.deal()
    # Display inital configuration
    clear_console()
    print("------------")
    dealer_score = get_score(dealer, name='Dealer', show_all=False)
    player_score = get_score(player)

    # starts rounds
    message = "- Type s for stand or h for hit: "
    action = 'h'
    on_player = True
    play = True
    while play:
        # when game on player
        if (player_score < 21) and on_player:
            action = input(message)
            # if not any([action.upper() == a for a in ('S', 'H')]):
            if action.upper() == 'S':
                on_player = False
                time.sleep(1)
            elif action.upper() == 'H':
                clear_console()
                print("------------")
                player.append(deck.draw())
                dealer_score = get_score(dealer, name='Dealer', show_all=False)
                player_score = get_score(player)
            else:
                print("You must type either 's' or 'h'")
        elif player_score > 21:
            print("Player busted and losse!")
            play = False
        elif player_score == 21:
            print("Player wins!")
            play = False
        # the end game
        else:
            clear_console()
            print("------------")
            dealer_score = get_score(dealer, name='Dealer', show_all=False)
            player_score = get_score(player)
            time.sleep(1)
            while dealer_score < 17:
                time.sleep(1.5)
                clear_console()
                print("------------")
                dealer.append(deck.draw())
                dealer_score = get_score(dealer, name='Dealer')
                player_score = get_score(player)
                time.sleep(1)
            if dealer_score > 21:
                print("Dealer busted and player win!")
            elif player_score >= dealer_score:
                print("Player wins!")
            else:
                print("Dealer win!")
            play = False
    
    
class BlackJack:
    def __init__(self) -> None:
        pass
    def run(self,) -> None:
        playBlackJack()


if __name__ == '__main__':
    playBlackJack()
