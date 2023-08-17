class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        def backtrack(s, wordDict, memo):
            # If the substring is already computed
            if s in memo:
                return memo[s]
            
            res = []
            
            # If the whole string is a word, append it to the result
            if s in wordDict:
                res.append(s)
            
            # Check every substring
            for i in range(1, len(s)):
                # If the prefix is in the word dictionary, we check the rest of the string
                if s[:i] in wordDict:
                    rest = backtrack(s[i:], wordDict, memo)
                    for item in rest:
                        res.append(s[:i] + " " + item)
                        
            # Memorize the computed result for the current substring
            memo[s] = res
            
            return res
        
        return backtrack(s, set(wordDict), {})