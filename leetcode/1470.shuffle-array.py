"""
# >>> Solution().shuffle([1,2,3,4,4,3,2,1], 4)
# [1, 4, 2, 3, 3, 2, 4, 1]
#
# >>> Solution().shuffle([[1,1,2,2], 2)
# [1, 2, 1, 2]

# >>> Solution().shuffle([2,5,1,3,4,7], 3)
# [2, 3, 5, 4, 1, 7]
"""
from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for x in range(n):
            print('x=', x, end=' ')
            # print(nums[x])
            result.append(nums[x])
            result.append(nums[x + n])
            print('result = ', result)

        return result

# Solution().shuffle([2,5,1,3,4,7], 3)

"""
0.
[2,5,1,3,4,7] <- nums

[] <-- result

1.

[2,5,1,3,4,7]

[2] <-- result

2.

[2,5,1,3,4,7]

[2,3]

3.

[2,5,1,3,4,7]

[2,3,5]

4.

[2,5,1,3,4,7]

[2,3,5,4]
"""
