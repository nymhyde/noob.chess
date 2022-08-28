#!/usr/bin/python3

# command line interface #
# ---------------------- #


import chess
import argparse



def start():
    '''
    Start the command line ui
    '''

    board = chess.Board()
    player = (chess.WHITE if input("Start as [W]hite or [B]lack :: \n") == "W"  else chess.BLACK)
    user = 'WHITE' if player == chess.WHITE else 'BLACK'
    print(f'You have to selected to play as {user}')

    print(render(board, player))

    if player == chess.WHITE:
        board.push(get_move(board))

    while not board.is_game_over():
        print(render(board, player))
        board.push(get_move(board))

    print(f' \n\n Result :: [W] {board.result()} [B] :: ')


def render(board, player):
    '''
    Print chess board with special chess characters depending upon which side player plays from
    '''

    board_string = list(str(board))
    uni_pieces = {
        "r": "♖",
        "n": "♘",
        "b": "♗",
        "q": "♕",
        "k": "♔",
        "p": "♙",
        "R": "♜",
        "N": "♞",
        "B": "♝",
        "Q": "♛",
        "K": "♚",
        "P": "♟",
        ".": "·",
    }

    for idx, char in enumerate(board_string):
        if char in uni_pieces:
            board_string[idx] = uni_pieces[char]
    ranks = ["1", "2", "3", "4", "5", "6", "7", "8"]
    display = []
    for rank in "".join(board_string).split('\n'):
        display.append(f'{ranks.pop()} {rank}')
    if player == chess.BLACK:
        display.reverse()
    display.append("  a b c d e f g h")

    return "\n" + "\n".join(display)



def get_move(board):
    '''
    Try (and keep trying) to get a legal next move from the user.
    Play the move by mutating the game board
    '''
    move = input(f'\n Your move(e.g. {list(board.legal_moves)[0]}) :: \n')

    for legal_move in board.legal_moves:
        if move == str(legal_move):
            return legal_move

    return get_move(board)



def get_depth():
    parser = argparser.ArgumentParser()
    parser.add_argument("--depth", default=5, help='provide an integer for depth')
    args = parser.parse_args()
    return max([1, int(args.depth)])



# main 
if  __name__ == "__main__":
    start()


