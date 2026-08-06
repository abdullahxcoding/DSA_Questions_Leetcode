class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = {0: -1}  
        count = 0
        ans = 0

        for i, num in enumerate(nums):
            if num == 1:
                count += 1
            else:
                count -= 1

            if count in prefix:
                ans = max(ans, i - prefix[count])
            else:
                prefix[count] = i

        return ans