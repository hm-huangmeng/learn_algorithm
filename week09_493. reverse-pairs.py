from typing import List


class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return 0
        count = [0]

        def merge(nums):
            if len(nums) <= 1:
                return nums

            left, right = merge(nums[:len(nums) // 2]), merge(nums[len(nums) // 2:])
            l = r = 0

            while l < len(left) and r < len(right):
                if left[l] <= 2 * right[r]:
                    l += 1
                else:
                    count[0] += len(left) - l
                    r += 1
            return sorted(left + right)

        merge(nums)
        return count[0]


if __name__ == "__main__":
    obj = Solution()
    # nums = [1, 3, 2, 3, 1]
    nums = [2, 4, 3, 5, 1]
    print(obj.reversePairs(nums))
