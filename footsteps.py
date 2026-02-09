"""
FOOTSTEPS GAME
--------------
A two-player bidding game inspired by classic programming puzzles.

Players secretly bid points each round to move a shared token
toward their side of the board. The player closest to the token
at the end of the game wins.
"""

# =========================
# CONSTANTS
# =========================
BOARD_SIZE = 9              # Total number of board spaces
START_POSITION = BOARD_SIZE // 2
STARTING_POINTS = 50


# =========================
# DISPLAY FUNCTIONS
# =========================
def clear_screen():
    """Prints blank lines to visually clear the console."""
    print("\n" * 50)

#code

def show_start_screen():
    """Displays the home/start screen with rules and credits."""
    clear_screen()
    print("===================================")
    print("           FOOTSTEPS")
    print("===================================\n")

    print("GAME DESCRIPTION:")
    print("Two players sit at opposite ends of a row.")
    print("A token starts in the center of the board.\n")

    print("HOW TO PLAY:")
    print("- Each player starts with 50 points")
    print("- Every round, both players secretly bid points")
    print("- The higher bid moves the token one space toward that player")
    print("- BOTH players lose the points they bid")
    print("- If bids are equal, the token does not move")
    print("- If a player runs out of points, the other may continue bidding")
    print("- The game ends when both players have no points")
    print("  or when the token reaches the end of the board\n")

    print("WINNING:")
    print("- The player closest to the token at the end wins")
    print("- Equal distance results in a draw\n")

    print("CREDITS:")
    print("Inspired by classic programming and game theory puzzles\n")

    input("Press ENTER to start the game...")


def display_board(token_position):
    """Displays the board and the token location."""
    board = ["." for _ in range(BOARD_SIZE)]
    board[token_position] = "X"

    print("\nA | " + " ".join(board) + " | B\n")


# =========================
# INPUT FUNCTIONS
# =========================
def get_bid(player_name, remaining_points):
    """
    Prompts a player to enter a valid bid.

    Parameters:
        player_name (str): Name of the player
        remaining_points (int): Points the player has left

    Returns:
        int: Valid bid amount
    """
    if remaining_points == 0:
        print(f"{player_name} has no points left and bids 0.")
        return 0

    while True:
        try:
            bid = int(input(f"{player_name}, enter your bid (0–{remaining_points}): "))
            if 0 <= bid <= remaining_points:
                return bid
            else:
                print("Invalid bid. Try again.")
        except ValueError:
            print("Please enter a valid number.")


# =========================
# GAME LOGIC
# =========================
def play_game():
    """Main game loop."""
    token_position = START_POSITION
    points_a = STARTING_POINTS
    points_b = STARTING_POINTS

    while True:
        clear_screen()
        display_board(token_position)
        print(f"Points — Player A: {points_a} | Player B: {points_b}\n")

        # End condition: both players out of points
        if points_a == 0 and points_b == 0:
            break

        bid_a = get_bid("Player A", points_a)
        bid_b = get_bid("Player B", points_b)

        points_a -= bid_a
        points_b -= bid_b

        # Determine movement
        if bid_a > bid_b:
            token_position -= 1
        elif bid_b > bid_a:
            token_position += 1

        # End condition: token reaches either end
        if token_position == 0 or token_position == BOARD_SIZE - 1:
            break

    show_end_screen(token_position, points_a, points_b)


def show_end_screen(token_position, points_a, points_b):
    """Displays the final results screen."""
    clear_screen()
    print("===================================")
    print("            GAME OVER")
    print("===================================\n")

    display_board(token_position)
    print(f"Final Points — Player A: {points_a} | Player B: {points_b}\n")

    if token_position < START_POSITION:
        print("🏆 Player A wins!")
    elif token_position > START_POSITION:
        print("🏆 Player B wins!")
    else:
        print("🤝 The game is a draw (half victory).")

    print("\nThank you for playing Footsteps!")


# =========================
# PROGRAM ENTRY POINT
# =========================
if __name__ == "__main__":
    show_start_screen()
    play_game()
