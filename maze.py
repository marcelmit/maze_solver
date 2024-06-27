from tkinter import Tk, BOTH, Canvas
import time

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
        
class Cell:
    def __init__(self, _x1, _y1, _x2, _y2, _win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = _x1
        self._x2 = _x2
        self._y1 = _y1
        self._y2 = _y2
        self._win = _win

    def draw(self):
        if not self._win:
            return
        if self.has_left_wall:
            self._win.canvas.create_line(self._x1, self._y1, self._x1, self._y2)
        if self.has_right_wall:
            self._win.canvas.create_line(self._x2, self._y1, self._x2, self._y2)
        if self.has_top_wall:
            self._win.canvas.create_line(self._x1, self._y1, self._x2, self._y1)
        if self.has_bottom_wall:
            self._win.canvas.create_line(self._x1, self._y2, self._x2, self._y2)

    def draw_move(self, to_cell, undo=False):
        # Calculate the center of the current cell
        from_x = (self._x1 + self._x2) // 2
        from_y = (self._y1 + self._y2) // 2
        # Calculate the center of the target cell
        to_x = (to_cell._x1 + to_cell._x2) // 2
        to_y = (to_cell._y1 + to_cell._y2) // 2  
        # Choose the color based on the undo flag
        color = "gray" if undo else "red"
        # Draw the line on the canvas
        self._win.canvas.create_line(from_x, from_y, to_x, to_y, fill=color, width=2)

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        self._create_cells()

    def _create_cells(self):
        for row in range(self._num_rows):
            cell_row = []
            for col in range(self._num_cols):
                x1 = self._x1 + col * self._cell_size_x
                y1 = self._y1 + row * self._cell_size_y
                x2 = x1 + self._cell_size_x
                y2 = y1 + self._cell_size_y
                cell = Cell(x1, y1, x2, y2)
                cell_row.append(cell)
            self._cells.append(cell_row)
        # Draw each cell
        for col in range(self._num_cols):
            for row in range(self._num_rows):
                self._draw_cell(row, col)

    def _draw_cell(self, i, j):
        # Calculate the cell's position based on the row (i) and column (j)
        x1 = self._x1 + j * self._cell_size_x
        y1 = self._y1 + i * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y  
        # Update the cell's coordinates
        cell = self._cells[i][j]
        cell._x1 = x1
        cell._y1 = y1
        cell._x2 = x2
        cell._y2 = y2  
        # Draw the cell
        cell.draw()  
        # Call the _animate method (assuming it exists)
        self._animate()

    def _animate(self):
        if self._win:
        # Call the window's redraw method
            self._win.redraw()  
            # Sleep for 0.05 seconds to visualize the algorithm's progress
            time.sleep(0.05)


def main():
    win = Window(800, 600)
    # Create Cells
    cell1 = Cell(50, 50, 100, 100, win)
    cell2 = Cell(110, 50, 160, 100, win)
    cell3 = Cell(50, 110, 100, 160, win)
    cell4 = Cell(110, 110, 160, 160, win)
    # Draw Cells
    cell1.draw()
    cell2.draw()
    cell3.draw()
    cell4.draw()
    # Create Points
    #point1 = Point(10, 10)
    #point2 = Point(100, 100)
    #point3 = Point(50, 150)
    # Create Lines
    #line1 = Line(point1, point2)
    #line2 = Line(point3, point1) 
    # Draw Lines
    #win.draw_line(line1, "black")
    #win.draw_line(line2, "red")
    win.wait_for_close()


if __name__ == "__main__":
    main()