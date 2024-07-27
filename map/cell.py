class Cell:
    start = False
    target = False
    lane = False
    blocked = False
    path = False
    intersection = False


    # initialize cell
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


    def set_blocked(self):
        self.lane = False
        self.blocked = True


    def set_intersection(self):
        self.intersection = True

    
    # Custom string function to display cell (as a colorful icon)
    def __str__(self):
        if self.start:
            return "🟩"
        if self.target:
            return "🟥"
        if self.path:
            return "🟦"
        if self.lane:
            return "⬜️"
        if self.blocked:
            return "⬛️"
        return "🟫"
    

    # Calculate f
    def f(self):
        return self.g + self.h