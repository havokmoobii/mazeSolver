class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def draw(self, canvas, fill_color):
        canvas.create_line(self.a.x, self.a.y, self.b.x, self.b.y, fill=fill_color, width=2)

class Cell:
    def __init__(self, window=None):
        self._has_left_wall = True
        self._has_right_wall = True
        self._has_top_wall = True
        self._has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window
        self._visited = False

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.__win is not None:
            if self._has_left_wall:
                self.__win.draw(Line(Point(x1, y1), Point(x1, y2)), "blue")
            else:
                self.__win.draw(Line(Point(x1, y1), Point(x1, y2)), "white")
            if self._has_right_wall:
                self.__win.draw(Line(Point(x2, y1), Point(x2, y2)), "blue")
            else:
                self.__win.draw(Line(Point(x2, y1), Point(x2, y2)), "white")
            if self._has_top_wall:
                self.__win.draw(Line(Point(x1, y1), Point(x2, y1)), "blue")
            else:
                self.__win.draw(Line(Point(x1, y1), Point(x2, y1)), "white")
            if self._has_bottom_wall:
                self.__win.draw(Line(Point(x1, y2), Point(x2, y2)), "blue")
            else:
                self.__win.draw(Line(Point(x1, y2), Point(x2, y2)), "white")

    def center_x(self):
        return self.__x1 + (self.__x2 - self.__x1) / 2
    
    def center_y(self):
        return self.__y1 + (self.__y2 - self.__y1) / 2
    
    def has_window(self):
        return self.__win is not None

    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        if self.__win is not None and to_cell.has_window():
            self.__win.draw(Line(Point(self.center_x(), self.center_y()), Point(to_cell.center_x(), to_cell.center_y())), color)