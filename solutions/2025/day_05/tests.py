# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 22:31:50 2025

@author: water
"""
import unittest

def merge_ranges(ranges):
    sorted_ranges = sorted(ranges)
    merged_ranges = []
    curr_rng = sorted_ranges[0]
    for rng in sorted_ranges[1:]:
        if curr_rng[1] >= rng[0] - 1:
            curr_rng[1] = rng[1]
        else:
            merged_ranges.append(curr_rng)
            curr_rng = rng
    merged_ranges.append(curr_rng)
    return merged_ranges


class TestRange(unittest.TestCase):
    def test_no_overlap(self):
        self.assertEqual(
            [[1,2], [4,5], [7,20]],
            merge_ranges([[1,2], [4,5], [7,20]])
        )

    def test_full_contained(self):
        self.assertEqual(
            [[1, 10]],
            merge_ranges([[3, 4], [1, 10]])
        )


if __name__ == '__main__':
    unittest.main()