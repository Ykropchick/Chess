import pygame as pg
from chess_piece import Piece
from pprint import PrettyPrinter
from pattern_of_pieces_movement import *
from Piece_dict import piece_dict
from color import Color
pp = PrettyPrinter()

class Main:
    def __init__(self):
        pg.init()
        # The board settings
        self.Height, self.Width = 600, 600
        self.screen = pg.display.set_mode((self.Height, self.Width))
        self.Row = 8
        self.Col = 8
        self.size = (self.Height // self.Row) - 8
        self.size_empty_space = (self.Height - self.size * 8)
        # the matrix board
        self.board = [[' ' for i in range(self.Row)] for j in range(self.Col)]

        # The fonts of side symbols
        self.digits = pg.font.Font(None, 32)
        self.letters = pg.font.Font(None, 32)

        # the mainloop
        self.running = True

        # whose is turn
        self.turn = Color()

        # the type of pieces that clicked
        self.clicked_piece = " "

        # check if the player clicked on pieces
        self.is_red = False

        # the red square is a square that the piece can move
        self.red_square = []

    def draw_pieces(self):
        for x, lst in enumerate(self.board):
            for y, value in enumerate(lst):
                if value[0] != " ":
                    piece = piece_dict[value](x, y, self.screen, self.size, self.board)
                    piece.draw()

    def reset_board(self):
        self.board = [[' ' for i in range(self.Row)] for j in range(self.Col)]
        # Do the board to the beginning condition
        # pawns
        for i in range(self.Row):
            self.board[i][1] = "bp"
            self.board[i][self.Row - 2] = "wp"

        # rooks
        self.board[self.Row - 1][0], self.board[0][0] = "br", "br"
        self.board[self.Row - 1][self.Row - 1], self.board[0][self.Row - 1] = "wr", "wr"

        # knights
        self.board[self.Row - 2][0], self.board[1][0] = "bk", "bk"
        self.board[self.Row - 2][self.Row - 1], self.board[1][self.Row - 1] = "wk", "wk"

        # bishop
        self.board[self.Row - 3][0], self.board[2][0] = "bb", "bb"
        self.board[self.Row - 3][self.Row - 1], self.board[2][self.Row - 1] = "wb", "wb"

        # queen
        self.board[3][0] = "bq"
        self.board[3][self.Row - 1] = "wq"
        # king

        self.board[4][0] = "bK"
        self.board[4][self.Row - 1] = "wK"

    def do_markup(self):
        list_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for i in range(self.Row):
            # the digits
            digit_obj = self.digits.render(f'{i + 1}', True, "black")
            self.screen.blit(digit_obj, (self.Width - self.size_empty_space + 10, i * self.size_empty_space + 25))
            # The letters
            letters_obj = self.letters.render(list_letters[i], True, "black")
            self.screen.blit(letters_obj, (i * self.size_empty_space + 30, self.Height - self.size_empty_space + 10))

    def draw_square(self, color, pos):
        # Draw the board squares
        pg.draw.rect(self.screen, color, (*pos, self.size, self.size))
        pg.draw.rect(self.screen, "black", (*pos, self.size, self.size), 2)

    def draw_board(self):
        # Draw the board
        for i in range(self.Row):
            y = self.size * i
            for j in range(self.Col):
                x = self.size * j
                if j & 1:
                    if i & 1:
                        self.draw_square("gray", (x, y))
                    else:
                        self.draw_square("white", (x, y))
                else:
                    if i & 1:
                        self.draw_square("white", (x, y))
                    else:
                        self.draw_square("gray", (x, y))
        # Draw the red square
        for i in range(1, len(self.red_square)):
            pg.draw.rect(self.screen, "red", (*self.red_square[i], self.size, self.size), 5)

    def find_the_red_square(self):
        # Find the square that we need to red
        self.red_square = []
        pos = pg.mouse.get_pos()
        x = pos[0] // self.size
        y = pos[1] // self.size
        if self.board[x][y] != " ":
            piece = piece_dict[self.board[x][y]](x, y, self.screen, self.size, self.board)
            self.red_square = piece.is_clicked()
            self.clicked_piece = self.board[x][y]
            self.is_red = True

    def check_is_move(self):
        pos = pg.mouse.get_pos()
        x = pos[0] // self.size
        y = pos[1] // self.size
        # is our click in pattern_of_movement_of_this piece
        if (x, y) in [(i[0] // self.size, i[1] // self.size) for i in self.red_square]:
            self.board[self.red_square[0][0]][self.red_square[0][1]] = " "
            self.board[x][y] = self.clicked_piece
            self.red_square = []
            self.is_red = False
            self.turn.swap()
        else:
            self.red_square = []
            self.is_red = False

    def check_the_lost(self):
        white_king = any("wK" in i for i in self.board)
        black_king = any("bK" in i for i in self.board)
        font = pg.font.Font(None, 50)
        if not white_king:
            text = font.render("The White lost", True, "red")
            self.screen.blit(text, (self.Width // 2, self.Height // 2))
            pg.time.delay(5000)
            self.reset_board()
        if not black_king:
            text = font.render("The Black lost", True, "red")
            self.screen.blit(text, (self.Width // 2, self.Height // 2))
            pg.time.delay(5000)
            self.reset_board()

    def mainloop(self):
        self.reset_board()
        while self.running:
            self.screen.fill("white")
            self.draw_board()
            self.do_markup()
            self.draw_pieces()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False
                if event.type == pg.MOUSEBUTTONDOWN:
                    # pp.pprint(self.board)
                    self.check_the_lost()
                    pos = pg.mouse.get_pos()
                    x = pos[0] // self.size
                    y = pos[1] // self.size
                    try:
                        if self.is_red:
                            self.check_is_move()
                        elif self.board[x][y][0] == self.turn.get():
                            self.find_the_red_square()
                        else:
                            self.red_square = []
                            self.is_red = False
                    except:
                        self.red_square = []
                        self.is_red = False
            pg.display.update()


Main().mainloop()
