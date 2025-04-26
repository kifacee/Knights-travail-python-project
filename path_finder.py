from tree import Node

class KnightPathFinder():
    def __init__(self, coord):
        (xi, yi) = coord
        self._x = xi
        self._y = yi
        self._coord = coord
        self._root = Node(coord)    #sets node._value = coord
        self._considered_positions = set([coord])



    def get_valid_moves(self, coord):   # coord is a tuple, not a Node instance
        moves = [
        (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)
        ]
        x, y = coord

        validMoves = [(x + dx, y + dy)
                      for dx, dy in moves
                      if (x + dx in range(8) and (y + dy in range(8)))
                      #  and (x + dx, y + dy) not in self._considered_positions #happens in new_move_positions
                      ]
        return set(validMoves)


        # for dx, dy in moves:
        #     new_x = x + dx
        #     new_y = y + dy
        #     if new_x in range(8) & new


    def new_move_positions(self, coord):        # coord is a tuple, not a Node instance
        validMoves = self.get_valid_moves(coord)
        newUnvisited = validMoves - self._considered_positions #take out ones already in visited list
        # unvisited = [move for move in validMoves if move not in self._considered_positions]
        self._considered_positions.update(newUnvisited)    #add these new moves to visited
        return newUnvisited


    def find_path(self, destination):
        (xf, yf) = destination


    def build_move_tree(self):      #assigns all child relationships based on unvisted places you can move to
        from collections import deque

        queue = deque([self._root])
        while queue:
            currentNode = queue.popleft()
            currentCoord = currentNode.value
            moveOptions = self.new_move_positions(currentCoord) #returns a list of coord tuples
            #add each valid, unvisited move as a child of the current node
            for option in moveOptions:
                nodeOption = Node(option)   #need to create ONE instance so you can enqueue and append that same instance
                currentNode.add_child(nodeOption)   #add child takes a NODE as an argument
                queue.append(nodeOption)        #add each new coordinate AS A NODE to the queue for BFS


    def find_path(self, endCoord):
        endNode = self._root.breadth_search(endCoord)  # returns a node
        return self.trace_to_root(endNode)


    def trace_to_root(self, endNode):
        from collections import deque
        currentNode = endNode
        path = deque([])
        while currentNode:
            path.appendleft(currentNode.value)    # want the order to be start to end, so using appendleft
            currentNode = currentNode.parent
        return path




# def print_tree(node, depth=0):
#     indent = "  " * depth
#     print(f"{indent}{node.value}")
#     for child in node.children:
#         print_tree(child, depth + 1)



# from graphviz import Digraph

# def visualize_tree(root_node):
#     dot = Digraph()
#     def add_nodes(node):
#         dot.node(str(node.value))
#         for child in node.children:
#             dot.edge(str(node.value), str(child.value))
#             add_nodes(child)
#     add_nodes(root_node)
#     return dot


# finder = KnightPathFinder((0, 0))
# print(finder.new_move_positions((0, 0)))   # Expected outcome: {(1, 2), (2, 1)}

# finder = KnightPathFinder((0, 0))
# finder.build_move_tree()
# print(finder._root.children[0].children)

# finder = KnightPathFinder((0, 0))
# finder.build_move_tree()
# print(finder.find_path((2, 1))) # => [(0, 0), (2, 1)]
# print(finder.find_path((3, 3))) # => [(0, 0), (2, 1), (3, 3)]
# print(finder.find_path((6, 2))) # => [(0, 0), (1, 2), (2, 4), (4, 3), (6, 2)]
# print(finder.find_path((7, 6))) # => [(0, 0), (1, 2), (2, 4), (4, 3), (5, 5), (7, 6)]


# finder = KnightPathFinder((0, 0))
# finder.build_move_tree()
# print_tree(finder._root)  # Show the whole tree

# path = finder.find_path((3, 3))
# print("Shortest path:", list(path))   #show just one path



#graphviz testing
# finder = KnightPathFinder((0, 0))
# finder.build_move_tree()
# dot = visualize_tree(finder._root)
# dot.render('knight_tree', view=True)  # creates a PDF and opens it
