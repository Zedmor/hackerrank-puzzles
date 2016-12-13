import logging
import unittest
import sys
from io import StringIO
out = StringIO()


import stocks


class StocksTest(unittest.TestCase):
    def setUp(self):
        self.output = StringIO()
        self.saved_stdout = sys.stdout
        sys.stdout = self.output
    def tearDown(self):
        self.output.close()
        sys.stdout = self.saved_stdout

    def testYourScript(self):
        frm = open('stockstest.txt', 'r')
        stocks.main(frm)
        log = logging.getLogger("SomeTest.testSomething")
        log.level = logging.DEBUG
        stream_handler = logging.StreamHandler(self.saved_stdout)
        log.addHandler(stream_handler)
        log.debug("aaaaa")
        log.debug(self.output.getvalue())
        #assert self.output.getvalue() == "My expected ouput"
        #print(self.output.getvalue())
        frm.close()


if __name__ == '__main__':

    unittest.main()
