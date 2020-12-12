def get_fuel_mass(mass):
    return mass//3 - 2

def total_fuel_mass(mass):
    total_mass = 0
    fuel_mass = get_fuel_mass(mass)

    while fuel_mass > 0:
        total_mass += fuel_mass
        fuel_mass = get_fuel_mass(fuel_mass)
    return total_mass


def main():
    with open('day1.txt') as inp:
        print(sum(total_fuel_mass(int(line)) for line in inp))

if __name__ == '__main__':
    main()
