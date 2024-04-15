import tkinter as tk

class Canvas(tk.Canvas):
    def __init__(self, master, width=400, height=400):
        super().__init__(master, width=width, height=height)
        self.shapes = []
    
    def add_shape(self, shape):
        self.shapes.append(shape)
    
    def clear(self):
        self.delete("all")
        self.shapes = []
    
    def show_shapes_with_delay(self, delay=500):
        for i, shape in enumerate(self.shapes):
            self.after(i * delay, shape.show)
