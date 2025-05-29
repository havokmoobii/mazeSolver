from window import Window
from maze import Maze

WINDOW_LENGTH = 800
WINDOW_WIDTH = 600
MAZE_X = 40
MAZE_Y = 40
ROWS = 26
COLS = 36
CELL_LENGTH = 20
CELL_WIDTH = 20


def main():
    win = Window(WINDOW_LENGTH, WINDOW_WIDTH)

    maze = Maze(MAZE_X, MAZE_Y, ROWS, COLS, CELL_LENGTH, CELL_WIDTH, win)
    if maze.solve():
        print("Success!")
    else:
        print("WTF")

    win.wait_for_close()

main()
