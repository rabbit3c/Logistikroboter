class Path():
    left = 0
    forward = 1
    right = 2

    path = []
    distance_to_target = 0
    track_points = False
    finished = False
    

    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b
        self.calculate()

    def __str__(self):
        return f"Path from {self.point_a} to {self.point_b}: {self.path}"
    
    def calculate(self):
        self.path = [self.right, self.left] #fester Wert
        self.distance_to_target = 2

    def next(self):
        if len(self.path) == 0: 
            return -1
        return self.path.pop(0)
    
    def check_path_done(self):
        if len(self.path) == 0: # if there are no more elements in the list, start to track points
            print("Tracking points...")
            self.track_points = True