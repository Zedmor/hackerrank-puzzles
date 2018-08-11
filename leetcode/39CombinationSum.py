"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.

"""


class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(candidates)
        all_paths = set()
        def recur_search(target, path=[]):
            if target == 0:
                all_paths.add(tuple(sorted(path)))
                return
            for cadidate in candidates:
                if cadidate > target:
                    break
                else:
                    recur_search(target - cadidate, path + [cadidate])

        recur_search(target)
        all_paths = [list(e) for e in all_paths]
        return all_paths


def test_example1():
    candidates = [2, 3, 6, 7]
    target = 7
    assert [
               [7],
               [2, 2, 3]
           ] == Solution().combinationSum(candidates, target)


def test_example2():
    candidates = [2, 3, 5]
    target = 8
    assert [
               [2, 2, 2, 2],
               [2, 3, 3],
               [3, 5]
           ] == Solution().combinationSum(candidates, target)
