class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = [] # 이웃한 정점 정보
        
    def add_adjacent_vertex(self, vertex):
        self.adjacent_vertices.append(vertex)
        
    def remove_adjacent_vertex(self, vertex):
        for i in range(len(self.adjacent_vertices)):
            if self.adjacent_vertices[i] == vertex:
                self.adjacent_vertices.pop(i)
                break

# 정점 생성
jake = Vertex("Jake")
ben = Vertex("Ben")
joy = Vertex("Joy")
ivy = Vertex("Ivy")
elin = Vertex("Elin")
anna = Vertex("Anna")
david = Vertex("David")

# 정점 연결
jake.add_adjacent_vertex(ben)
ben.add_adjacent_vertex(jake)
joy.add_adjacent_vertex(ben)
joy.add_adjacent_vertex(ivy)
ivy.add_adjacent_vertex(joy)
ivy.add_adjacent_vertex(ben)
elin.add_adjacent_vertex(ivy)
elin.add_adjacent_vertex(anna)
anna.add_adjacent_vertex(ben)
anna.add_adjacent_vertex(david)
anna.add_adjacent_vertex(elin)
david.add_adjacent_vertex(anna)

# anna의 인접 정점 출력
print([vertex.value for vertex in anna.adjacent_vertices])
# jake의 인접 정점 출력
print([vertex.value for vertex in jake.adjacent_vertices])

# david 제거 후, anna의 인접 정점 출력
anna.remove_adjacent_vertex(david)
print([vertex.value for vertex in anna.adjacent_vertices])