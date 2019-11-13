board_values_dict_empty = {1:" ", 2:" ", 3:" ", 4:" ", 5:" ", 6:" ", 7:" ", 8:" ", 9:" "}

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

def print_board(array):
    for item in array:
        print(item)

def update_dict(player, key):
    # Confirm location has not already been played
    if board_values_dict[key] != " ":
        print("Invalid move! Please try again.")
        return False

    # Update dictionary with new move
    board_values_dict[key] = player.upper()

    # Check if game has been won!
    if key == 1:
        if (board_values_dict[2] == board_values_dict[3] == player.upper()) or (board_values_dict[5] == board_values_dict[9] == player.upper()) or (board_values_dict[4] == board_values_dict[7] == player.upper()):
            game_over(player)
    elif key == 2:
        if (board_values_dict[1] == board_values_dict[3] == player.upper()) or (board_values_dict[5] == board_values_dict[8] == player.upper()):
            game_over(player)
    elif key == 3:
        if (board_values_dict[1] == board_values_dict[2] == player.upper()) or (board_values_dict[5] == board_values_dict[7] == player.upper()) or (board_values_dict[6] == board_values_dict[9] == player.upper()):
            game_over(player)
    elif key == 4:
        if (board_values_dict[1] == board_values_dict[7] == player.upper()) or (board_values_dict[5] == board_values_dict[6] == player.upper()):
            game_over(player)
    elif key == 5:
        if (board_values_dict[1] == board_values_dict[9] == player.upper()) or (board_values_dict[7] == board_values_dict[3] == player.upper()) or (board_values_dict[4] == board_values_dict[6] == player.upper()) or (board_values_dict[2] == board_values_dict[8] == player.upper()):
            game_over(player)
    elif key == 6:
        if (board_values_dict[4] == board_values_dict[5] == player.upper()) or (board_values_dict[3] == board_values_dict[9] == player.upper()):
            game_over(player)
    elif key == 7:
        if (board_values_dict[1] == board_values_dict[4] == player.upper()) or (board_values_dict[5] == board_values_dict[3] == player.upper()) or (board_values_dict[8] == board_values_dict[9] == player.upper()):
            game_over(player)
    elif key == 8:
        if (board_values_dict[7] == board_values_dict[9] == player.upper()) or (board_values_dict[2] == board_values_dict[5] == player.upper()):
            game_over(player)
    elif key == 9:
        if (board_values_dict[1] == board_values_dict[5] == player.upper()) or (board_values_dict[7] == board_values_dict[8] == player.upper()) or (board_values_dict[3] == board_values_dict[6] == player.upper()):
            game_over(player)
    else:
        pass

    # Check if board full:
    if " " not in board_values_dict.values():
        game_over()

def game_over(result="cat"):
    if result.lower() == "x" or result.lower() == "o":
        print(f"Player {result.upper()} wins!!")
    else:
        print("Sorry, Cat's game!")

    play_again = input("Press Enter to play again, or type 'end' to finish: ")
    if play_again.lower() != "end":
        pass # TODO: Recursive call on entire game
    else:
        print("Thanks for playing!")

def play_game():
    print("\nWelcome to Tic-Tac-Toe!\n")
    print("Two-players will take turns placing an X or an O on the board using numbers that correspond to different locations on the playing board:\n")
    print_board(board_layout)
    print("First player to get three-in-a-row wins!! X always goes first!\n")
    input("Press enter when ready to start!")

    board_values_dict = board_values_dict_empty.copy()
    board_values_array = ["   |   |   ",
                          f" {board_values_dict[1]} | {board_values_dict[2]} | {board_values_dict[3]} ",
                          "   |   |   ",
                          "---+---+---",
                          "   |   |   ",
                          f" {board_values_dict[4]} | {board_values_dict[5]} | {board_values_dict[6]} ",
                          "   |   |   ",
                          "---+---+---",
                          "   |   |   ",
                          f" {board_values_dict[7]} | {board_values_dict[8]} | {board_values_dict[9]} ",
                          "   |   |   "]

    player_x_turn = True

    if player_x_turn:
        move = input("Player X, select your move: ")


play_game()