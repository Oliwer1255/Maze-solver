from window import Window
from geometry import Point, Line
from cell import Cell

def main():
    window = Window(800, 600)

    cell1 = Cell(150, 150, 200, 200, window)
    cell1.right_wall = False
    cell1.draw()

    cell2 = Cell(200, 150, 250, 200, window)
    cell2.left_wall = False
    cell2.draw()

    cell1.draw_move(cell2)

    window.wait_for_close()

main()
