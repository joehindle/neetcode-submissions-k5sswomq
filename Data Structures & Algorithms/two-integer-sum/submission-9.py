class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num1 in enumerate(nums):
            for i in range(index+1, len(nums)):
                num2=nums[i]
                if num1 + num2 == target:
                    return [index, i]
        return []