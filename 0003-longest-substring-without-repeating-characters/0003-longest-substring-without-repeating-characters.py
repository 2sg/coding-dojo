class Solution(object):
    def lengthOfLongestSubstring(self, s):
        start = max_length = 0
        used_chars = {}

        for i, char in enumerate(s):
            if char in used_chars and start <= used_chars[char]:
                start = used_chars[char] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used_chars[char] = i

        return max_length
