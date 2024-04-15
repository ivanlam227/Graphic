from shape import Shape

class Rectangle(Shape):
    def __init__(self, canvas, x1, y1, x2, y2, color="black", filled=False, fill_color="black"):
        super().__init__(canvas)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.color = color
        self.filled = filled
        self.fill_color = fill_color
    
    def show(self):
        if self.filled:
            self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.color, fill=self.fill_color)
        else:
            self.canvas.create_rectangle(self.x1, self.y1, self.x2, self.y2, outline=self.color)
