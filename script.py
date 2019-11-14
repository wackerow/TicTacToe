def print_board(array):
    print("\n")
    for item in array:
        print(item)
    print("\n")

def valid_move(num, board):
    # Confirm location is valid and empty
    if num not in [str(x) for x in range(1,10)]:
        print("Must be a number between 1 - 9. Please try again.")
        return False
    elif board[int(num)] != " ":
        print("Spot already taken!! Please try again.")
        return False
    else:
        return True

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
    # Array of winning combinations
    winning_combos = [[1,2,3],[4,5,6],[7,8,9], # Rows
                      [1,4,7],[2,5,8],[3,6,9], # Columns
                      [1,5,9],[3,5,7]] # Diags

    # Check if game has been won!
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


def board_full(board):
    # Check if board full:
    return " " not in board.values()

def game_over(winner="cat"):
    # Game over code, run after someone wins or board fills without winner
    if winner in ("X","O"):
        print(f"Player {winner.upper()} wins!!")
    else:
        print("Sorry, cat's game!")

    # Prompt user to play again or end script
    return input("Press Enter to play again, or type 'end' to finish: ").lower() == "end"

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

            else:
                player_turn = {"X":"O", "O":"X"}[player_turn]

        else: # Move was invalid
            continue # continue WHILE loop without changing player_x_turn boolean

    # Game is over, declare winner, prompt for new game
    if game_over(winner):
        # Game officially over, end script
        print("Thanks for playing!")
    else:
        play_game()

play_game()