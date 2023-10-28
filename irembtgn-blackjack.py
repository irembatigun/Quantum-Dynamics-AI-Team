import random

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
card_values = {'J': 10, 'Q': 10, 'K': 10, 'A': 11}

users_total_win = 0
computers_total_win = 0
balance = 1000

print("Hello, what is your name?")
name = input()


def blackjack():
  global balance
  global users_current_score
  global computers_current_score
  computer_name = "Computer"

  user_cards = random.sample(cards, 2)
  computer_cards = random.sample(cards, 2)

  users_current_score = sum(
      [card_values.get(card, card) for card in user_cards])
  computers_current_score = sum(
      [card_values.get(card, card) for card in computer_cards])

  if 'A' in user_cards and users_current_score > 21:
    users_current_score -= 10

  print("Welcome to Blackjack " + name)
  print(
      "1. Start Game \n2. Show Balance \n3. Quit Game \nPlease enter your choice:"
  )
  choice = input()
  if choice == "1":
    print("Place your bet:")
    bet = int(input())

    def win():
      global balance
      balance += bet
      print("Your balance is: " + str(balance))
      user_cards.clear()
      computer_cards.clear()
      global users_total_win
      users_total_win += 1
      print(name, " won", users_total_win, "times.")
      print("Computer won", computers_total_win, "times.")

    def lose():
      global balance
      balance -= bet
      print("Your balance is: " + str(balance))
      user_cards.clear()
      computer_cards.clear()
      global computers_total_win
      computers_total_win += 1
      print(name, " won", users_total_win, "times.")
      print("Computer won", computers_total_win, "times.")

    print(name, "'s cards:", user_cards, "current score:", users_current_score)
    print(computer_name, "'s first card:", computer_cards[0])

    def show_final_hands():
      print("Your final hand:", user_cards, "current score:",
            users_current_score)
      print("Computer's final hand:", computer_cards, "current score:",
            computers_current_score)

    while (1):
      print("Type 'y' to get another card, or 'n' to pass:")
      button = input()
      if button == "y":
        new_card = random.choice(cards)
        user_cards.append(new_card)
        users_current_score += card_values.get(new_card, new_card)
        computer_card = random.choice(cards)
        if (computers_current_score < 17):
          computer_cards.append(computer_card)
        computers_current_score += card_values.get(computer_card,
                                                   computer_card)
        print(name, "'s cards:", user_cards, "current score:",
              users_current_score)
      elif button == "n":
        show_final_hands()

      else:
        print("Invalid button")

      if users_current_score > 21:
        show_final_hands()
        print("You went over! Computer wins!")
        lose()
        blackjack()
        break

      elif computers_current_score > 21:
        show_final_hands()
        print("Opponent went over! You win!")
        win()
        blackjack()
        break
      elif users_current_score > computers_current_score:
        show_final_hands()
        print("You win!")
        win()
        blackjack()
        break
      elif computers_current_score > users_current_score:
        show_final_hands()
        print("Computer wins!")
        lose()
        blackjack()
        break
      else:
        show_final_hands()
        print("It's a tie!")
        blackjack()

  elif choice == "2":
    print("Your balance is: " + str(balance))
    blackjack()

  elif choice == "3":
    print("Thanks for playing!")
    exit()
  else:
    print("Invalid choice")
    blackjack()


blackjack()
