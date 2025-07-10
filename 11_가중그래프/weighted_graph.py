class WeightedGraphVertex:
    def __init__(self, value):
        self.value = value
        self.adjacent_vertices = {}
        
    def add_adjacent_vertex(self, vertex, weight):
        self.add_adjacent_vertex[vertex.value] = weight
    
    def remove_adjacent_vertex(self, vertex):
        self.adjacent_vertices.pop(vertex.value, None)
        
# 정점 생성
seoul = WeightedGraphVertex("서울")
wonju = WeightedGraphVertex("원주")
gangneung = WeightedGraphVertex("강릉")
daejeon = WeightedGraphVertex("대전")
jeonju = WeightedGraphVertex("전주")
daegu = WeightedGraphVertex("대구")

# 간선 추가
seoul.add_adjacent_vertex(wonju, 87)
seoul.add_adjacent_vertex(daejeon, 140)
seoul.add_adjacent_vertex(jeonju, 187)

# 출력
print(seoul.adjacent_vertices)  
# → {'원주': 87, '대전': 140, '전주': 187}

# 간선 제거
seoul.remove_adjacent_vertex(jeonju)

# 출력
print(seoul.adjacent_vertices)  
# → {'원주': 87, '대전': 140}
