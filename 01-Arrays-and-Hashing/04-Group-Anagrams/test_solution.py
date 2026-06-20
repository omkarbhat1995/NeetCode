import pytest
from solution import Solution

class TestGroupAnagrams:
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.solver = Solution()

    @pytest.mark.parametrize("strs, expected", [
        # --- Standard LeetCode Examples ---
        (["act", "pots", "tops", "cat", "stop", "hat"], 
         [["hat"], ["act", "cat"], ["stop", "pots", "tops"]]),
        (["x"], [["x"]]),
        ([""], [[""]]),
        
        # --- Length and Empty Edge Cases ---
        (["", "", ""], [["", "", ""]]),                               # Multiple empty strings
        (["a", "b", "c"], [["a"], ["b"], ["c"]]),                     # Single distinct characters
        (["a", "a", "a"], [["a", "a", "a"]]),                         # Single identical characters
        
        # --- Structural Edge Cases ---
        (["ab", "ba", "abc", "cba", "bca", "d"], 
         [["ab", "ba"], ["abc", "cba", "bca"], ["d"]]),               # Mixed group sizes
        (["hello", "llohe", "world", "dlrow"], 
         [["hello", "llohe"], ["world", "dlrow"]]),                   # Multi-letter distinct groups
        (["abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"], 
         [["abcdefghijklmnopqrstuvwxyz", "zyxwvutsrqponmlkjihgfedcba"]]), # Full alphabet
        
        # --- Value Edge Cases ---
        (["eat", "tea", "tan", "ate", "nat", "bat"], 
         [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),           # Classic LeetCode blind 75 case
        (["ddddddg", "dgggggg"], [["ddddddg"], ["dgggggg"]])          # Similar character counts but distinct
    ])
    def test_groupAnagrams(self, strs, expected):
        result = self.solver.groupAnagrams(strs)
        
        # Since output order doesn't matter, we must sort the inner and outer lists 
        # to ensure a deterministic and stable comparison.
        sorted_result = sorted([sorted(group) for group in result])
        sorted_expected = sorted([sorted(group) for group in expected])
        
        assert sorted_result == sorted_expected

    # --- Isolated Constraint Edge Cases ---
    
    def test_groupAnagrams_max_length_strings(self):
        # 10 strings of exactly 100 'a's, and 1 string of 100 'b's
        strs = ["a" * 100 for _ in range(10)] + ["b" * 100]
        expected = [["a" * 100 for _ in range(10)], ["b" * 100]]
        
        result = self.solver.groupAnagrams(strs)
        sorted_result = sorted([sorted(group) for group in result])
        sorted_expected = sorted([sorted(group) for group in expected])
        
        assert sorted_result == sorted_expected

    def test_groupAnagrams_max_array_size(self):
        # Array of 1000 single character strings ('a' and 'b' alternating)
        strs = ["a" if i % 2 == 0 else "b" for i in range(1000)]
        expected = [["a"] * 500, ["b"] * 500]
        
        result = self.solver.groupAnagrams(strs)
        sorted_result = sorted([sorted(group) for group in result])
        sorted_expected = sorted([sorted(group) for group in expected])
        
        assert sorted_result == sorted_expected