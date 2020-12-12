#
# @lc app=leetcode id=1105 lang=python3
#
# [1105] Filling Bookcase Shelves
#
# https://leetcode.com/problems/filling-bookcase-shelves/description/
#
# algorithms
# Medium (57.91%)
# Total Accepted:    17K
# Total Submissions: 29.3K
# Testcase Example:  '[[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]]\n4'
#
# We have a sequence of books: the i-th Book has thickness books[i][0] and
# height books[i][1].
#
# We want to place these books in order onto bookcase shelves that have total
# width shelf_width.
#
# We choose some of the books to place on this shelf (such that the sum of
# their thickness is <= shelf_width), then build another level of shelf of the
# bookcase so that the total height of the bookcase has increased by the
# maximum height of the books we just put down.  We repeat this process until
# there are no more books to place.
#
# Note again that at each step of the above process, the order of the books we
# place is the same order as the given sequence of books.  For example, if we
# have an ordered list of 5 books, we might place the first and second Book
# onto the first shelf, the third Book on the second shelf, and the fourth and
# fifth Book on the last shelf.
#
# Return the minimum possible height that the total bookshelf can be after
# placing shelves in this manner.
#
#
# Example 1:
#
#
# Input: books = [[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], shelf_width = 4
# Output: 6
# Explanation:
# The sum of the heights of the 3 shelves are 1 + 3 + 2 = 6.
# Notice that Book number 2 does not have to be on the first shelf.
#
#
#
# Constraints:
#
#
# 1 <= books.length <= 1000
# 1 <= books[i][0] <= shelf_width <= 1000
# 1 <= books[i][1] <= 1000
#
#
#
from collections import namedtuple
from copy import deepcopy
from functools import lru_cache
from typing import List

Book = namedtuple('Book', ('width', 'height'))


def to_tuple(lst):
    return tuple(to_tuple(i) if isinstance(i, list) else i for i in lst)


def to_list(tup):
    return list(to_list(i) if (isinstance(i, tuple) and not isinstance(i, Book)) else i for i in tup)


class Solution:
    """
    >>> Solution().minHeightShelves([[11,83],[170,4],[93,80],[155,163],[134,118],[75,14],[122,192],[123,154],[187,29],[160,64],[170,152],[113,179],[60,102],[28,187],[59,95],[187,97],[49,193],[67,126],[75,45],[130,160],[4,102],[116,171],[43,170],[96,188],[54,15],[167,183],[58,158],[59,55],[148,183],[89,95],[90,113],[51,49],[91,28],[172,103],[173,3],[131,78],[11,199],[77,200],[58,65],[77,30],[157,58],[18,194],[101,148],[22,197],[76,181],[21,176],[50,45],[80,174],[116,198],[138,9],[58,125],[163,102],[133,175],[21,39],[141,156],[34,185],[14,113],[11,34],[35,184],[16,132],[78,147],[85,170],[32,149],[46,94],[196,3],[155,90],[9,114],[117,119],[17,157],[94,178],[53,55],[103,142],[70,121],[9,141],[16,170],[92,137],[157,30],[94,82],[144,149],[128,160],[8,147],[153,198],[12,22],[140,68],[64,172],[86,63],[66,158],[23,15],[120,99],[27,165],[79,174],[46,19],[60,98],[160,172],[128,184],[63,172],[135,54],[40,4],[102,171],[29,125],[81,9],[111,197],[16,90],[22,150],[168,126],[187,61],[47,190],[54,110],[106,102],[55,47],[117,134],[33,107],[2,10],[18,62],[109,188],[113,37],[59,159],[120,175],[17,147],[112,195],[177,53],[148,173],[29,105],[196,32],[123,51],[29,19],[161,178],[148,2],[70,124],[126,9],[105,87],[41,121],[147,10],[78,167],[91,197],[22,98],[73,33],[148,194],[166,64],[33,138],[139,158],[160,19],[140,27],[103,109],[88,16],[99,181],[2,140],[50,188],[200,77],[73,84],[159,130],[115,199],[152,79],[1,172],[124,136],[117,138],[158,86],[193,150],[56,57],[150,133],[52,186],[21,145],[127,97],[108,110],[174,44],[199,169],[139,200],[66,48],[52,190],[27,86],[142,191],[191,79],[126,114],[125,100],[176,95],[104,79],[146,189],[144,78],[52,106],[74,74],[163,128],[34,181],[20,178],[15,107],[105,8],[66,142],[39,126],[95,59],[164,69],[138,18],[110,145],[128,200],[149,150],[149,93],[145,140],[90,170],[81,127],[57,151],[167,127],[95,89]], 200)
    15672

    >>> Solution().minHeightShelves([[1,1],[2,3],[2,3],[1,1],[1,1],[1,1],[1,2]], 4)
    6

    """
    def result_height(self, r):
        return sum([max(sublist, key=lambda book: book.height).height for sublist in r])

    def shelve_width(self, shelf):
        return sum([book.width for book in shelf])

    def minHeightShelves(self, books: List[List[int]], shelf_width: int) -> int:
        books = tuple(Book(*b) for b in books)

        @lru_cache(maxsize=2000)
        def recur(solution, unassigned_books):

            solution = to_list(solution)
            if not unassigned_books:
                result = self.result_height(solution)
                return result, solution
            possible_solutions = []
            # if width of last solution is allow to add book we can add it to last shelf
            variant = deepcopy(solution)
            variant[-1].append(unassigned_books[0])
            if self.shelve_width(variant[-1]) <= shelf_width:
                possible_solutions.append(variant)
            # Starting new shelf is always an option if there's books on last shelf
            if solution[-1]:
                variant = deepcopy(solution)
                variant.append([unassigned_books[0]])
                possible_solutions.append(variant)
            if not possible_solutions:
                return float('inf')
            return min(recur(to_tuple(variant), unassigned_books[1:]) for variant in possible_solutions)
        best_solution = (tuple(),)
        left_pointer = 0
        pointer = 1
        while pointer < len(books):
            pointer = 0
            solution = recur(to_tuple(best_solution), books[left_pointer:pointer])
            if len(solution[1]) > 2:
                best_solution = solution[1][:-2]
                left_pointer = sum([len(sublist) for sublist in best_solution])
            print(solution[0])
        return solution[0]
