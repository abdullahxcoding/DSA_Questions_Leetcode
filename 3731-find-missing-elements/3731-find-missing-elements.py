class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        largest=smallest = nums[0]
        result = []
        for i in nums: 
            if i > largest: 
                largest= i
            elif i < smallest:
                smallest = i

        for j in range(smallest,largest):
            if j not in nums: 
                result.append(j)

        return result
