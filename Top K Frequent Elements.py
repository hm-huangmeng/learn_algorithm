from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [i[0] for i in Counter(nums).most_common(k)]


if __name__ == '__main__':
    # nums = [1, 1, 1, 2, 2, 3]
    # k = 2
    nums = [1]
    k = 1
    obj = Solution()
    print(obj.topKFrequent(nums, k))