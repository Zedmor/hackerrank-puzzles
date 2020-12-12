from pytest import fixture

from advents_of_code.year2019.day18.day18 import Game
from advents_of_code.year2019.day18.day18_2 import Game as Game2


def sanitize(vault):
    return [i.strip() for i in vault.split('\n') if i.strip()]


def test_full_run():
    vault = """
    #########
    #b.A.@.a#
    #########
    """
    game = Game(sanitize(vault))

    assert game.solve() == 8


def test_full_run2():
    vault = """
    ########################
    #f.D.E.e.C.b.A.@.a.B.c.#
    ######################.#
    #d.....................#
    ########################
    """
    game = Game(sanitize(vault))

    assert game.solve() == 86


def test_full_run3():
    vault = """
    ########################
    #...............b.C.D.f#
    #.######################
    #.....@.a.B.c.d.A.e.F.g#
    ########################
    """
    game = Game(sanitize(vault))

    assert game.solve() == 132


def test_full_run5():
    vault = """
    #################
    #i.G..c...e..H.p#
    ########.########
    #j.A..b...f..D.o#
    ########@########
    #k.E..a...g..B.n#
    ########.########
    #l.F..d...h..C.m#
    #################
    """
    game = Game(sanitize(vault))

    assert game.heros == (4, 8)

    assert game.solve() == 136


def test_full_run4():
    vault = """
    ########################
    #@..............ac.GI.b#
    ###d#e#f################
    ###A#B#C################
    ###g#h#i################
    ########################
    """
    game = Game(sanitize(vault))

    assert game.solve() == 81


def test_full_run4():
    vault = """
    #############
    #g#f.D#..h#l#
    #F###e#E###.#
    #dCba@#@BcIJ#
    #############
    #nK.L@#@G...#
    #M###N#H###.#
    #o#m..#i#jk.#
    #############
    """
    game = Game2(sanitize(vault))

    assert game.solve() == 72


def test_full_run5():
    vault = """
    #######
    #a.#Cd#
    ##@#@##
    #######
    ##@#@##
    #cB#Ab#
    #######    
    """
    game = Game2(sanitize(vault))

    assert game.solve() == 8


def test_full_run6():
    vault = """
    ###############
    #d.ABC.#.....a#
    ######@#@######
    ###############
    ######@#@######
    #b.....#.....c#
    ###############  
    """
    game = Game2(sanitize(vault))

    assert game.solve() == 24


def test_full_run7():
    vault = """
    #############
    #DcBa.#.GhKl#
    #.###@#@#I###
    #e#d#####j#k#
    ###C#@#@###J#
    #fEbA.#.FgHi#
    #############
    """
    game = Game2(sanitize(vault))

    assert game.solve() == 32


def get_vault():
    with open('day18.txt') as f:
        lab = f.read().splitlines()

    return lab


def test_real_run():
    vault = get_vault()
    game = Game2(vault)
    assert game.solve() == 8
