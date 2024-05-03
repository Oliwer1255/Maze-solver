import time
import random
import sys
from cell import Cell

class Maze:

    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            cell_size_x,
            cell_size_y,
            window=None,
            seed=None,
        ):
        self.cells = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
        if seed != None:
            random.seed(seed)
        self.__window = window

        self.__create_cells()

    def __create_cells(self):

        for i in range(self.__num_rows):
            cells = []
            for j in range(self.__num_cols):
                cell = Cell(
                    self.__x1 + (j + 1) * self.__cell_size_x,
                    self.__y1 + (i + 1) * self.__cell_size_y,
                    self.__x1 + (j + 1) * self.__cell_size_x + self.__cell_size_x,
                    self.__y1 + (i + 1) * self.__cell_size_y + self.__cell_size_y,
                    self.__window
                )
                cells.append(cell)

            self.cells.append(cells)

        self.__draw_cells()
        self.__break_entrance_and_exit()
        self.__break_walls_r(0, 0)
        self.__reset_cells_visited()

    def __draw_cells(self):
        for cells in self.cells:
            for cell in cells:
                cell.draw()
                self.__animate()

    def __break_entrance_and_exit(self):
        self.cells[0][0].top_wall = False
        self.cells[0][0].draw()
        self.cells[-1][-1].bottom_wall = False
        self.cells[-1][-1].draw()

    def __animate(self):
        if self.__window == None:
            return
         
        self.__window.redraw()
        time.sleep(0.05)

    def __break_walls_r(self, i, j):
        self.__animate()
        self.cells[j][i].visited = True
        while True:
            to_visit = []
            
            if i - 1 >= 0:
                if not self.cells[j][i - 1].visited:
                    to_visit.append([i - 1, j, "Left"])
            if i + 1 < self.__num_cols:
                if not self.cells[j][i + 1].visited:
                    to_visit.append([i + 1, j, "Right"])
            if j - 1 >= 0:
                if not self.cells[j - 1][i].visited:
                    to_visit.append([i, j - 1, "Up"])
            if j + 1 < self.__num_rows:
                if not self.cells[j + 1][i].visited:
                    to_visit.append([i, j + 1, "Down"])
            
            if len(to_visit) == 0:
                self.cells[j][i].draw()
                return
            
            direction_index = random.randrange(len(to_visit))
            direction = to_visit[direction_index]

            if direction[2] == "Left":
                self.cells[j][i].left_wall = False
                self.cells[direction[1]][direction[0]].right_wall = False
            if direction[2] == "Right":
                self.cells[j][i].right_wall = False
                self.cells[direction[1]][direction[0]].left_wall = False
            if direction[2] == "Up":
                self.cells[j][i].top_wall = False
                self.cells[direction[1]][direction[0]].bottom_wall = False
            if direction[2] == "Down":
                self.cells[j][i].bottom_wall = False
                self.cells[direction[1]][direction[0]].top_wall = False

            self.__break_walls_r(direction[0], direction[1])

    def __reset_cells_visited(self):
        for list_of_cells in self.cells:
            for cell in list_of_cells:
                cell.visited = False

    def solve(self):
        return self.__solve_r(0, 0)

    def __solve_r(self, i, j):
        self.__animate()
        self.cells[j][i].visited = True
        if i == self.__num_cols - 1 and j == self.__num_rows - 1:
            return True
        
        to_visit = []

        if i - 1 >= 0:
            if not self.cells[j][i - 1].right_wall and not self.cells[j][i - 1].visited:
                to_visit.append([i - 1, j])
        if i + 1 < self.__num_cols:
            if not self.cells[j][i + 1].left_wall and not self.cells[j][i + 1].visited:
                to_visit.append([i + 1, j])
        if j - 1 >= 0:
            if not self.cells[j - 1][i].bottom_wall and not self.cells[j - 1][i].visited:
                to_visit.append([i, j - 1])
        if j + 1 < self.__num_rows:
            if not self.cells[j + 1][i].top_wall and not self.cells[j + 1][i].visited:
                to_visit.append([i, j + 1])

        current_cell = self.cells[j][i]

        for pos in to_visit:
            current_cell.draw_move(self.cells[pos[1]][pos[0]])
            if self.__solve_r(pos[0], pos[1]):
                return True
            current_cell.draw_move(self.cells[pos[1]][pos[0]], True)

        return False
        
        

