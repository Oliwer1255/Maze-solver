from window import Window
from maze import Maze

def main():
    window = Window(800, 600)

    maze = Maze(10, 10, 8, 8, 50, 50, window, 0)
    maze.solve()

    window.wait_for_close()

main()
