import random

class BlackjackGame:
    def __init__(self):
        self.player_balance = 1000  
        self.player_bet = 0
        self.player_name = ""
        self.games_won = 0
        self.games_lost = 0

    def start_game(self):
        print("Welcome to Blackjack!")
        self.player_name = input("Enter your name: ")

        while True:
            print("\n1. Start Game")
            print("2. Show Balance")
            print("3. Quit")

            choice = input("Enter your choice (1/2/3): ")

            if choice == '1':
                self.play_round()
            elif choice == '2':
                self.show_balance()
            elif choice == '3':
                print("Thanks for playing! Exiting.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")

    def initialize_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        deck = [{'rank': rank, 'suit': suit} for rank in ranks for suit in suits]
        random.shuffle(deck)
        return deck

    def deal_initial_cards(self, deck):
        player_hand = [self.draw_card(deck), self.draw_card(deck)]
        dealer_hand = [self.draw_card(deck), self.draw_card(deck)]
        return player_hand, dealer_hand

    def draw_card(self, deck):
        return deck.pop()

    def calculate_hand_value(self, hand):
        values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}
        hand_value = sum([values[card['rank']] for card in hand])
        num_aces = sum(1 for card in hand if card['rank'] == 'A')

        while hand_value > 21 and num_aces:
            hand_value -= 10
            num_aces -= 1

        return hand_value

    def display_game_status(self, player_hand, dealer_hand, show_all=False):
        print(f"\n{self.player_name}'s Hand: {', '.join(card['rank'] for card in player_hand)}, current score: {self.calculate_hand_value(player_hand)}")
        print(f"Computer's first card: {dealer_hand[0]['rank']}")

    def take_bet(self):
        while True:
            try:
                bet = int(input(f"Hello {self.player_name}! Place your bet: $"))
                if 1 <= bet <= self.player_balance:
                    self.player_bet = bet
                    break
                else:
                    print("Invalid bet amount. Please enter a valid amount.")
            except ValueError:
                print("Invalid input. Please enter a valid bet amount.")

    def play_round(self):
        deck = self.initialize_deck()
        player_hand, dealer_hand = self.deal_initial_cards(deck)

        self.take_bet()

        while True:
            self.display_game_status(player_hand, dealer_hand)
            choice = input("Type 'y' to get another card, or 'n' to pass: ").lower()

            if choice == 'y':
                player_hand.append(self.draw_card(deck))
                if self.calculate_hand_value(player_hand) > 21:
                    print("Bust! You went over 21. You lose.")
                    self.player_balance -= self.player_bet
                    self.games_lost += 1
                    return
            elif choice == 'n':
                break

        while self.calculate_hand_value(dealer_hand) < 17:
            dealer_hand.append(self.draw_card(deck))

        self.display_game_status(player_hand, dealer_hand, show_all=True)
        player_value = self.calculate_hand_value(player_hand)
        dealer_value = self.calculate_hand_value(dealer_hand)

        if player_value > dealer_value or dealer_value > 21:
            print(f"Congratulations, {self.player_name}! You win.")
            self.player_balance += self.player_bet
            self.games_won += 1
        elif player_value < dealer_value:
            print(f"Sorry, {self.player_name}. You lose. Dealer wins.")
            self.player_balance -= self.player_bet
            self.games_lost += 1
        else:
            print("It's a tie. Push.")

    def show_balance(self):
        print(f"\n{self.player_name}'s Balance: {self.player_balance}")
        print("Games Won:", self.games_won)
        print("Games Lost:", self.games_lost)

if __name__ == "__main__":
    blackjack_game = BlackjackGame()
    blackjack_game.start_game()
