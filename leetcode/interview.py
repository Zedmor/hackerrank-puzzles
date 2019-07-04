"""
>>> Solution().combinationSum([2, 3, 6, 7], 7)
[
  [7],
  [2,2,3]
]
>>> Solution().combinationSum([2, 3, 5], 8)
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
class Solution:
    def combinationSum(self, nums: list, val: int) -> int:
        all_results = set()
        def recurSum(nums, residual, collected=None):
            if not collected:
                collected = []
            if residual == 0:
                all_results.add(tuple(sorted(collected)))
            elif residual < 0:
                return False
            else:
                for num in nums:
                    new_collected = collected.copy()
                    new_collected.append(num)
                    recurSum(nums, residual - num, new_collected)

        recurSum(set(nums), val)
        all_results = [list(t) for t in all_results]
        return all_results

