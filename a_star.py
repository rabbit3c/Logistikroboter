from map.map import Map
from map.cell import Cell
from path import Path


def search(start, target, direction) -> Path: #A* Search Algorithm
    print("Starting Search Algorithm...")

    map = Map()

    map.set_start(start)
    map.set_target(target)

    print(f"Finding fastest way from \033[32m{start}\033[0m to \033[31m{target}\033[0m")

    print(map)
    print()

    start_node = map.nearest_lane(start)
    target_node = map.nearest_lane(target)

    map.cell((start_node[0] - direction[0], start_node[1] - direction[1])).set_blocked()

    map.cell(start_node).g = 0 # distance of start_cell to start is 0

    open_list = [start_node] # nodes to explore
    closed_list = [] # already explored nodes

    while len(open_list) > 0:
        q = smallest_f(open_list, map)
        open_list.remove(q)

        q_cell = map.cell(q)

        successors = map.successor_nodes(q)

        for successor in successors:
            cell = map.cell(successor)

            if successor == target_node:
                cell.parent = q
                path = trace_path(map, start_node, target_node)
                return path

            if successor in open_list:
                continue

            if successor in closed_list:
                continue

            cell.g = q_cell.g + 1 # compute g, which is the distance to the start node
            cell.h = calculate_h(successor, target_node)

            cell.parent = q
            open_list.append(successor)
        
        closed_list.append(q)

    raise Exception("No Path was found")

    
def trace_path(map: Map, start_node, target_node) -> Path: # draw path on map and calculate instructions for robot
    print("Path calculated!")
    
    nodes = map.draw_path(start_node, target_node)
    print(map)

    return Path(start_node, target_node, nodes, map)


            
def calculate_h(point, target): # estimate distance to target
    distance = abs(point[0] - target[0]) + abs(point[1] - target[1])
    return distance


def smallest_f(list: list, map: Map) -> tuple[int, int]: # find cell with smallest f value
    best_f = float('inf') 

    for node in list:
        f = map.cell(node).f()
        if f > best_f:
            continue
        if f == best_f:
            if node[0] == 6 or node[1] == 4: #try to avoid the middle
                continue
        best_node = node
        best_f = f
    
    return best_node
        

if __name__ == "__main__":
    path = search((8, 2), (1, 5), (1, 0))
    print(path)