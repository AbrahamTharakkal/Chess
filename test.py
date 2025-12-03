import chess
board = chess.Board()
# Making moves using Standard Algebraic Notation (SAN)
board.push_san("e4")
board.push_san("e5")
board.push_san("Nf3")
board.push_san("h5")
board.push_san("Bc4")
board.push_san("c6")
move = chess.Move.from_uci("e1g1")
if move in board.legal_moves:
    board.push(move)
print(board)
print("Checkmate:", board.is_checkmate())