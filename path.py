from map.map import Map

class Path():
    left = 0
    forward = 1
    right = 2

    path = []
    distance_to_target = 0
    track_points = False
    finished = False
    

    def __init__(self, start, target, nodes, map: Map):
        self.start = start
        self.target = target
        self.calculate(map, nodes)

    def __str__(self):
        return f"Path from {self.start} to {self.target}: {self.path}"
    
    def calculate(self, map: Map, nodes):
        directions = [
            [self.forward, self.forward, self.left, self.right],
            [self.forward, self.forward, self.right, self.left],
            [self.right, self.left, self.forward, self.forward],
            [self.left, self.right, self.forward, self.forward]
        ]

        modifiers = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1]
        ]

        for i, node in enumerate(nodes):
            cell = map.cell(node)

            if not cell.intersection:
                continue

            if i == 0 or i == len(nodes) - 1:
                continue

            for j, line_direction in enumerate(directions):
                if (node[0] + modifiers[j][0], node[1] + modifiers[j][1]) != nodes[i - 1]:
                    continue

                for k, direction in enumerate(line_direction):
                    if (node[0] + modifiers[k][0], node[1] + modifiers[k][1]) != nodes[i + 1]:
                        continue

                    self.path.append(direction)


    def next(self):
        if len(self.path) == 0: 
            return -1
        return self.path.pop(0)
    
    def check_path_done(self):
        if len(self.path) == 0: # if there are no more elements in the list, start to track points
            print("Tracking points...")
            self.track_points = True