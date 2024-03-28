import json
from cell import Cell

class Map:
    map = []

    def __init__(self):
        grid = self.load_json()

        for grid_line in grid:
            line = []

            for grid_cell in grid_line:
                cell = Cell(grid_cell)
                line.append(cell)
            
            self.map.append(line)


    def load_json(self):
        file = open("/home/matthieu/Logistikroboter/map/map.json")
        return json.load(file)
    

    def __str__(self):
        string = ""

        for line in self.map:
            for cell in line:
                string += str(cell)
            
            string += "\n"

        return string


if __name__ == "__main__":
    map = Map()
    print(map)