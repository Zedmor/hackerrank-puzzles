import csv

import random
import time

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y %I:%M %p', prop)

games = ["Pac-Man",
         "Space Invaders",
         "Donkey Kong",
         "Ms. Pac-Man",
         "Asteroids",
         "Defender",
         "Centipede",
         "Galaxian",
         "Donkey Kong Jr.",
         "Mr. Do!",
         "Tempest",
         "Q*bert",
         "Robotron: 2084",
         "Dig Dug",
         "Pole Position",
         "Popeye",
         "Missile Command",
         "Jungle Hunt",
         "Dragon's Lair",
         "Berzerk",
         "Scramble",
         "Battlezone",
         "Stargate",
         "Star Wars",
         "Super Cobra",
         "Space Duel"]

fieldnames = ['datetime_of_sale', 'game1', 'units_sold1', 'game2', 'units_sold2', 'on_sale']

with open("Games_Sale.csv", 'w') as games_file:
    writer = csv.DictWriter(games_file, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(500):
        item = {
            'datetime_of_sale': randomDate("1/1/1983 1:30 PM", "1/1/1985 4:50 AM", random.random()),
            'game1': random.choice(games),
            'units_sold1': random.randint(1, 50),
            'game2': random.choice(games),
            'units_sold2': random.randint(1, 50),
            'on_sale': 'OS' if random.randint(1, 3) == 1 else ''
        }
        writer.writerow(item)
