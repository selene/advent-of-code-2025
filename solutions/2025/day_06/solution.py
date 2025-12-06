# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/6

import re
    
from ...base import StrSplitSolution, answer


class MathProblem:
    problems = []
    operation = ""

class Solution(StrSplitSolution):
    _year = 2025
    _day = 6

    def parse_input(self):
        problems = None
        for line in self.input:
            print(line)
            cols = re.split(r'\s+', line.strip())
            print(cols)
            if not problems:
                problems = [[] for c in cols]
            for i, val in enumerate(cols):
                if val == "*" or val == "+":
                    problems[i].append(val)
                else:
                    problems[i].append(int(val))
        
        print(f"final problems:\n{problems}")
        return problems
        
            

    # @answer(1234)
    def part_1(self) -> int:
        problems = self.parse_input()
        
        total = 0
        for problem in problems:
            # print(f"problem: {problem}")
            operator = problem[-1]
            if operator == '+':
                total += sum(problem[:-1])
            elif operator == '*':
                mult = 1
                for num in problem[:-1]:
                    mult = mult * num
                total += mult
            else:
                print(f"Help, invalid operator {problems[-1]}!")
        return total

    # @answer(1234)
    def part_2(self) -> int:
        pass

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
