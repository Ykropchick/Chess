from pattern_of_pieces_movement import *
from chess_piece import Piece, Pawn
import pygame as pg

piece_dict = {
    # black rook
    "br": lambda x, y, screen, size, board: Piece(screen, (x * size, y * size),
                                                  ("b", pg.image.load("images/rook1.png")),
                                                  pattern_of_rooks, size, board),
    # black pawn
    "bp": lambda x, y, screen, size, board: Pawn(screen, (x * size, y * size), ("b", pg.image.load("images/pawn1.png")),
                                                 pattern_of_black_pawns, size, board),
    # black knight
    "bk": lambda x, y, screen, size, board: Piece(screen, (x * size, y * size),
                                                  ("b", pg.image.load("images/knight1.png")),
                                                  pattern_of_knight, size, board),
    # black bishop
    "bb": lambda x, y, screen, size, board: Piece(screen, (x * size, y * size),
                                                  ("b", pg.image.load("images/bishop1.png")),
                                                  pattern_of_bishop, size, board),
    # black queen
    "bq": lambda x, y, screen, size, board: Piece(screen, (x * size, y * size),
                                                  ("b", pg.image.load("images/queen1.png")),
                                                  pattern_of_queen, size, board),
    # black king
    "bK": lambda x, y, screen, size, board: Piece(screen, (x * size, y * size),
                                                  ("b", pg.image.load("images/king1.png")),
                                                  pattern_of_king, size, board),
    # white rook
    "wr": lambda x, y, screen, size, board: Piece(screen, (x * size, y * size), ("w", pg.image.load("images/rook.png")),
                                                  pattern_of_rooks, size, board),
    # white pawn
    "wp": lambda x, y, screen, size, board: Pawn(screen, (x * size, y * size), ("w", pg.image.load("images/pawn.png")),
                                                 pattern_of_white_pawns, size, board),
    # white knight
    "wk": lambda x, y, screen, size, board: Piece(screen, (x * size, y * size),
                                                  ("w", pg.image.load("images/knight.png")),
                                                  pattern_of_knight, size, board),
    # white bishop
    "wb": lambda x, y, screen, size, board: Piece(screen, (x * size, y * size),
                                                  ("w", pg.image.load("images/bishop.png")),
                                                  pattern_of_bishop, size, board),
    # white queen
    "wq": lambda x, y, screen, size, board: Piece(screen, (x * size, y * size),
                                                  ("w", pg.image.load("images/queen.png")),
                                                  pattern_of_queen, size, board),
    # white king
    "wK": lambda x, y, screen, size, board: Piece(screen, (x * size, y * size), ("w", pg.image.load("images/king.png")),
                                                  pattern_of_king, size, board),
}
