import unittest
from leetcode import ZumaGame488

class Testboard(unittest.TestCase):
    def testClearBoard(self):
        a = ZumaGame488.Board('RBYYYBBRRB')
        a.clearboard()
        self.assertEqual('B', a.getPosition())
        a = ZumaGame488.Board('RRRRR')
        a.clearboard()
        self.assertEqual('', a.getPosition())
        a = ZumaGame488.Board('WWRRRRRW')
        a.clearboard()
        self.assertEqual('', a.getPosition())


    def testInserting(self):
        a = ZumaGame488.Board('RRRRR')
        a.insertMarble('B',0)
        self.assertEqual('B', a.getPosition())
        a.insertMarble('B',1)
        self.assertEqual('BB', a.getPosition())
        a.insertMarble('B', 2)
        self.assertEqual('', a.getPosition())
        a.insertMarble('R', 0)
        self.assertEqual('R', a.getPosition())
    def testFind(self):
        a = ZumaGame488.Board('RRBBWWBBWW')
        self.assertEqual(a.pairIndices('R'), [0])
        self.assertEqual(a.pairIndices('W'), [4, 8])

class TestSolution(unittest.TestCase):
    def test1(self):
        a = ZumaGame488.Solution()
        inp = ("RGGBYRRYWWYYBBGRGG"
, "RRYWG")
        self.assertEqual(a.findMinStep(*inp), 4)

    def test2(self):
        a = ZumaGame488.Solution()
        inp = ( "WWGWGW"
,"GWBWR")
        self.assertEqual(a.findMinStep(*inp), 3)


    def test3(self):
        a = ZumaGame488.Solution()
        inp = (    "RRWWRRW","WWRRR")
        self.assertEqual(a.findMinStep(*inp), 2)



    def test4(self):
        a = ZumaGame488.Solution()
        inp = ("RRWWRRW"
        , "RR")
        self.assertEqual(a.findMinStep(*inp), 2)

    def test5(self):
        a = ZumaGame488.Solution()
        inp = ("WRRBBW", "RB")
        self.assertEqual(a.findMinStep(*inp), -1)
    def test6(self):
        a = ZumaGame488.Solution()
        inp = ("WWRRBBWW", "WRBRW")
        self.assertEqual(a.findMinStep(*inp), 2)
    def test7(self):
        a = ZumaGame488.Solution()
        inp = ("G", "GGGGG")
        self.assertEqual(a.findMinStep(*inp), 2)
    def test8(self):
        a = ZumaGame488.Solution()
        inp = ("RBYYBBRRB", "YRBGB")
        self.assertEqual(a.findMinStep(*inp), 3)
    def test9(self):
        a = ZumaGame488.Solution()
        inp = ("RRWWRRW", "R")
        self.assertEqual(a.findMinStep(*inp), -1)



if __name__ == '__main__':
    unittest.main(verbosity=2)