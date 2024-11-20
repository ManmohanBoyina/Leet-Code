from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        tour = {}
        for path in paths:
            tour[path[0]] = path[1]
        for city in tour.values():
            if city not in tour.keys():
                return city
