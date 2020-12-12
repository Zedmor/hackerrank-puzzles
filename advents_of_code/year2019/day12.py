import itertools


class Moon:
    def __init__(self, *coords):
        self.x, self.y, self.z = coords
        self.dx, self.dy, self.dz = 0, 0, 0

    def __repr__(self):
        return f'Coords: {str((self.x, self.y, self.z))} velocity: {str((self.dx, self.dy, self.dz))}'

    def __eq__(self, other):
        return all((self.x == other.x,
                    self.y == other.y,
                    self.z == other.z,
                    self.dx == other.dx,
                    self.dy == other.dy,
                    self.dz == other.dz))


moons = [Moon(-1, 0, 2), Moon(2, -10, -7), Moon(4, -8, 8), Moon(3, 5, -1)]

moons = [Moon(-7, -1, 6), Moon(6, -9, -9), Moon(-12, 2, -7), Moon(4, -17, -12)]

moons_orig = [Moon(-7, -1, 6), Moon(6, -9, -9), Moon(-12, 2, -7), Moon(4, -17, -12)]

print(moons)


def update_gravity(moon1, moon2):
    for attr in ('x', 'y', 'z'):
        if getattr(moon1, attr) < getattr(moon2, attr):
            delta = 1
        elif getattr(moon1, attr) > getattr(moon2, attr):
            delta = -1
        else:
            delta = 0

        setattr(moon1, 'd' + attr, getattr(moon1, 'd' + attr) + delta)
        setattr(moon2, 'd' + attr, getattr(moon2, 'd' + attr) - delta)


def update_velocities(moons):
    for moon in moons:
        moon.x += moon.dx
        moon.y += moon.dy
        moon.z += moon.dz


def energy(moon):
    return (abs(moon.x) + abs(moon.y) + abs(moon.z)) * (abs(moon.dx) + abs(moon.dy) + abs(moon.dz))


def equal(moons1, moons2):
    return all(m1 == m2 for m1, m2 in zip(moons1, moons2))


counter = 0
while not equal(moons, moons_orig) or counter == 0:
    for pair in itertools.combinations(moons, 2):
        update_gravity(*pair)

    update_velocities(moons)

    counter += 1

print(counter)

# print(sum(energy(moon) for moon in moons))
