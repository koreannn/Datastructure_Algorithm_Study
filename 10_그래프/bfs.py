from collections import deque

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_verticies = []
        
    def add_adjacent_vertex(self, vertex):
        self.adjacent_verticies.append(vertex)
    
    def remove_adjacent_vertex(self, vertex):
        self.adjacent_verticies = [
            v for v in self.adjacent_verticies if v is not vertex
            ]

def bfs(start_vertex):
    visited = set([start_vertex])
    queue = deque([start_vertex])
    
    while queue:
        curr = queue.popleft()
        print(f"정점: {curr.value}")
        
        for neighbor in curr.adjacent_verticies:
            if neighbor not in visited: # 방문했던 노드가 아닐 경우에만
                visited.add(neighbor)
                queue.append(neighbor)
                
                                
def dfs(vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    
    print(f"정점: {vertex.value}")
    
    for neighbor in vertex.adjacent_verticies:
        if neighbor not in visited:
            dfs(neighbor, visited)


# 그래프 생성
ben   = Vertex("Ben")
ivy   = Vertex("Ivy")
joy   = Vertex("Joy")
jake  = Vertex("Jake")
anna  = Vertex("Anna")
david = Vertex("David")
elin  = Vertex("Elin")
owen  = Vertex("Owen")

ben.add_adjacent_vertex(ivy)
ben.add_adjacent_vertex(jake)
ben.add_adjacent_vertex(anna)
ben.add_adjacent_vertex(david)

ivy.add_adjacent_vertex(ben)
ivy.add_adjacent_vertex(joy)

joy.add_adjacent_vertex(ivy)
joy.add_adjacent_vertex(jake)

jake.add_adjacent_vertex(ben)
jake.add_adjacent_vertex(joy)

anna.add_adjacent_vertex(ben)

david.add_adjacent_vertex(ben)
david.add_adjacent_vertex(elin)

elin.add_adjacent_vertex(david)
elin.add_adjacent_vertex(owen)

owen.add_adjacent_vertex(elin)


# 탐색
print("DFS 순회:")
dfs(ben)

print()
print("\nBFS 순회:")
bfs(ben)