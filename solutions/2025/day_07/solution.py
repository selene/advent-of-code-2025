# Generated using @xavdid's AoC Python Template: https://github.com/xavdid/advent-of-code-python-template

# puzzle prompt: https://adventofcode.com/2025/day/7

from collections import defaultdict

from ...base import StrSplitSolution, answer


class Solution(StrSplitSolution):
    _year = 2025
    _day = 7

    # @answer(1234)
    def part_1(self) -> int:
        manifold = [list(line) for line in self.input]
        
        num_splits = 0
        beams = []
        for r, line in enumerate(manifold):
            # print(f"line {r}: line")
            next_beams = []
            if 'S' in line:
                # print(f"  found start at {line.index('S')}")
                next_beams = [line.index('S')]
            elif '^' in line:
                
                beam_idx = 0
                curr_beam = beams[beam_idx]
                for c, val in enumerate(line):
                    if c == curr_beam:
                        if val == '.':
                            next_beams.append(c)
                        elif val == '^':
                            # print(f"  beam at {curr_beam} encountered splitter")
                            next_beams.extend([c-1, c+1])
                            num_splits += 1
                        if beam_idx < len(beams) - 1:
                            beam_idx += 1
                            curr_beam = beams[beam_idx]
            else:
                next_beams = beams
            beams = sorted(list(set(next_beams)))
            # print(f"Updated beams: {beams}")

        return num_splits


    # @answer(1234)
    def part_2(self) -> int:
        manifold = [list(line) for line in self.input]
        beams = []
        for r, line in enumerate(manifold):
            next_beams = []
            if 'S' in line:
                # print(f"  found start at {line.index('S')}")
                next_beams = [(line.index('S'), 1)]
            elif '^' in line:
                beam_idx = 0
                curr_pos, curr_count = beams[beam_idx]
                for c, val in enumerate(line):
                    if c == curr_pos:
                        if val == '.':
                            next_beams.append((c, curr_count))
                        elif val == '^':
                            # print(f"  beam at {curr_beam} encountered splitter")
                            next_beams.extend([(c-1, curr_count), (c+1, curr_count)])
                        
                        beam_idx += 1
                        if beam_idx < len(beams):
                            curr_pos, curr_count = beams[beam_idx]
                        else:
                            curr_pos = None
            else:
                next_beams = beams
            
            # print(f"next beams before summing: {next_beams}")
            if len(next_beams) < 2:
                next_sums = next_beams
            else:
                next_sums = []
                prev_pos, prev_count = next_beams[0]
                for pos, count in next_beams[1:]:
                    if pos == prev_pos:
                        prev_count += count
                    else:
                        next_sums.append((prev_pos, prev_count))
                        prev_pos = pos
                        prev_count = count
                next_sums.append((prev_pos, prev_count))
            beams = next_sums
            # print(f"Updated beams: {beams}")
            
        return sum([count for pos, count in beams])
            
            

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
