# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/3

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 3
    separator = "\n"

    # @answer(17427)
    def part_1(self) -> int:
        total = 0
        
        print(f"input: {self.input}")
        for bank in self.input:
            print(f"  bank: {bank}")
            high1 = int(bank[-2])
            high2 = int(bank[-1])
            for d_str in bank[:-2][::-1]:
                digit = int(d_str)
                if digit >= high1:
                    if high1 >= high2:
                        high2 = high1
                    high1 = digit
            jolts = high1 * 10 + high2
            print(f"    jolts: {jolts}")
            total += jolts
        
        return total

    # @answer(1234)
    def part_2(self) -> int:
        total = 0
        
        for bank in self.input:
            print(f"  bank: {bank}")
            highs = [int(d) for d in bank[-13:]]
            for d_str in bank[:-13][::-1]:
                digit = int(d_str)
                old_highs = [*highs]
                for i in range(0, 12):
                    if digit >= highs[i]:
                        highs[i] = digit
                        digit = old_highs[i]
            jolts = int(''.join([str(h) for h in highs]))
            print(f"    jolts: {jolts}")
            total += jolts
        return total
                    
                    
                        

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
