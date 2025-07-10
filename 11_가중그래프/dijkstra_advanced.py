"""
"""
import math
from typing import Dict

class City:
    def __init__(self, name: str):
        self.name = name
        self.adjacent_cities = {}
    
    def add_adjacent_city(self, city: "City", distance: float) -> None:
        self.adjacent_cities[city.name] = distance
        
    def remove_adjacent_city(self, city: "City") -> None:
        self.adjacent_cities.pop(city.name, None)
    
class Dijkstra:
    def __init__(self):
        self.all_cities = {}
        
    def register_city(self, city: City) -> None:
        self.all_cities[city.name] = city
    
    def shortest_paths(self, start: City) -> Dict[str, float]:
        unvisited = set(self.all_cities.keys())
        distance = {name: math.inf for name in self.all_cities}
        distance[start.name] = 0.0 # 시작점부터 시작점까지의 거리는 0
    
        while unvisited:
            curr = min(unvisited, key=lambda name: distance[name])
            unvisited.remove(curr)
            
            curr_city = self.all_cities[curr]
            for nbr_name, w in curr_city.adjacent_cities.items():
                if nbr_name not in unvisited:
                    continue
                alt_dist = distance[curr] + w # 현재 도시(curr)를 거쳐 인접 도시(nbr_name)까지 가는 후보 거리
                if alt_dist < distance[nbr_name]:
                    distance[nbr_name] = alt_dist
        
        return distance

seoul = City("서울")
wonju = City("원주")
gangneung = City("강릉")
daejeon = City("대전")
jeonju = City("전주")
daegu = City("대구")

dj = Dijkstra()
for city in (seoul, wonju, gangneung, daejeon, jeonju, daegu):
    dj.register_city(city)

edges = [ # 간선 정보
    (seoul, wonju, 87),
    (seoul, gangneung, 165),
    (seoul, daejeon, 140),
    (seoul, jeonju, 187),
    (wonju, gangneung, 95),
    (wonju, daejeon, 118),
    (wonju, daegu, 178),
    (gangneung, daegu, 212),
    (daejeon, jeonju, 56),
    (daejeon, daegu, 122),
    (jeonju, daegu, 130),
]

for a, b, w in edges:
    a.add_adjacent_city(b, w)
    b.add_adjacent_city(a, w)
    
distances = dj.shortest_paths(seoul)
print(distances)