class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        def backtrack(path, t):
            if path:  
                result.add(path)
            for i in range(len(t)):
                backtrack(path + t[i], t[:i] + t[i+1:])
                
        result = set()
        backtrack("", tiles)
        return len(result)
