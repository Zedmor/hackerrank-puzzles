from collections import defaultdict
from queue import Queue

import numpy as np
import pytest

k = """16
10
15
5
1
11
7
19
6
12
4"""

l = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

m = """152
18
146
22
28
133
114
67
19
37
66
14
90
163
26
149
71
106
46
143
145
12
151
105
58
130
93
49
74
83
129
122
63
134
86
136
166
169
159
3
178
88
103
97
110
53
125
128
9
15
78
1
50
87
56
89
60
139
113
43
36
118
170
96
135
23
144
153
150
142
95
180
35
179
80
13
115
2
171
32
70
6
72
119
29
79
27
47
107
73
162
172
57
40
48
100
64
59
175
104
156
94
77
65"""

z = """1
2
4
6"""


def solve(s):
    nums = list(map(int, s.split('\n')))

    variants = 1

    target = max(nums) + 3

    nums = sorted([0] + nums + [target])

    print(nums)

    dp = [-1] * len(nums)

    for i in range(len(nums)):
        cursor = i + 1
        while cursor < len(nums) and nums[cursor] - nums[i] <= 3:
            dp[cursor] += 1
            cursor += 1
    dp[0] = 0

    for i in range(len(nums)):
        cursor = i + 1
        while cursor < len(nums) and nums[cursor] - nums[i] <= 3:
            dp[cursor] += dp[i]
            cursor += 1

    return dp[-1] + 1


@pytest.mark.parametrize(
    ('s', 'expected'),
    (
            (m, 19208),
    ),
)
def test(s: str, expected: int) -> None:
    assert solve(s) == expected


