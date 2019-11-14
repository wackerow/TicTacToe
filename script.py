"""
Tic-Tac-Toe Python Game!
"""

def print_board(array):
    """
    :param array: Array of markers corresponding to game board
    :return: None (Prints to display current game board)
    """

    print("\n")
    print(f"{array[1]}|{array[2]}|{array[3]}")
    print("-+-+-")
    print(f"{array[4]}|{array[5]}|{array[6]}")
    print("-+-+-")
    print(f"{array[7]}|{array[8]}|{array[9]}")
    print("\n")


def valid_move(user_input, board):
    """
    :param user_input: Users input to be checked for validity
    :param board: Array of markers for current game state (before new move)
    :return: Boolean if move was valid or not
    """

    # Confirm user input is valid (1-9)
    if user_input not in [str(x) for x in range(1, 10)]:
        print("Must be a number between 1 - 9. Please try again.")
        return False
    # Confirm location is empty
    if board[int(user_input)] != " ":
        print("Spot already taken!! Please try again.")
        return False
    return True


def game_won(player, board):
    """
    :param player: "X" or "O" depending which turn
    :param board: Array of markers for current game state
    :return: Boolean if game was won or not
    """

    # Array of winning combinations
    winning_combos = [[1, 2, 3], [4, 5, 6], [7, 8, 9],  # Rows
                      [1, 4, 7], [2, 5, 8], [3, 6, 9],  # Columns
                      [1, 5, 9], [3, 5, 7]]  # Diagonals

    # Check if game has been won!
    for combo in winning_combos:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == player:
            return True
    return False


def board_full(board):
    """
    :param board: Array of markers for current game state
    :return: Boolean if board full or not (Tie game)
    """

    # Check if board full:
    return " " not in board


def game_over(winner):
    """
    :param winner: "X", "O" or "cat" depending on winner
    :return: Boolean if game to end or not (False = Replay)
    """

    # Game over code, run after someone wins or board fills without winner
    if winner in ("X", "O"):
        print(f"Player {winner.upper()} wins!!")
    else:
        print("Sorry, cat's game!")

    # Prompt user to play again or end script
    return input("Press Enter to play again, or type 'end' to finish: ").lower() == "end"


def play_game():
    """
    Tic Tac Toe game play script
    :return: None
    """
    print("\nWelcome to Tic-Tac-Toe!\n")
    print("Two-players will take turns placing an X or an O on the board \
using numbers that correspond to different locations on the playing board:\n")

    # Board layout to display for player reference
    print_board(range(10))

    print("First player to get three-in-a-row wins!! X always goes first!\n")
    input("Press enter when ready to start!")

    # Initiate empty game board array, game_is_over False and player_turn "X"
    board_array = ["0"] + [" "] * 9
    game_is_over = False
    player_turn = "X"
    winner = "cat"

    # Display initial playing board
    print_board(board_array)

    # Game play loop (While nobody has won, and board not full)
    while not game_is_over:
        # Prompt user to select where to place X/O
        user_move = input(f"Player {player_turn}, select your move: ")

        if valid_move(user_move, board_array):  # user_move passed as string
            user_move = int(user_move)

            # Update board array with new move
            board_array[user_move] = player_turn

            # Display updated board
            print_board(board_array)

            # Check for game over
            # Player won:
            if game_won(player_turn, board_array):
                game_is_over = True
                winner = player_turn
            # Board if full (Cat's Game!):
            elif board_full(board_array):
                game_is_over = True
            # Otherwise, swap player_turn and continue:
            else:
                player_turn = {"X": "O", "O": "X"}[player_turn]

        else:  # Move was invalid
            continue  # continue WHILE loop without changing player_x_turn boolean

    # Game is over, declare winner, prompt for new game
    if game_over(winner):
        # Game officially over, end script
        print("Thanks for playing!")
    else:
        play_game()


play_game()
