class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx_fast = 0
        idx_slow = 0
        for num in nums:
            if nums[idx_fast] != nums[idx_slow]:
                idx_slow += 1
                nums[idx_slow] = nums[idx_fast]
            idx_fast += 1
        return idx_slow + 1
		