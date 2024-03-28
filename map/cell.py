class Cell:
    start = False
    target = False
    lane = False
    path = False
    intersection = False


    def __init__(self, cell_state):
        self.lane = cell_state == 1
        self.g = float('inf')  # Cost from start to this cell
        self.h = 0  # Estimated cost from this cell to destination
        self.parent = (0, 0)


    def set_start(self):
        self.start = True


    def set_target(self):
        self.target = True


    def set_path(self):
        self.path = True


    def set_intersection(self):
        self.intersection = True

    
    def __str__(self):
        if self.start:
            return "🟩"
        if self.target:
            return "🟥"
        if self.path:
            return "🟦"
        if self.lane:
            return "⬜️"
        return "🟫"
    

    def f(self): # calculate f
        return self.g + self.h