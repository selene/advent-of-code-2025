# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/8

from dataclasses import dataclass
import math
from ...base import StrSplitSolution, answer


@dataclass
class Pos:
    x: int
    y: int
    z: int
    
    def dist(self, other_pos) -> float:
        return math.sqrt((other_pos.x - self.x)**2 +  (other_pos.y - self.y)**2 + (other_pos.z - self.z)**2)
    
    def __hash__(self):
        return hash((self.x, self.y, self.z))
    
    def __str__(self):
        return f'({self.x},{self.y},{self.z})'

@dataclass
class Pair:
    pos1: Pos
    pos2: Pos
    dist: float

    def __hash__(self):
        return hash((self.pos1, self.pos2, dist))

class Solution(StrSplitSolution):
    _year = 2025
    _day = 8

    def load_coordinates(self):
        coords = []
        for line in self.input:
            xstr, ystr, zstr = line.split(',')
            coords.append(Pos(int(xstr), int(ystr), int(zstr)))
        return sorted(coords, key=lambda p: p.x)

    def find_closest_pairs(self, coordinates):
        pairs = []
        for i, pos1 in enumerate(coordinates[:-1]):
            for j, pos2 in enumerate(coordinates[i+1:]):
                dist = pos1.dist(pos2)
                pairs.append(Pair(pos1, pos2, dist))

        return sorted(pairs, key=lambda p: p.dist)
                
        

    @answer(83520)
    def part_1(self) -> int:
        coords = self.load_coordinates()
        pairs = self.find_closest_pairs(coords)[:1000]
        # print(pairs)
        
        circuits = {}
        for pair in pairs:
            pos1 = pair.pos1
            pos2 = pair.pos2
            
            new_circuit = circuits.get(pos1, set()) | circuits.get(pos2, set()) | set([pos1, pos2])
            for p in new_circuit:
                circuits[p] = new_circuit
        
        unique_circuits = []
        for c in circuits.values():
            if c not in unique_circuits:
                unique_circuits.append(c)
        
        sorted_circuits = sorted(unique_circuits, key=len, reverse=True)
        print(f"Final circuits count: {len(sorted_circuits)}")
        # print(sorted_circuits[:10])
        product = 1
        for circ in sorted_circuits[:3]:
            product *= len(circ)
        return product
        
        

    @answer(1131823407)
    def part_2(self) -> int:
        coords = self.load_coordinates()
        pairs = self.find_closest_pairs(coords)
        
        circuits = {}
        seen_pos = set()
        for i, pair in enumerate(pairs):
            pos1 = pair.pos1
            pos2 = pair.pos2

            seen_pos.add(pos1)
            seen_pos.add(pos2)
            if pos1 in circuits and pos2 in circuits:
                new_circuit = circuits[pos1] | circuits[pos2]
                for p in new_circuit:
                    circuits[p] = new_circuit
            elif pos1 in circuits:
                circuits[pos1].add(pos2)
                circuits[pos2] = circuits[pos1]
            elif pos2 in circuits:
                circuits[pos2].add(pos1)
                circuits[pos1] = circuits[pos2]
            else:
                new_circuit = set([pos1, pos2])
                circuits[pos1] = new_circuit
                circuits[pos2] = new_circuit

            if len(seen_pos) == len(coords):
                print(f"All positions seen at iteration {i}")
            if len(circuits[pos1]) == len(coords):
                print(f"Final circuit connected at iteration {i}")
                return pos1.x * pos2.x
        

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
