# Each square will hold a character represnting a chess piece 
# Pawns are P
#Rooks are R
#Knights are N
#Bishops are B
#Queens are Q
#Kings are K
#. is an empty square 
#uppercase letters are white lowercase are black 

#This is the board 
board = [
    list("rnbqkbnr"),
    list("pppppppp"),
    list("........"),
    list("........"),
    list("........"),
    list("........"),
    list("PPPPPPPP"),
    list("RNBQKBNR")
]


# Display the chessboard.
def display_board():
    print("\n  a b c d e f g h")

    for row in range(8):
        print(8 - row, end=" ")

        for col in range(8):
            print(board[row][col], end=" ")

        print(8 - row)

    print("  a b c d e f g h\n")


# Convert chess notation, such as e2, into row and column numbers.
def convert_square(square):
    col = ord(square[0]) - ord("a")
    row = 8 - int(square[1])

    return row, col


# Check whether the squares between two positions are empty.
def path_is_clear(sr, sc, tr, tc):
    row_step = (tr > sr) - (tr < sr)
    col_step = (tc > sc) - (tc < sc)

    row = sr + row_step
    col = sc + col_step

    while (row, col) != (tr, tc):
        if board[row][col] != ".":
            return False

        row += row_step
        col += col_step

    return True


# Check whether a piece can legally move according to
# its movement pattern and the current board occupancy.
def valid_move(sr, sc, tr, tc):
    piece = board[sr][sc]
    target = board[tr][tc]

    # Cannot move to the same square.
    if sr == tr and sc == tc:
        return False

    # Cannot capture your own piece.
    if target != ".":
        if piece.isupper() == target.isupper():
            return False

    row_diff = tr - sr
    col_diff = tc - sc

    piece_type = piece.upper()

    # PAWN
    if piece_type == "P":
        direction = -1 if piece.isupper() else 1
        start_row = 6 if piece.isupper() else 1

        # Move forward one square.
        if col_diff == 0 and row_diff == direction:
            return target == "."

        # Move forward two squares from the starting row.
        if col_diff == 0 and sr == start_row:
            if row_diff == 2 * direction and target == ".":
                middle_row = sr + direction
                return board[middle_row][sc] == "."

        # Capture diagonally.
        if abs(col_diff) == 1 and row_diff == direction:
            return (
                target != "."
                and piece.isupper() != target.isupper()
            )

        return False

    # ROOK: horizontal or vertical movement.
    if piece_type == "R":
        straight = row_diff == 0 or col_diff == 0

        return (
            straight
            and path_is_clear(sr, sc, tr, tc)
        )

    # KNIGHT: two squares in one direction,
    # then one square perpendicular to that direction.
    if piece_type == "N":
        return sorted(
            [abs(row_diff), abs(col_diff)]
        ) == [1, 2]

    # BISHOP: diagonal movement.
    if piece_type == "B":
        diagonal = abs(row_diff) == abs(col_diff)

        return (
            diagonal
            and path_is_clear(sr, sc, tr, tc)
        )

    # QUEEN: horizontal, vertical, or diagonal movement.
    if piece_type == "Q":
        straight = row_diff == 0 or col_diff == 0
        diagonal = abs(row_diff) == abs(col_diff)

        return (
            (straight or diagonal)
            and path_is_clear(sr, sc, tr, tc)
        )

    # KING: one square in any direction.
    if piece_type == "K":
        return max(
            abs(row_diff), abs(col_diff)
        ) == 1

    return False


# Select and move a piece.
def move_piece(start, end, player):
    sr, sc = convert_square(start)
    tr, tc = convert_square(end)

    piece = board[sr][sc]

    # Check that a piece exists on the starting square.
    if piece == ".":
        print("Illegal move: no piece on that square.")
        return False

    # Check that the piece belongs to the current player.
    if player == "white" and piece.islower():
        print("Illegal move: select a White piece.")
        return False

    if player == "black" and piece.isupper():
        print("Illegal move: select a Black piece.")
        return False

    # Validate the movement.
    if not valid_move(sr, sc, tr, tc):
        print("Illegal move: that piece cannot move there.")
        return False

    # Capture an opponent's piece if the destination is occupied.
    if board[tr][tc] != ".":
        print("Capture! The piece", board[tr][tc], "was removed.")

    # Update the board only after the move is approved.
    board[tr][tc] = piece
    board[sr][sc] = "."

    print("Move successful!")
    display_board()

    return True


# Main game loop.
def play_game():
    current_player = "white"

    display_board()

    while True:
        print("Current player:", current_player.capitalize())

        move = input(
            "Enter your move (example: e2 e4), "
            "or type quit: "
        ).strip().lower()

        if move == "quit":
            print("Game ended.")
            break

        parts = move.split()

        # Require a starting square and destination.
        if len(parts) != 2:
            print("Invalid input. Enter a move like e2 e4.")
            continue

        start, end = parts

        # Validate chess square notation.
        if (
            len(start) != 2
            or len(end) != 2
            or start[0] not in "abcdefgh"
            or end[0] not in "abcdefgh"
            or start[1] not in "12345678"
            or end[1] not in "12345678"
        ):
            print("Invalid square. Use squares a1 through h8.")
            continue

        # Execute the move.
        # Switch turns only when the move succeeds.
        if move_piece(start, end, current_player):
            if current_player == "white":
                current_player = "black"
            else:
                current_player = "white"


# Start the game.
if __name__ == "__main__":
    play_game()
