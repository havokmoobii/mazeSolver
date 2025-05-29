import time
import random

from enum import Enum

from graphics import Cell

ANIMATION_DELAY = 0.001

class Direction(Enum):
    Left = "left"
    Up = "up"
    Right = "right"
    Down = "down"

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            win=None,
            seed=None
        ):
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        self.__win = win

        self.__cells = []
        self.__create_cells()
        self.__break_entrance_and_exit()
        self.__break_walls(0, 0)

        if seed is not None:
            random.seed(seed)

    def __create_cells(self):
        for i in range(self.__num_cols):
            self.__cells.append([])
            for j in range(self.__num_rows):
                self.__cells[i].append(Cell(self.__win))
                self.__draw_cell(i, j)
    
    def __draw_cell(self, i, j):
        self.__cells[i][j].draw(
            self.__x1 + self.__cell_size_x * i,
            self.__y1 + self.__cell_size_y * j,
            self.__x1 + self.__cell_size_x * (i + 1),
            self.__y1 + self.__cell_size_y * (j + 1)
        )
        self.__animate()

    def __animate(self):
        if self.__win is not None:
            self.__win.redraw()
        #time.sleep(ANIMATION_DELAY)

    def __break_entrance_and_exit(self):
        if self.__num_rows == 0 or self.__num_cols == 0:
            raise Exception("Error: There is no maze.")
        self.__cells[0][0]._has_top_wall = False
        self.__draw_cell(0, 0)
        self.__cells[self.__num_cols - 1][self.__num_rows - 1]._has_bottom_wall = False
        self.__draw_cell(self.__num_cols - 1, self.__num_rows - 1)

    def __break_walls(self, i, j):
        self.__cells[i][j]._visited = True
        self.__draw_cell(i, j)
        if i == self.__num_cols and j == self.__num_rows:
            return
        neighbors = []
        if i > 0:
            neighbors.append((i-1, j, Direction.Left))
        if j > 0:
            neighbors.append((i, j-1, Direction.Up))
        if i + 1 < self.__num_cols:
            neighbors.append((i+1, j, Direction.Right))
        if j + 1 < self.__num_rows:
            neighbors.append((i, j+1, Direction.Down))
        random.shuffle(neighbors)
        for neighbor in neighbors:
            if not self.__cells[neighbor[0]][neighbor[1]]._visited:
                match(neighbor[2]):
                    case Direction.Left:
                        self.__cells[i][j]._has_left_wall = False
                        self.__cells[i-1][j]._has_right_wall = False
                    case Direction.Up:
                        self.__cells[i][j]._has_top_wall = False
                        self.__cells[i][j-1]._has_bottom_wall = False
                    case Direction.Right:
                        self.__cells[i][j]._has_right_wall = False
                        self.__cells[i+1][j]._has_left_wall = False
                    case Direction.Down:
                        self.__cells[i][j]._has_bottom_wall = False
                        self.__cells[i][j+1]._has_top_wall = False
                self.__draw_cell(i, j)
                print(f"calling break wall {neighbor[2].value} from cell {i}, {j}")
                self.__break_walls(neighbor[0], neighbor[1])




"""
class Graph:
    def depth_first_search(self, start_vertex):
        visited = []
        return self.depth_first_search_r(visited, start_vertex)

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        neighbors = sorted(self.graph[current_vertex])
        for neighbor in neighbors:
            if neighbor not in visited:
                visited = self.depth_first_search_r(visited, neighbor)
        return visited
"""
