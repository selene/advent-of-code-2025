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

    def parse_input1(self):
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
        problems = self.parse_input1()
        
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


    def parse_input2(self):
        problems = None
        numbers = None
        operators = []
        
        widths = []
        curr_start = 0
        print(f"operators row: {self.input[-1]}")
        for i, val in enumerate(self.input[-1]): # The operators row
            if val in ["*", "+"]:
                operators.append(val)
                if i != 0:
                    widths.append(i - curr_start - 1)
                    curr_start = i
        widths.append(len(self.input[-1]) - curr_start)
        print(f"widths: {widths}")
        
        
        columns = [[] for w in widths]
        for r, line in enumerate(self.input[:-1]):
            # print(f"line {r}: {line}")
            col_start = 0
            for c, w in enumerate(widths):
                col_end = col_start + w
                # print(f"  col range: {col_start}..{col_end}, width={w}")
                columns[c].append(line[col_start:col_end])
                # print(f"    appending to col {c}: {line[col_start:col_end]}")
                col_start = col_end + 1
        print(f"columns\n{columns}")
            
        problems = []
        for i, column in enumerate(columns):
            operator = operators[i]
            
            transp = list(zip(*[list(val) for val in column]))
            # print(f"transp:\n{transp}")
            numbers = [int(''.join(digits)) for digits in transp]
            # print(f"  numbers:   {numbers}")
            
            problems.append((operator, numbers))
        
        print(f"final problems:\n{problems}")
        return problems

    @answer(11494432585168)
    def part_2(self) -> int:
        problems = self.parse_input2()
        
        total = 0
        for p in problems:
            if p[0] == "+":
                total += sum(p[1])
            elif p[0] == "*":
                product = 1
                for n in p[1]:
                    product *= n
                total += product
        return total
        

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
