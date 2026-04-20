class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        output = []

        for idx in range(length):
            current_product = 1
            for other_idx in range(length):
                if other_idx != idx:
                    current_product *= nums[other_idx]
            output.append(current_product)

        return output