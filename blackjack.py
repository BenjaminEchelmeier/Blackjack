"""
This is a text simulation of Blackjack, somewhat simplified.
All code herein is original to Benjamin Echelmeier
"""
from random import shuffle


class Card:
    """
    Cards are created to populate the deck.
    """

    def __init__(self, value, card_name=""):
        """
        Generates a card to populate a deck
        :param value: int
        """
        self.value = value
        self.name = card_name
        if self.name == "":
            self.name = value
        self.suit = None

    def __str__(self):
        """
        :return: if object has name, retruns self.name, else returns self.value
        """
        return f"{self.name} of {self.suit}s"

    def change_value(self, value):
        self.value = value

    def change_name(self, card_name):
        self.name = card_name

    def change_suit(self, suit):
        if suit == 0:
            self.suit = "Spade"
        elif suit == 1:
            self.suit = "Club"
        elif suit == 2:
            self.suit = "Heart"
        elif suit == 3:
            self.suit = "Diamond"
        else:
            self.suit = suit


class Deck:
    """
    The deck is intended to be generated at the begging of each round. This replaces shuffling.
    """

    def __init__(self):
        """
        Deck is generated with 52 cards, each with a Blackjack value.
        """
        # cards are created and assigned values
        a_of_spades = ace_of_clubs = ace_of_hearts = ace_of_diamonds = Card(11, "Ace")
        k_of_spades = king_of_clubs = king_of_hearts = king_of_diamonds = Card(10, "King")
        q_of_spades = q_of_clubs = q_of_hearts = q_of_diamonds = Card(10, "Queen")
        j_of_spades = j_of_clubs = j_of_hearts = j_of_diamonds = Card(10, "Jack")
        ten_of_spades = ten_of_clubs = ten_of_hearts = ten_of_diamonds = Card(10)
        nine_of_spades = nine_of_clubs = nine_of_hearts = nine_of_diamonds = Card(9)
        eight_of_spades = eight_of_clubs = eight_of_hearts = eight_of_diamonds = Card(8)
        seven_of_spades = seven_of_clubs = seven_of_hearts = seven_of_diamonds = Card(7)
        six_of_spades = six_of_clubs = six_of_hearts = six_of_diamonds = Card(6)
        five_of_spades = five_of_clubs = five_of_hearts = five_of_diamonds = Card(5)
        four_of_spades = four_of_clubs = four_of_hearts = four_of_diamonds = Card(4)
        three_of_spades = three_of_clubs = three_of_hearts = three_of_diamonds = Card(3)
        two_of_spades = two_of_clubs = two_of_hearts = two_of_diamonds = Card(2)

        # hid and revealed decks are generated, and the hid deck is populated with cards
        self.revealed = []
        self.hid = [a_of_spades, ace_of_clubs, ace_of_hearts, ace_of_diamonds,
                    k_of_spades, king_of_clubs, king_of_hearts, king_of_diamonds,
                    q_of_spades, q_of_clubs, q_of_hearts, q_of_diamonds,
                    j_of_spades, j_of_clubs, j_of_hearts, j_of_diamonds,
                    ten_of_spades, ten_of_clubs, ten_of_hearts, ten_of_diamonds,
                    nine_of_spades, nine_of_clubs, nine_of_hearts, nine_of_diamonds,
                    eight_of_spades, eight_of_clubs, eight_of_hearts, eight_of_diamonds,
                    seven_of_spades, seven_of_clubs, seven_of_hearts, seven_of_diamonds,
                    six_of_spades, six_of_clubs, six_of_hearts, six_of_diamonds,
                    five_of_spades, five_of_clubs, five_of_hearts, five_of_diamonds,
                    four_of_spades, four_of_clubs, four_of_hearts, four_of_diamonds,
                    three_of_spades, three_of_clubs, three_of_hearts, three_of_diamonds,
                    two_of_spades, two_of_clubs, two_of_hearts, two_of_diamonds]

        # iteration is used to assign suite to cards
        for item in range(0, 52, 4):
            # assign suits
            for i in range(0, 4):
                self.hid[item].change_suit(i)

    def shuffle(self):
        """
        Shuffles the deck
        """
        shuffle(self.hid)

    def draw(self):
        card = self.hid.pop()
        self.revealed.append(card)
        return card


class Player:
    """
    The basis for a player in the game. Currently designed for a single player.
    """

    def __init__(self, player_name, bankroll=100):
        """
        Initialize the player. Intended for use at the start of the game.
        :param player_name: str variable; fill with player's name. stored as self.name
        :param bankroll: int variable; fill with player's initial bankroll (in USD). Defaults to $20
        """
        self.name = player_name
        self.bankroll = bankroll

    def change_money(self, number):
        self.bankroll += number


