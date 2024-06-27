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

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self):
        self.running = True
        while self.running:
            self.redraw()

    def close(self):
        self.running = False
        self.root.destroy()

def main():
    win = Window(800, 600)
    win.wait_for_close()


if __name__ == "__main__":
    main()