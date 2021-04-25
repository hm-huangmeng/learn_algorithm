from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return False
        end_reachable = len(nums) - 1
        for idx in range(len(nums) - 1, -1, -1):
            if nums[idx] + idx >= end_reachable:
                end_reachable = idx
        return True if 0 == end_reachable else False


if __name__ == '__main__':
    nums = [2, 3, 1, 1, 4]
    #nums = [3, 2, 1, 0, 4]
    obj = Solution()
    print(obj.canJump(nums))
