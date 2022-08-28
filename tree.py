from chess import Board, Move, STARTING_FEN

# an adjacency list
positions = {}

# depth-first search from a FEN string
def generate_tree(fen):
    board = Board(fen)
    legal_moves = list(board.legal_moves)
    if fen in positions:
        positions[fen] += legal_moves
    else:
        positions[fen] = legal_moves

    for move in legal_moves:
        board.push(move)
        next_fen = board.fen()
        board.pop()
        generate_tree(next_fen)

try:
    generate_tree(STARTING_FEN)
except RecursionError: 
    print(len(positions) + sum(len(p) for p in positions))
