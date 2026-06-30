board = [
    ["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
    ["BP", "BP", "BP", "BP", "BP", "BP", "BP", "BP"],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None],
    ["WP", "WP", "WP", "WP", "WP", "WP", "WP", "WP"],
    ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]
]


current_turn = "White"

while True:
    print(f"\nCurrent Turn {current_turn}")
    move = input("Enter your move : ")
    start, end = move.split()

    start_file = start[0]
    start_rank = int(start[1])
    start_col = ord(start_file) - ord("a")
    start_row = 8 - start_rank

    end_file = end[0]
    end_rank = int(end[1])
    end_col = ord(end_file) - ord("a")
    end_row = 8 - end_rank

    piece = board[start_row][start_col]

    if piece is None:
        print("NO piece in the square")
        continue
    
    if current_turn == "White" and piece[0]!= "W":
        print("It's White's turn!")
        continue
    if current_turn == "Black" and piece[0]!="B":
        print("It's Black's turn!")

    destination_piece = board[end_row][end_col]
    if destination_piece is not None:
        if destination_piece[0] == piece[0]=="W":
            print("You can't capture your own piece!")
            continue

    board[end_row][end_col] = piece
    board[start_row][start_col]=None
    print()
    for row in board:
        for square in row:
            if square is None:
                print("--", end=" ")
            else:
                print(square, end=" ")
        print()




    if current_turn == "White":
        current_turn = "Black"
    else:
        current_turn = "White"

   
      