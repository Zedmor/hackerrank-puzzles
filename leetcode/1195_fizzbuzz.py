from concurrent.futures.thread import ThreadPoolExecutor

fizz = lambda n: n % 3 == 0
buzz = lambda n: n % 5 == 0
fizzbuzz = lambda n: n % 3 == 0 and n % 5 == 0
check_n = lambda n: n % 3 != 0 and n % 5 != 0

class FizzBuzz:
    def __init__(self, n: int):
        self.cursor = 1
        self.n = n
        self.lock = False

    def executor_factory(self, clause, callable, blockers):
        def implementation():
            while self.cursor <= self.n:
                if clause(self.cursor) and not any([b(self.cursor) for b in blockers]) and self.cursor <= self.n:
                    callable(self.cursor)
                    self.cursor += 1
        return implementation

    def fizz(self, printFizz: 'Callable[[], None]') -> None:
        blockers = [fizzbuzz]
        self.executor_factory(fizz, lambda n: printFizz(), blockers)()

    def buzz(self, printBuzz: 'Callable[[], None]') -> None:
        blockers = [fizzbuzz]
        self.executor_factory(buzz, lambda n: printBuzz(), blockers)()

    def fizzbuzz(self, printFizzBuzz: 'Callable[[], None]') -> None:
        blockers = []
        self.executor_factory(fizzbuzz, lambda n: printFizzBuzz(), blockers)()

    def number(self, printNumber: 'Callable[[int], None]') -> None:
        blockers = [fizz, buzz, fizzbuzz]
        self.executor_factory(check_n, printNumber, blockers)()


result = []

o = FizzBuzz(15)

executor = ThreadPoolExecutor(4)

executor.submit(o.fizz, (lambda: result.append('fizz')))
executor.submit(o.buzz, (lambda: result.append('buzz')))
executor.submit(o.fizzbuzz, (lambda: result.append('fizzbuzz')))
executor.submit(o.number, (lambda num: result.append(num)))
executor.shutdown()

print(result)

assert result == [1, 2, "fizz", 4, "buzz", "fizz", 7, 8, "fizz", "buzz", 11, "fizz", 13, 14, "fizzbuzz"]

