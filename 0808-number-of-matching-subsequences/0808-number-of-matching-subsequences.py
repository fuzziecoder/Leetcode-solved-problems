from collections import defaultdict
import bisect

class Solution(object):
    def numMatchingSubseq(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: int
        """
        # Step 1: Preprocess `s` to store indices of each character
        char_indices = defaultdict(list)
        for index, char in enumerate(s):
            char_indices[char].append(index)
        
        def is_subsequence(word):
            """Check if word is a subsequence of s using binary search"""
            prev_index = -1
            for char in word:
                if char not in char_indices:
                    return False
                
                # Find the smallest index in s that is greater than prev_index
                idx_list = char_indices[char]
                pos = bisect.bisect_left(idx_list, prev_index + 1)
                
                if pos == len(idx_list):  # No valid position found
                    return False
                
                prev_index = idx_list[pos]  # Move to the next index
            
            return True
        
        # Step 2: Count the number of words that are subsequences of s
        return sum(1 for word in words if is_subsequence(word))
