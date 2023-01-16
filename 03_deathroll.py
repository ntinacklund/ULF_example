from random import choice, randint

def deathroll():
    print("Name of player 1")
    player_one = input(">> ").title()

    print("Name of player 2")
    player_two = input(">> ").title()
    
    
    start = int(input(f"At what integer would you like to start, {player_one}: "))
    roll = start
    winner = ""
    while True:
        roll = randint(1, roll)
        print(f"{player_one} rolled {roll}.")
        if roll == 1:
            print(f"{player_one} lost!")
            winner = player_two
            break
        input("Press Enter to continue.")
        roll = randint(1, roll)
        print(f"{player_two} rolled {roll}.")
        if roll == 1:
            print(f"{player_two} lost!")
            winner = player_one
            break
        input("Press Enter to continue.\n")
    print(f"{winner} won!")
    
    
if __name__ == "__main__":
    deathroll()