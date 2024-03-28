class Cell:
    def __init__(self, cell_state):
        self.path = cell_state == 1
    
    def __str__(self):
        if self.path:
            return "⬜️"
        return "🟫"