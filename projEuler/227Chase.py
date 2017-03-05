import matplotlib.pyplot as plt
import random
positions = []
for j in range(10000):

    position = 50
    for i in range(10000):
        r = random.randint(1,6)
        if r == 1:
            position-=1
        if r == 6:
            position+=1
        if position == 100:
            position = 0
        if position == -1:
            position = 99
    positions.append(position)

plt.hist(positions, 49)
plt.show()