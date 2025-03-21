import random
import time
import os


def setup_cards():
    cards = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    cards = cards + cards  
    random.shuffle(cards) 
    return cards


def display_board(board, revealed, size):
    os.system('cls' if os.name == 'nt' else 'clear')  
    print("Memory Puzzle Game")
    print(f"Time Remaining: {time_left} seconds")
    print("\n")


    for i in range(size):
        for j in range(size):
            idx = i * size + j
            if revealed[idx]:
                print(f"[{board[idx]}]", end=" ")
            else:
                print("[*]", end=" ")
        print()


def check_win(revealed, size):
    return all(revealed)

# The main game loop
def play_game():
    global time_left
    size = 4 
    board = setup_cards()  
    revealed = [False] * 16  
    moves = 0  

    
    time_left = 60  
    start_time = time.time()

    
    while time_left > 0:
        display_board(board, revealed, size)

        if check_win(revealed, size):
            print(f"\nCongratulations! You won in {moves} moves.")
            break

        print(f"\nChoose two cards to flip (1-16):")


        try:
            first_choice = int(input("Enter the number (1-16) of the first card to flip: ")) - 1
            if first_choice < 0 or first_choice >= 16 or revealed[first_choice]:
                print("Invalid choice or card already revealed. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 16.")
            continue

        
        try:
            second_choice = int(input("Enter the number (1-16) of the second card to flip: ")) - 1
            if second_choice < 0 or second_choice >= 16 or revealed[second_choice] or second_choice == first_choice:
                print("Invalid choice or card already revealed. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 16.")
            continue

        
        revealed[first_choice] = True
        revealed[second_choice] = True
        display_board(board, revealed, size)

        
        if board[first_choice] == board[second_choice]:
            print(f"Match found: {board[first_choice]}!")
        else:
            print(f"No match: {board[first_choice]} vs {board[second_choice]}")
            time.sleep(1)
            revealed[first_choice] = False
            revealed[second_choice] = False

        moves += 1

        
        time_left = 60 - int(time.time() - start_time)

        if time_left <= 0:
            display_board(board, revealed, size)
            print("\nTime's up! You lost.")
            break


if __name__ == "__main__":
    play_game()
