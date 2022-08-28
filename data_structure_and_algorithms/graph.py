# Depth forst seach and breadth first of a graph.

def dfs(graph, start, visited=None):
    # This checks if the visited node is empty
    if visited is None:
        visited = set()

    # Add the start to the visited Node and print it
    visited.add(start)
    print(start, end=" ")

    # I terare through the unvisited node and perform a reculsive call on each node till the end
    for next in graph[start] - visited:
        dfs(graph, next, visited)
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
    
    dfs(data, "B")
    print('')
    bfs(data, "B")