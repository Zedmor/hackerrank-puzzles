from collections import defaultdict


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None
        self.count = 0

    def __repr__(self):
        return f'{self.val}'

class Game:
    def __init__(self):
        self.all_values = set()
        self.current = None
        self.count = 0

    def __repr__(self):
        repr = '(' + self.current.__repr__() + ')'
        cursor = self.current.next
        while cursor != self.current:
            repr = repr + ' -> ' + cursor.__repr__()
            cursor = cursor.next
        return repr


    def add(self):
        result = 0
        if not self.current:
            self.current = Node(self.count)
            self.current.next = self.current
            self.current.prev = self.current
            self.all_values.add(self.count)
        else:
            self.count += 1
            if self.count % 23 == 0:
                result += self.count
                cursor = self.current
                for i in range(7):
                    cursor = cursor.prev
                result += cursor.val
                cursor.prev.next = cursor.next
                cursor.next.prev = cursor.prev
                self.current = cursor.next
                self.all_values.remove(cursor.val)
                return result, cursor.val
            else:
                insert_point = self.current.next
                next_point = self.current.next.next
                new_marble = Node(self.count)
                self.all_values.add(self.count)
                insert_point.next = new_marble
                next_point.prev = new_marble
                new_marble.next = next_point
                new_marble.prev = insert_point
                self.current = new_marble
        return 0,0

    def is_present(self, val):
        return val in self.all_values





game = Game()

results = defaultdict(int)

for t in range(30000):
    for i in range(405):
        result = game.add()
        results[i] += result[0]
    # for k,v in results.items():
    #     if v == 146373:
    #         print('result found')
    #         print(game)
    #         print(results, result)
    #         exit(0)
        if game.is_present(7170000):
            print('marble found')
            print(max(results.values()))
            exit(0)



# print(game)
