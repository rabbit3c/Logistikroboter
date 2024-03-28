import json
from map.cell import Cell

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

        self.calculate_intersections()


    def load_json(self): #load map from json
        file = open("/home/matthieu/Logistikroboter/map/map.json")
        return json.load(file)
    

    def calculate_intersections(self):
        for y, map_line in enumerate(self.map):
            for x, cell in enumerate(map_line):
                if not cell.lane:
                    continue
                amount_neighbours = self.count_neighbours((x, y))
                if amount_neighbours == 4:
                    cell.set_intersection()
    

    def __str__(self):
        string = ""

        for line in self.map:
            for cell in line:
                string += str(cell)
            
            string += "\n"

        return string
    

    def cell(self, point) -> Cell:
        return self.map[point[1]][point[0]]
    

    def set_start(self, start):
        self.cell(start).set_start()


    def set_target(self, target):
        self.cell(target).set_target()


    def nearest_lane(self, point) -> tuple[int, int]: #find nearest path cell to a point
        if self.cell(point).lane:
            return point
        
        x = point[0]
        y = point[1]
        max = len(self.map)

        for i in range(y - 1, y + 2, 2):
            if not i >= 0 or not i < max:
                continue
            if self.cell((x, i)).lane:
                return (x, i)
            
        raise Exception("Target is not adjacent to a path")
    
    
    def successor_nodes(self, point) -> list[tuple[int, int]]: # find adjacent path cells and return them
        nodes = []

        x = point[0]
        y = point[1]

        y_max = len(self.map)
        x_max = len(self.map[0])

        for y2 in range(y - 1, y + 2, 2):
            if not y2 >= 0 or not y2 < y_max:
                continue
            if self.cell((x, y2)).lane:
                nodes.append((x, y2))

        for x2 in range(x - 1, x + 2, 2):
            if not x2 >= 0 or not x2 < x_max:
                continue
            if self.cell((x2, y)).lane:
                nodes.append((x2, y))

        return nodes
    

    def count_neighbours(self, point):
        counter = 0

        x = point[0]
        y = point[1]

        y_max = len(self.map)
        x_max = len(self.map[0])

        for y2 in range(y - 1, y + 2, 2):
            if not y2 >= 0 or not y2 < y_max:
                continue
            if self.cell((x, y2)).lane:
                counter += 1

        for x2 in range(x - 1, x + 2, 2):
            if not x2 >= 0 or not x2 < x_max:
                continue
            if self.cell((x2, y)).lane:
                counter += 1

        return counter
    

    def draw_path(self, start_node, target_node) -> list[tuple[int, int]]:
        node = target_node
        path = []

        while True:
            path.insert(0, node)

            cell = self.cell(node)
            cell.set_path()

            if node == start_node:
                break

            if node == cell.parent:
                raise Exception("node's parent is itself")

            node = cell.parent

        return path
    
