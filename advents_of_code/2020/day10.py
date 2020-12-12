from copy import copy
from queue import Queue

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

nums = list(map(int, z.split('\n')))

target = max(nums) + 3

state = ([0], sorted(nums) + [target])

q = Queue()
q.put(state)

cnt = 0

while not q.empty():
    # print(q.qsize())
    chain, bag = q.get()
    if chain[-1] == target:
        cnt += 1
        print(chain)
        diff_1 = sum([1 for a,b in zip(chain, chain[1:]) if b - a == 1])
        diff_2 = sum([1 for a,b in zip(chain, chain[1:]) if b - a == 3])

    for n in bag:
        new_bag = copy(bag)

        if n > chain[-1] + 3:
            break
        if n < chain[-1] + 1:
            new_bag.remove(n)
            continue

        new_bag.remove(n)
        new_state = (chain + [n], new_bag)
        q.put(new_state)

print(cnt)
