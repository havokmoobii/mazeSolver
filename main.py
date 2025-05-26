from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title = "Maze Solver"
        self.canvas = Canvas(self.__root, bg="white", width=width, height=height)
        self.canvas.pack(fill=BOTH, expand=1)
        self.running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def draw(self, line, fill_color):
        line.draw(self.canvas, fill_color)

    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()
    
    def close(self):
        self.running = False

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
    def __init__(self, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.__x1 = -1
        self.__x2 = -1
        self.__y1 = -1
        self.__y2 = -1
        self.__win = window

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        if self.has_left_wall:
            self.__win.draw(Line(Point(x1, y1), Point(x1, y2)), "blue")
        if self.has_right_wall:
            self.__win.draw(Line(Point(x2, y1), Point(x2, y2)), "blue")
        if self.has_top_wall:
            self.__win.draw(Line(Point(x1, y1), Point(x2, y1)), "blue")
        if self.has_bottom_wall:
            self.__win.draw(Line(Point(x1, y2), Point(x2, y2)), "blue")

    def center_x(self):
        return self.__x1 + (self.__x2 - self.__x1) / 2
    
    def center_y(self):
        return self.__y1 + (self.__y2 - self.__y1) / 2

    def draw_move(self, to_cell, undo=False):
        print("hi")
        color = "red"
        if undo:
            color = "gray"
        self.__win.draw(Line(Point(self.center_x(), self.center_y()), Point(to_cell.center_x(), to_cell.center_y())), color)

def main():
    win = Window(800, 600)

    cell = Cell(win)
    cell.draw(20, 20, 100, 100)
    cell2 = Cell(win)
    cell2.draw(100, 20, 180, 100)
    cell3 = Cell(win)
    cell3.draw(180, 20, 260, 100)
    cell.draw_move(cell3, undo=True)

    win.wait_for_close()

main()
