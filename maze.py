import time
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
        ):
        self.cells = []
        self.__x1 = x1
        self.__y1 = y1
        self.__num_rows = num_rows
        self.__num_cols = num_cols
        self.__cell_size_x = cell_size_x
        self.__cell_size_y = cell_size_y
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


        
