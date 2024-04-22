from window import Window
from geometry import Point, Line
from cell import Cell

def main():
    window = Window(800, 600)

    cell = Cell(150, 150, 200, 200, window)
    cell.right_wall = False
    cell.draw()

    cell = Cell(100, 100, 150, 150, window)
    cell.bottom_wall = False
    cell.draw()

    cell = Cell(350, 350, 400, 400, window)
    cell.top_wall = False
    cell.left_wall = False
    cell.draw()

    window.wait_for_close()

main()
