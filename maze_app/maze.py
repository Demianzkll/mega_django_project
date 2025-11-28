from dataclasses import dataclass
from typing import Optional
import random

@dataclass
class Node:
    loc: tuple  
    state: int
    parent: Optional['Node'] = None




class Maze:
    def __init__(self, size):
        self.size = size
        self.grid = [[0 for col in range(self.size)] for row in range(self.size)]
        self.path = []

    def __str__(self):
        out = ''
        for row in range(self.size):
            for col in range(self.size):
                if (row, col) in self.path:
                    out += '*'
                else:
                    out += ('X' if self.grid[row][col] else ' ')
            out += '\n'
        return out
    

    def generate(self):
        # self.grid = [
        #     [0, 0, 0, 0],
        #     [1, 0, 1, 0],
        #     [0, 0, 1, 1],
        #     [1, 0, 0, 0]
        # ]
        self.path = []
        for row in range(self.size):
            for col in range(self.size):
                self.grid[row][col] = 0 if random.uniform(0.0, 1.0) < 0.7 else 1
        self.grid[0][0] = 0
        self.grid[-1][-1] = 0




    def get_state(self, loc):
        row = loc[0]
        col = loc[1]
        return self.grid[row][col]


    def is_loc_valid(self, loc):
        row = loc[0]
        col = loc[1]
        return (0 <= col < self.size) and (0 <= row < self.size)



    def get_neighbours(self, loc):
        res = []
        row, col = loc

        # up
        up = (row - 1, col)
        if self.is_loc_valid(up) and self.get_state(up) != 1:
            res.append(up)

        # down
        down = (row + 1, col)
        if self.is_loc_valid(down) and self.get_state(down) != 1:
            res.append(down)

        # left
        left = (row, col - 1)
        if self.is_loc_valid(left) and self.get_state(left) != 1:
            res.append(left)

        # right
        right = (row, col + 1)
        if self.is_loc_valid(right) and self.get_state(right) != 1:
            res.append(right)

        return res



    def solve(self):
        node = Node((0,0), self.grid[0][0])
        visited = []
        stack = [node]
        while len(stack) != 0:
            node = stack.pop()
            visited.append(node.loc)

            if node.loc == (self.size-1, self.size-1):
                tn = node
                while tn.parent != None:
                    print('-->', tn.loc)
                    self.path.append(tn.loc)
                    tn = tn.parent
                print('Path was found')
                return
             
            neighbours = self.get_neighbours(node.loc)
            for n_loc in neighbours:
                if n_loc not in visited:
                    stack.append(Node(n_loc, self.grid[n_loc[0]][n_loc[1]], node))

        print('No path was found')


maze = Maze(5)
maze.generate()
print(maze)
maze.solve()
print(maze)

node_a = Node((0,0), 1)
node_b = Node((0,1), 1, node_a)
print(node_b.parent.loc)
