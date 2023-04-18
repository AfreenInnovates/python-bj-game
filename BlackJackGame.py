import random
active = True


def play_game():
    deck = list(range(1, 14))
    random.shuffle(deck)
    card1, card2 = random.sample(deck, 2)
    sum = card1 + card2
    global active
    while active:
        userentry = input("Enter 'yes' to play and 'q' to quit: ").lower()
        if userentry == "yes":
            print(f"Your cards are: \n{card1}\n{card2}")
            print(f"Sum of your cards is: {sum}")
            if sum == 21:
                print("You win!")
                break
            elif sum > 21:
                print("You lose!")
                break
            else:
                while sum < 21:
                    user2entry = input(
                        "Would you like to get one random card (enter 'yes') Or to quit the game (enter 'q')?: ")
                    if user2entry == "yes":
                        new_card = deck.pop()
                        sum = sum + new_card
                        print(f"Your new random card is {new_card}!")
                        print(f"Your new sum of cards is {sum}.")
                        if sum == 21:
                            print("You win!")
                            quit()
                        elif sum > 21:
                            print("You lose!")
                            print("Better luck next time :)")
                            quit()
                    elif user2entry == "q":
                        print("Goodbye! See you soon.")
                        print(
                            "If you want to play a new game, please enter the run button :)")
                        quit()
                    else:
                        print("Enter a valid option please.")
        elif userentry == "q":
            print("Goodbye!")
            print("If you want to play, please enter the run button :)")
            active = False
        else:
            print("Enter a valid option please")
            continue


play_game()
