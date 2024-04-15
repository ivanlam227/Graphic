from shape import Shape

class Point(Shape):
    def __init__(self, canvas, x, y, color="white"):
        super().__init__(canvas)
        self.x = x
        self.y = y
        self.color = color
    
    def show(self):
        self.canvas.create_rectangle(self.x, self.y, self.x+1, self.y+1, fill=self.color)
