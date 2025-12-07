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
            print(f"Updated beams: {beams}")

        return num_splits


    # @answer(1234)
    def part_2(self) -> int:
        manifold = [list(line) for line in self.input]
        
        num_timelines = 0
        beams = defaultdict(lambda: 0)
        beam_list = []
        for r, line in enumerate(manifold):
            # self.debug(f"line {r}: {''.join(line)}")
            next_beams = defaultdict(lambda: 0)
            beam_keys = list(beams.keys())
            next_beam_list = []
            if 'S' in line:
                # self.debug(f"  found start at {line.index('S')}")
                next_beams[line.index('S')] = 1
                next_beam_list = [line.index('S')]
            elif '^' in line:
                # Use dict count
                beam_idx = 0
                curr_beam = beam_keys[beam_idx]
                for c, val in enumerate(line):
                    if c == curr_beam:
                        if val == '.':
                            next_beams[c] = beams[c]
                        elif val == '^':
                            # self.debug(f"  beam at {curr_beam} encountered splitter")
                            next_beams[c-1] += beams[c]
                            next_beams[c+1] += beams[c]
                            # num_timelines += beams[c] * 2
                        if beam_idx < len(beam_keys) - 1:
                            beam_idx += 1
                            curr_beam = beam_keys[beam_idx]
                        else:
                            curr_beam = None
                            
                # Use list
                beam_idx = 0
                curr_beam = beam_list[beam_idx]
                for c, val in enumerate(line):
                    while c == curr_beam:
                        if val == '.':
                            next_beam_list.append(c)
                        elif val == '^':
                            # print(f"  beam at {curr_beam} encountered splitter")
                            next_beam_list.extend([c-1, c+1])
                        beam_idx += 1
                        if beam_idx < len(beams):
                            curr_beam = beam_list[beam_idx]
                        else:
                            curr_beam = None
            else:
                next_beams = beams
                next_beam_list = beam_list
            beams = next_beams
            beam_list = next_beam_list
            
            beam_strs = []
            for i in range(len(self.input[0])):
                if i in beams:
                    val = beams[i]
                    if val < 10:
                        beam_strs.append(f" {val} ")
                    else:
                        beam_strs.append(f"{val} ")
                else:
                    beam_strs.append(' . ')
            # self.debug(f"Updated beams: {beams}")
            line_str = ' '.join([f' {c} ' for c in line])
            # self.debug(line_str)
            self.debug(' '.join(beam_strs))
            self.debug(beam_list)

        # return num_timelines
        return sum(beams.values())

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
