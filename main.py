from window import Window
from geometry import Point, Line

def main():
    window = Window(800, 600)

    start = Point(300, 500)
    end = Point(500, 200)
    line = Line(start, end)
    window.draw_line(line, "red")

    start = Point(400, 300)
    end = Point(200, 200)
    line = Line(start, end)
    window.draw_line(line, "black")

    window.wait_for_close()

main()
