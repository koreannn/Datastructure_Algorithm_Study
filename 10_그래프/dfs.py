class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = []
        
    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)
    
    def remove_adjacent_vertex(self, vertex):
        for i in range(len(self.adjacent_vertices)):
            if self.adjacent_vertices[i] == vertex:
                self.adjacent_vertices.pop(i)
                break
            
def dfs(vertex: "Vertex", visited_vertices = None):
    if visited_vertices is None:
        visited_vertices = {}
        
    visited_vertices[vertex.value] # 방문한 정점은 visited에 표기
    print(f"정점: {vertex.value}") # 현재 방문한 정점 출력
    
    for adjacent in vertex.adjacent_vertices:
        if visited_vertices.get(adjacent.value, False): # 이미 방문했던 노드라면 pass
            continue 
        dfs(adjacent, visited_vertices) # 방문한 정점이 아니라면, 그 정점을 대상으로 깊이 우선 탐색 수행
        
ben = Vertex("Ben")
ivy = Vertex("Ivy")
joy = Vertex("Joy")
jake = Vertex("Jake")
anna = Vertex("Anna")
david = Vertex("David")
elin = Vertex("Elin")
owen = Vertex("Owen")

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

dfs(ben)