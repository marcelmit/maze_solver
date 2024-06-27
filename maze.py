from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, length):
        self.width = width
        self.length = length
        self.root = Tk()
        self.root.title
        self.canvas = Canvas(self.root, width=self.width, height=self.length)
        self.canvas.pack(fill=BOTH, expand=True)
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False

    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
     self.x = x
     self.y = y

class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def draw(self, canvas, fill_color):
        canvas.create_line(
            self.start_point.x, self.start_point.y,
            self.end_point.x, self.end_point.y,
            fill=fill_color, width=2
)


def main():
    win = Window(800, 600)
    # Create Points
    point1 = Point(10, 10)
    point2 = Point(100, 100)
    point3 = Point(50, 150)
    # Create Lines
    line1 = Line(point1, point2)
    line2 = Line(point3, point1)  
    # Draw Lines
    win.draw_line(line1, "black")
    win.draw_line(line2, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()