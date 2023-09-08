from enum import Enum


class NetworkNode:
    def __init__(self, color: Enum, value: int):
        self.color = color
        self.value = value


def check_path(grid: list[list[NetworkNode]], max_diff: int, start_coord) -> bool:
    # create a set of already visisted nodes,
    # a queue of nodes to visit, and target node of bottom corner
    visited_coords = set()
    node_queue = [start_coord]
    target = (len(grid)-1, len(grid[0])-1)
    
    # Check if nodes share color
    # or have a absolute difference in values less than the max_diff
    def check_if_neighbor(base_node: NetworkNode,
    potential_neighbor: NetworkNode, max_diff: int) -> bool:
        if base_node.color == potential_neighbor.color \
                or abs(base_node.value - potential_neighbor.value) <= max_diff:
            return True
        return False

    def add_node_to_queue(old_coord: tuple, new_coord: tuple):
        if new_coord not in visited_coords \
                and new_coord[0] in range(len(grid)) \
                and new_coord[1] in range(len(grid[0])) \
                and check_if_neighbor(grid[old_coord[0]][old_coord[1]], grid[new_coord[0]][new_coord[1]], max_diff):
            node_queue.append(new_coord)

    while len(node_queue) > 0:
        node = node_queue.pop()
        if (node[0], node[1]) not in visited_coords:
            visited_coords.add((node[0], node[1]))

            # Check potential neighbors
        potential_neighbor = [(node[0]+1, node[1]),
                                (node[0]-1, node[1]),
                                (node[0], node[1]-1),
                                (node[0], node[1]+1)]
        for coordinate in potential_neighbor:
            add_node_to_queue(node, coordinate)

        # east_node = (node[0]+1, node[1])
        # west_node = (node[0]-1, node[1])
        # north_node = (node[0], node[1]-1)
        # south_node = (node[0], node[1]+1)
        # add_node_to_queue(node, east_node)
        # add_node_to_queue(node, west_node)
        # add_node_to_queue(node, north_node)
        # add_node_to_queue(node, south_node)
        if target in visited_coords:
            return True
    return False


node1 = NetworkNode("blue", 1)
node2 = NetworkNode("yellow", 10)
node3 = NetworkNode("yellow", 11)

node4 = NetworkNode("blue", 6)
node5 = NetworkNode("red", 9)
node6 = NetworkNode("yellow", 2)

node7 = NetworkNode("blue", 10)
node8 = NetworkNode("yellow", 10)
node9 = NetworkNode("blue", 2)

row1 = [node1, node2, node3]
row2 = [node4, node5, node6]
row3 = [node7, node8, node9]
sample_grid = [row1, row2, row3]

start_coord = (0, 0)

print(check_path(sample_grid, 2, start_coord))