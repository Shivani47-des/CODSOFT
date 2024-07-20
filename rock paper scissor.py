import random
def game():
    print("\n THE ROCK,PAPER,SCISSORS GAME..")
    print("CHOOSE ANY : ROCK, PAPER,SCISSOR\n")

    item=["rock","scissor","paper"]

    rand=random.choice(item)
    attempts=0
    while True:
        choice=input("ENTER YOUR CHOICE: ").lower()
        if choice=="exit":
            print("Game Ended!")
            break
        
        elif choice==rand :
            print("YOU WON!")
            print(f"YOU WON THE GAME BY GUESSING THE CORRECT OUTPUT {choice} and in {attempts+1} attempts.\n")
            play_again = input("IF YOU WANT TO PLAY AGAIN ,ENTER 'YES', ELSE TYPE 'EXIT' TO QUIT. ").lower()

            if play_again != 'YES':
                print("Thanks for playing!")
            else:
                game()
        else:
            print("TRY AGAIN")

            attempts=attempts+1


game()


