from map.map import Map
from path import Path

# Slightly simplified A* Search Algorithm to calculate
def search(start, target, direction, direction_end=False) -> Path: 
    print("\033[33mStarting Search Algorithm...\033[0m")

    # create instance of the map and set start and target
    map = Map()

    map.set_start(start)
    map.set_target(target)

    print(f"Finding fastest way from \033[32m{start}\033[0m to \033[31m{target}\033[0m")

    print(map)
    print()

    # calcuate nearest node to start and target
    start_node = map.nearest_lane(start)
    target_node = map.nearest_lane(target)

    # block cell behind robot to force robot to drive in right direction
    map.cell((start_node[0] - direction[0], start_node[1] - direction[1])).set_blocked()
    
    # if wanted, block cell in front of target to force robot to drive from right direction
    if direction_end:
        map.cell((target_node[0] + direction_end[0], target_node[1] + direction_end[1])).set_blocked()

    # start of the actual A* Search Algorithm
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


# draw path on map and calculate instructions for robot
def trace_path(map: Map, start_node, target_node) -> Path:
    print("\033[32mPath calculated!\033[0m")
    
    nodes = map.draw_path(start_node, target_node)
    print(map)

    return Path(start_node, target_node, nodes, map)


# Estimate distance to target            
def calculate_h(point, target):
    distance = abs(point[0] - target[0]) + abs(point[1] - target[1])
    return distance


# Find cell with smallest f value
def smallest_f(list: list, map: Map) -> tuple[int, int]:
    best_f = float('inf') 

    for node in list:
        f = map.cell(node).f()
        if f > best_f:
            continue
        if f == best_f:
            if node[0] > 1 and node [0] > or node[1] == 4: # try to avoid the middle of the warehouse
                continue
        best_node = node
        best_f = f
    
    return best_node
        

if __name__ == "__main__":
    path = search((8, 2), (2, 5), (1, 0), (1, 0))
    print(path)