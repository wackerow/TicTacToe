def print_board(array):
    print("\n")
    for item in array:
        print(item)
    print("\n")

def update_board_array(dict):
    return ["   |   |   ",
          f" {dict[1]} | {dict[2]} | {dict[3]} ",
          "   |   |   ",
          "---+---+---",
          "   |   |   ",
          f" {dict[4]} | {dict[5]} | {dict[6]} ",
          "   |   |   ",
          "---+---+---",
          "   |   |   ",
          f" {dict[7]} | {dict[8]} | {dict[9]} ",
          "   |   |   "]

def game_won(player, key, board):
    # Check if game has been won!
    if key == 1 and ((board[2] == board[3] == player) or (board[5] == board[9] == player) or (board[4] == board[7] == player)):
        return True
    elif key == 2 and ((board[1] == board[3] == player) or (board[5] == board[8] == player)):
        return True
    elif key == 3 and ((board[1] == board[2] == player) or (board[5] == board[7] == player) or (board[6] == board[9] == player)):
        return True
    elif key == 4 and ((board[1] == board[7] == player) or (board[5] == board[6] == player)):
        return True
    elif key == 5 and ((board[1] == board[9] == player) or (board[7] == board[3] == player) or (board[4] == board[6] == player) or (board[2] == board[8] == player)):
        return True
    elif key == 6 and ((board[4] == board[5] == player) or (board[3] == board[9] == player)):
        return True
    elif key == 7 and ((board[1] == board[4] == player) or (board[5] == board[3] == player) or (board[8] == board[9] == player)):
        return True
    elif key == 8 and ((board[7] == board[9] == player) or (board[2] == board[5] == player)):
        return True
    elif key == 9 and ((board[1] == board[5] == player) or (board[7] == board[8] == player) or (board[3] == board[6] == player)):
        return True
    else:
        return False

def board_full(board):
    # Check if board full:
    return " " not in board.values()

def game_over(winner="cat"):
    # Game over code, run after someone wins or board fills without winner
    if winner in ("X","O"):
        print(f"Player {winner.upper()} wins!!")
    else:
        print("Sorry, Cat's game!")

    # Prompt user to play again or end script
    play_again = input("Press Enter to play again, or type 'end' to finish: ")
    if play_again.lower() == "end":
        # Game officially over
        print("Thanks for playing!")
        return True
    else:
        # Game will restart
        return False

def valid_move(num, board):
    # Confirm location is valid and empty
    if num not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Must be a number between 1 - 9. Please try again.")
        return False
    elif board[int(num)] != " ":
        print("Spot already taken!! Please try again.")
        return False
    else:
        return True

def play_game():
    print("\nWelcome to Tic-Tac-Toe!\n")
    print("Two-players will take turns placing an X or an O on the board using numbers that correspond to different locations on the playing board:\n")
    # Board layout to display for player reference
    board_layout = ["   |   |   ",
                    " 1 | 2 | 3 ",
                    "   |   |   ",
                    "---+---+---",
                    "   |   |   ",
                    " 4 | 5 | 6 ",
                    "   |   |   ",
                    "---+---+---",
                    "   |   |   ",
                    " 7 | 8 | 9 ",
                    "   |   |   "]
    print_board(board_layout)
    print("First player to get three-in-a-row wins!! X always goes first!\n")
    input("Press enter when ready to start!")

    # (Re-)Initiate empty game board
    # Dictionary for empty board
    board_values_dict = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ", 8: " ", 9: " "}

    # Game board -- References board_value_dict for current game state
    board_values_array = update_board_array(board_values_dict)
    
    # Initiate game_is_over False and player_turn "X"
    game_is_over = False
    player_turn = "X"

    # Display inital playing board
    print_board(board_values_array)
    
    # Gameplay loop (While nobody has won, and board not full)
    while not game_is_over:
        # Prompt user to select where to place X/O
        user_move = input(f"Player {player_turn}, select your move: ")

        if valid_move(user_move, board_values_dict): # user_move passed as string
            user_move = int(user_move)

            # Update dictionary/array with new move
            board_values_dict[user_move] = player_turn
            board_values_array = update_board_array(board_values_dict)

            # Display updated board
            print_board(board_values_array)

            # Check for game over
            # Player won:
            if game_won(player_turn, user_move, board_values_dict):
                game_is_over = True
                winner = player_turn
            # Board if full (Cat's Game!):
            elif board_full(board_values_dict):
                game_is_over = True
                winner = "cat"

            # Otherwise, game continues
            # Swap player_turn:
            elif player_turn == "X":
                player_turn = "O"
            elif player_turn == "O":
                player_turn = "X"
        else:
            continue # continue WHILE loop without changing player_x_turn boolean

    # Game is over, declare winner, prompt for new game
    if game_over(winner):
        return # game officially over, end script
    else:
        play_game()

play_game()