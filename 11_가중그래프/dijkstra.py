import math
from typing import Dict, Optional, Tuple, List

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
        self.all_cities = {} # mappping city name -> City instance
    
    def register_city(self, city: City) -> None:
        self.all_cities[city.name] = city
        
    def shortest_path(self, start:City, end: City) -> Optional[List[str]]:
        dist = {name: math.inf for name in self.all_cities}
        prev = {name: None for name in self.all_cities}
        
        dist[start.name] = 0.0
        
        unvisited = set(self.all_cities.keys())
        visited = set()
        
        while unvisited:
            curr = min(unvisited, key=lambda name: dist[name])
            unvisited.remove(curr)
            visited.add(curr)
            
            if curr == end.name:
                break
            
            curr_city = self.all_cities[curr]
            for nbr_name, weight in curr_city.adjacent_cities.items():
                if nbr_name in visited:
                    continue
                alt = dist[curr] + weight
                if alt < dist[nbr_name]:
                    dist[nbr_name] = alt
                    prev[nbr_name] = curr
        
        if dist[end.name] == math.inf:
            print(f"No path from {start.name} -> {end.name}")
            return None
        
        path = []
        cur = end.name
        while cur is not None:
            path.append(cur)
            cur = prev[cur]
        path.reverse()
        
        print(" -> ".join(path), f"(total distance: {dist[end.name]})")
        return path
            
        

# create cities
seoul = City("서울")
wonju = City("원주")
gangneung = City("강릉")
daejeon = City("대전")
jeonju = City("전주")
daegu = City("대구")

# register in graph
dj = Dijkstra()
for city in (seoul, wonju, gangneung, daejeon, jeonju, daegu):
    dj.register_city(city)

# add edges (bidirectional)
edges = [
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

# compute and print shortest path
dj.shortest_path(seoul, daegu)