class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums=sorted(nums)
        for item in nums:
            if nums.count(item) > 1:
                return True
        return False