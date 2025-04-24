from tree import Node

class KnightPathFinder():
    def __init__(self, coord):
        (xi, yi) = coord
        self._x = xi
        self._y = yi
        self._coord = coord
        self._root = Node(coord)
        self._considered_positions = set([coord])



    def get_valid_moves(self, coord):
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


    def new_move_positions(self, coord):
        validMoves = self.get_valid_moves(coord)
        newUnvisited = validMoves - self._considered_positions #take out ones already in visited list
        # unvisited = [move for move in validMoves if move not in self._considered_positions]
        self._considered_positions.update(newUnvisited)    #add these new moves to visited
        return newUnvisited


    def find_path(self, destination):
        (xf, yf) = destination


# finder = KnightPathFinder((0, 0))
# print(finder.new_move_positions((0, 0)))   # Expected outcome: {(1, 2), (2, 1)}
