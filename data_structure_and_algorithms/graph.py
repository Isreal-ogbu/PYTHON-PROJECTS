# Depth forst seach and breadth first of a graph.

def dfs(graph, start, stop, visited=None):
    # This checks if the visited node is empty
    if visited is None:
        visited = set()

    # Add the start to the visited Node and print it
    visited.add(start)
    
    
    # I terare through the unvisited node and perform a reculsive call on each node till the end
    for next in graph[start] - visited:
        dfs(graph, next, stop, visited)
    return 


def bfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    queue = list(start)
    while queue:
        val = queue.pop(0)
        if val not in visited:
            print(val, end=" ")
        visited.add(val)
        for next in graph[val] - visited:
            queue.append(next) 

    return 
if __name__ == "__main__":

    data = {
        'A': {'B'}, 'B': {'A', 'C', 'D'}, 'C': {'B', 'E'}, 'D': {'B', 'E'},
        'E': {'C', 'D', 'F'}, 'F': {'E'}
    }
    
    dfs(data, "A", "F")
    print('')
    bfs(data, "A")


# Binary search Tree - max, min, add, preorder, postorder, inorder, search, height.

class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_val(self, data):
        if self.data is None:
            self.data = Tree(data)
        if data < self.data:
            if not self.left:
                self.left = Tree(data)
            return self.left.add_val(data)
        if data > self.data:
            if not self.right:
                self.right = Tree(data)
            return self.right.add_val(data)

    def inorder(self):
        res = []
        if self.left:
            res += self.left.inorder()
        res.append(self.data)
        if self.right:
            res += self.right.inorder()
        return res

    def preorder(self):
        res = [self.data]
        if self.left:
            res += self.left.preorder()
        if self.right:
            res += self.right.preorder()
        return res
    
    def postorder(self):
        res = []
        if self.left:
            res += self.left.postorder()
        if self.right:
            res += self.right.postorder()
        res.append(self.data)
        return res

    def search(self, val):
        if self.data == val:
            return self.data
        elif val < self.data:
            if not self.left:
                return
            return self.left.search(val)
        elif val > self.data:
            if not self.right:
                return
            return self.right.search(val)

    def getsize(self):
        if self.left is not None and self.right is not None:
            return 1 + self.left.getsize() + self.right.getsize()
        elif self.right:
            return 1 + self.right.getsize()
        elif self.left:
            return 1 + self.left.getsize()
        else:
            return 1

    def min_value(self):
        if self.left is None:
            return self.data
        return self.left.min_value()

    def max_value(self):
        if self.right is None:
            return self.data
        return self.right.max_value()


def helper(nums):
    test = Tree(nums[0])
    for i in range(1, len(nums)):
        test.add_val(nums[i])
    return test

if __name__ == '__main__':
    values = [1, 3, 5, 21, 1, 5, 8, 3, 5, 5, 90, 45, 2]
    test = helper(values)
    print(test.inorder())
    print(test.preorder())
    print(test.getsize())
    print(test.search(90))
    print(test.min_value())
    print(test.max_value())

# rotate an image (leetcode)

def rotate(matrix):
    matric = matrix.copy()
    for i in range(len(matric)):
        arr1 = []
        for j in range(len(matric)):
            arr1.append(matric[j][i])
        matrix[i] = arr1[::-1]
    return matrix


print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))

