class Solution:
    def maxProduct(self, words: List[str]) -> int:
        max_len = 0
        for i in range(0,len(words)):
            for j in range(i+1,len(words)):
                if set(words[i]).intersection(set(words[j])) == set():
                    max_len= max(max_len,len(words[i])*len(words[j]))
        return max_len
    
