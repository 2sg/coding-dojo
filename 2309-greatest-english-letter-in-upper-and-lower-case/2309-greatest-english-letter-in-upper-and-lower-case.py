class Solution:
    def greatestLetter(self, s: str) -> str:
        upper_set = set()
        lower_set = set()
        
        for char in s:
            if char.isupper():
                upper_set.add(char)
            else:
                lower_set.add(char.upper())  

        for char in reversed("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            if char in upper_set and char in lower_set:
                return char
        return ""
