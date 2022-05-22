import pygame as pg


class Piece:
    def __init__(self, screen, pos, sprite, pattern_of_movement, size_of_square, board):
        pg.init()
        self.size = size_of_square
        self.screen = screen
        self.pos = pos
        self.color, self.sprite = sprite
        self.pattern = pattern_of_movement  # [ (x + 2, y + 1),
        self.board = board

    def is_clicked(self):
        pos_figure = (self.pos[0] // self.size, self.pos[1] // self.size)
        to_draw = [pos_figure]
        for i in self.pattern:
            if type(i) is list:
                # This for rooks, bishops and queens
                flag = False
                for j in i:
                    try:
                        x = pos_figure[0] + j[0]
                        y = pos_figure[1] + j[1]

                        if self.board[x][y] != " ":
                            if type(self.board[x][y]) is str and self.board[x][y][0] != self.color:
                                to_draw.append((x * self.size, y * self.size))
                            break
                        if type(self.board[x][y]) is str and self.board[x][y] == " ":
                            to_draw.append((x * self.size, y * self.size))
                    except:
                        pass
            else:
                try:
                    # This is for pawns and kings and knights
                    x = pos_figure[0] + i[0]
                    y = pos_figure[1] + i[1]
                    if type(self.board[x][y]) is str and self.board[x][y][0] != self.color:
                        to_draw.append((x * self.size, y * self.size))
                except:
                    pass
        return to_draw

    def get_class(self):
        pass

    def get_pos(self):
        return (self.pos[0] // self.size, self.pos[1] // self.size)

    def move(self, pos):
        self.pos = pos

    def draw(self):
        self.screen.blit(self.sprite, self.pos)



class Pawn(Piece):
    def is_clicked(self):
        pos_figure = (self.pos[0] // self.size, self.pos[1] // self.size)
        x, y = pos_figure
        to_draw = [pos_figure]
        if self.color == "b":
            if self.board[x][y+1] == " ":
                to_draw.append((x * self.size, (y + 1) * self.size))
            if self.board[x - 1][y + 1][0] == "w":
                to_draw.append(((x-1) * self.size, (y+1) * self.size))
            if self.board[x + 1][y + 1][0] == "w":
                to_draw.append(((x+1) * self.size, (y+1) * self.size))
            if y == 1:
                to_draw.append((x * self.size, (y + 2) * self.size))
        else:
            if self.board[x][y - 1] == " ":
                to_draw.append((x * self.size, (y - 1) * self.size))
            if self.board[x + 1][y - 1][0] == "b":
                print(1)
                to_draw.append(((x+1) * self.size, (y-1) * self.size))
            if self.board[x - 1][y - 1][0] == "b":
                print(2)
                to_draw.append(((x-1) * self.size, (y-1) * self.size))
            if y == 6:
                to_draw.append((x * self.size, (y - 2) * self.size))
        return to_draw

