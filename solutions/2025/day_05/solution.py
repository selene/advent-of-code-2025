# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/5

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 5

    def parse_input(self):
        blank_idx = self.input.index('')
        ranges = [
            [int(n) for n in rng.split('-')]
            for rng in self.input[:blank_idx]
        ]
        ids = [int(n) for n in self.input[blank_idx+1:]]
        
        return ranges, ids

    # def part_1(self) -> int:
    #     # DUMBEST WAY
    #     ranges, ids = self.parse_input()
        
    #     valid_count = 0
    #     for i in ids:
    #         for rng in ranges:
    #             if i >= rng[0] and i <= rng[1]:
    #                 valid_count += 1
    #                 break
        
    #     return valid_count

    def merge_ranges(self, ranges):
        sorted_ranges = sorted(ranges)
        merged_ranges = []
        curr_rng = sorted_ranges[0]
        for rng in sorted_ranges[1:]:
            if curr_rng[1] >= rng[0] - 1:
                curr_rng[1] = max(curr_rng[1], rng[1])
            else:
                merged_ranges.append(curr_rng)
                curr_rng = rng
        merged_ranges.append(curr_rng)
        return merged_ranges


    @answer(701)
    def part_1(self) -> int:
        ranges, ids = self.parse_input()
        
        ranges = sorted(ranges)
        # print(ranges)
        print(f"{len(ids)} ids")
        print(ids)
        
        merged_ranges = self.merge_ranges(ranges)
        
        print(f"merged_ranges\n{merged_ranges}")
        valid_count = 0
        for i in ids:
            valid = False
            upper = len(merged_ranges)
            lower = 0
            
            pivot = lower + (upper - lower)//2
            # print(f"Checking id {i}")
            while upper > lower:
                pivot_range = merged_ranges[pivot]
                # print(f"  {lower} -- {pivot}({pivot_range}) -- {upper}")
                if i >= pivot_range[0] and i <= pivot_range[1]:
                    valid = True
                    break
                elif i < pivot_range[0]:
                    upper = pivot
                elif i > pivot_range[1]:
                    lower = pivot + 1
                else:
                    break
                pivot = lower + (upper - lower)//2
            if valid:
                # print("  valid!")
                valid_count += 1
        
        return valid_count

    @answer(352340558684863)
    def part_2(self) -> int:
        ranges, ids = self.parse_input()
        
        ranges = sorted(ranges)
        merged_ranges = self.merge_ranges(ranges)
        
        valid_count = 0
        for rng in merged_ranges:
            valid_count += rng[1] - rng[0] + 1
        
        return valid_count

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
