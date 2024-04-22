from geometry import Point, Line


class Cell:

    def __init__(self, x1, y1, x2, y2, window):
        self.left_wall = True
        self.right_wall = True
        self.top_wall = True
        self.bottom_wall = True
        self.__x1 = x1
        self.__x2 = x2
        self.__y1 = y1
        self.__y2 = y2
        self.__window = window

    def draw(self):
        top_left = Point(self.__x1, self.__y1)
        top_right = Point(self.__x2, self.__y1)
        bottom_left = Point(self.__x1, self.__y2)
        bottom_right = Point(self.__x2, self.__y2)
        

        if self.left_wall:
            line = Line(bottom_left, top_left)
            self.__window.draw_line(line, "black")
        if self.right_wall:
            line = Line(bottom_right, top_right)
            self.__window.draw_line(line, "black")
        if self.top_wall:
            line = Line(top_left, top_right)
            self.__window.draw_line(line, "black")
        if self.bottom_wall:
            line = Line(bottom_left, bottom_right)
            self.__window.draw_line(line, "black")
        
