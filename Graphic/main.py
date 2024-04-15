import tkinter as tk
from canvas import Canvas
from rectangle import Rectangle
from point import Point

def main():
    root = tk.Tk()
    canvas = Canvas(root)
    canvas.pack()
    
 
    canvas.add_shape(Rectangle(canvas, 10, 10, 100, 100, "red", True, "yellow"))
    canvas.add_shape(Rectangle(canvas, 150, 100, 200, 250, "blue", True, "green"))
    canvas.add_shape(Rectangle(canvas, 10, 100, 200, 150, "orange"))
    canvas.add_shape(Point(canvas, 250, 50))
    canvas.add_shape(Point(canvas, 200, 50, "magenta"))
    

    canvas.show_shapes_with_delay(1000) 
    
    root.mainloop()

if __name__ == "__main__":
    main()
