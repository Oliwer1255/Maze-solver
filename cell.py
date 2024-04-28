from geometry import Point, Line


class Cell:

    def __init__(self, x1, y1, x2, y2, window=None):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        self.__window = window
        self.visited = False

    def draw(self):
        if self.__window == None:
            return

        top_left = Point(self.x1, self.y1)
        top_right = Point(self.x2, self.y1)
        bottom_left = Point(self.x1, self.y2)
        bottom_right = Point(self.x2, self.y2)

        if self.left_wall:
            line = Line(bottom_left, top_left)
            self.__window.draw_line(line, "black")
        else:
            line = Line(bottom_left, top_left)
            self.__window.draw_line(line, "#d9d9d9")

        if self.right_wall:
            line = Line(bottom_right, top_right)
            self.__window.draw_line(line, "black")
        else:
            line = Line(bottom_right, top_right)
            self.__window.draw_line(line, "#d9d9d9")

        if self.top_wall:
            line = Line(top_left, top_right)
            self.__window.draw_line(line, "black")
        else:
            line = Line(top_left, top_right)
            self.__window.draw_line(line, "#d9d9d9")

        if self.bottom_wall:
            line = Line(bottom_left, bottom_right)
            self.__window.draw_line(line, "black")
        else:
            line = Line(bottom_left, bottom_right)
            self.__window.draw_line(line, "#d9d9d9")

    def draw_move(self, to_cell, undo=False):
        start = Point(
            self.x1 + (self.x2 - self.x1) // 2, 
            self.y1 + (self.y2 - self.y1) // 2
        )
        end = Point(
            to_cell.x1 + (to_cell.x2 - to_cell.x1) // 2, 
            to_cell.y1 + (to_cell.y2 - to_cell.y1) // 2
        )

        line = Line(start, end)

        if undo:
            self.__window.draw_line(line, "gray")
        else:
            self.__window.draw_line(line, "red")
            
        