class Hand:
    """
    Hand objects are intended to be created at the start of each round for both the dealer and
    each player.
    """

    def __init__(self, card):
        self.cards = [card]
        self.value = card.value
        self.bust = False

    def hit(self, card):
        self.cards.append(card)
        self.value += card.value
        while self.value > 21 and not self.bust:
            for card in self.cards:
                if card.value == 11:
                    self.value -= 10
                    card.change_value(1)
                    break
            if self.value > 21:
                self.bust = True
                break

    def eval(self):
        print(f"\nYour cards are:")
        for card in self.cards:
            print(card)
        print(f"with a value of {self.value}")

    def dealer_eval(self):
        print(f"\nThe dealer's cards are:")
        for card in self.cards:
            print(card)
        print(f"with a value of {self.value}")

    def show(self):
        print(f"\nThe dealer shows the {self.cards[0]}.")

    def stand(self):
        pass


def play_round():
    deck = Deck()
    deck.shuffle()
    global player
    bet = input(f"\nYou have ${player.bankroll}. How much do you want to bet?\n$")
    try:
        bet = int(bet)
    except:
        bet = -5455531
    while not (5 <= bet <= player.bankroll):
        if bet > player.bankroll:
            bet = input(f"You only have ${player.bankroll}! How much do you really want to bet?\n$")
            try:
                bet = int(bet)
            except:
                bet = -5455531
        elif bet < 5 and not (bet == -5455531):
            bet = input("You 'gotta bet at least $5! How much do you really want to bet?\n$")
            try:
                bet = int(bet)
            except:
                bet = -5455531
        else:
            print("What!? Please just give me a number.")
            bet = input(f"\nYou have ${player.bankroll}. How much do you want to bet?\n$")
            try:
                bet = int(bet)
            except:
                bet = -5455531
    player.change_money(-bet)
    hand = Hand(deck.draw())
    dealer = Hand(deck.draw())
    hand.hit(deck.draw())
    hand.eval()
    dealer.show()
    choice = ""
    while choice != "S":
        choice = input("\nWould you like to (H)it, (D)ouble Down or (S)tand?\n").upper()
        if choice == "H":
            hand.hit(deck.draw())
            hand.eval()
        elif choice == "D":
            if bet > player.bankroll:
                print("You don't have enough money!")
            else:
                player.change_money(-bet)
                bet *= 2
                hand.hit(deck.draw())
                hand.eval()
        elif choice != "S":
            print("Please enter 'H', 'D' or 'S'")
        if hand.bust:
            print("You busted!")
            break
    if not hand.bust:
        while dealer.value < 17:
            dealer.hit(deck.draw())
            print("The dealer hit")
            dealer.dealer_eval()
            if dealer.bust:
                print("The dealer busted!")

    if hand.bust or (dealer.value > hand.value and not dealer.bust):
        print(f"You lose your bet of ${bet}\n\n")

    elif dealer.bust or hand.value > dealer.value:
        print(f"You win! Your bet is paid 1:1 for a total of {bet * 2}\n\n")
        player.change_money(bet * 2)

    elif hand.value == dealer.value:
        print("It's a push! Your bet is returned.\n\n")
        player.change_money(bet)


def play_game():
    print("Welcome to Benjamin's Python Blackjack!")
    print("We only deal in whole dollars, and the minimum bid is $5")
    name = input("What is your name?\n").title()
    money = input(f"Welcome to the table, {name}. How much money did you bring?\n$")
    try:
        money = int(money)
    except:
        money = 0
    while money < 5:
        money = input(f"That don't make no sense, {name}! You need at least $5. "
                      "How much do you really got?\n$")
        try:
            money = int(money)
        except:
            money = 0
    global player
    player = Player(name, money)
    play = "Y"
    while play == "Y":
        play_round()
        if player.bankroll < 5:
            print("Sorry, you don't have enough money to make a bet. Please leave the table.")
            break
        play = input(f"You have ${player.bankroll} in chips. Would you like to play again? (Y/N)\n").capitalize()
        while play != "Y" and play != "N":
            print(f"You entered '{play}'; please enter 'Y' or 'N' for a valid response.")
            play = input("Would you like to play again? (Y/N)\n").capitalize()
    print(f"Thank you for playing {player.name}. You came in with ${money} and left with ${player.bankroll}")


if __name__ == "__main__":
    play_game()
