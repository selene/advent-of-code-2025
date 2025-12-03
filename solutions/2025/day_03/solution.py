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
        
        for bank in self.input:
            high1 = int(bank[-2])
            high2 = int(bank[-1])
            for d_str in bank[:-2][::-1]:
                digit = int(d_str)
                if digit >= high1:
                    if high1 >= high2:
                        high2 = high1
                    high1 = digit
            jolts = high1 * 10 + high2
            total += jolts
        
        return total

    # @answer(1234)
    def part_2(self) -> int:
        total = 0
        
        # Approach:
        # Get the last 12 digits of the bank
        # Starting from the digit before that (bank[-12]), compare against the
        # leftmost digit
        # If it's higher:
        #   Save the new digit as the leftmost
        #   Compare the previous leftmost digit against the next leftmost
        #   Keep bumping digits down as long as they're higher than the old one
        # Stop bumping if we find one that's not higher
        for bank_str in self.input:
            bank = [int(b) for b in bank_str]
            print(f"  bank: {bank}")
            highs = list(range(len(bank) - 12, len(bank)))
            remaining_bank = bank[:-12]
            print(f"    reversed bank after last 12 digits removed: {bank[:-12][::-1]}")
            for offset, digit in enumerate(remaining_bank[::-1]):
                # print(f"    digit={digit}, offset={offset}")
                # print(f"    high indexes={highs}")
                # print(f"    high values ={[bank[h] for h in highs]}")
                idx = len(bank) - 12 - offset - 1
                # print(f"   idx={idx}")
                old_highs = [*highs]
                for i in range(0, 12):
                    if digit >= bank[highs[i]]:
                        highs[i] = idx
                        digit = bank[old_highs[i]]
                        idx = old_highs[i]
                    else:
                        break
            jolts = int(''.join([str(bank[h]) for h in highs]))
            print(f"    jolts: {jolts}")
            total += jolts
        return total
                    
                    
                        

    # @answer((1234, 4567))
    # def solve(self) -> tuple[int, int]:
    #     pass
