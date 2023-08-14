import random

choose=['ROCK','PAPER','SCISSOR']

def game():
    print('\n\nx-x-x-x-x-x-x-WElCOME TO THE GAME: ROCK, PAPER AND SCISSOR-x-x-x-x-x-x-x')
    won=0

    rounds=int(input("Enter number of rounds: "))
    for i in range(rounds):
        comp= random.choice(choose)
        
        player=input('\nEnter your choice: ').upper()
        print("Computer choice:" + comp)
        if (player=="PAPER" and comp=="ROCK") or\
            (player=="ROCK" and comp=="SCISSOR") or\
            (player=="SCISSOR" and comp=="PAPER"):
            print("-------YOU WON!!!!-------")
            won += 1
        elif (comp=="PAPER" and player=="ROCK") or\
            (comp=="ROCK" and player=="SCISSOR") or\
            (comp=="SCISSOR" and player=="PAPER"):
            print("-------YOU LOSE!!!!-------")

        elif player== comp:
            print("-------TIE-------")

        else:
            print("INVALID ENTRY...")

    print("\nGames wons by player: ", won)   
    
    play_again=input("\nWanna play again? (y/n): ").lower()
    if (play_again == 'y'):
        print("y")
        game()
    elif (play_again== 'n'):
        exit('\nx-x-x-x-x-x-x-Thank you for playing!-x-x-x-x-x-x-x')
    else:
        print("Error: Invalid choice.")

game()   