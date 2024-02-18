class Path():
    left = 0
    forward = 1
    right = 2

    path = []
    

    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b
        self.calculate()

    def __str__(self):
        return f"Path from {self.point_a} to {self.point_b}: {self.path}"
    
    def calculate(self):
        self.path = [self.right, self.left]

    def next(self):
        if len(self.path) == 0: 
            return -1
        return self.path.pop(0)