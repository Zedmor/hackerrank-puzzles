"""
135Candy.py
There are N children standing in a line. Each child is assigned a rating value.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
What is the minimum candies you must give?
"""
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        candies = [1]*len(ratings)
        while sum(ratings)>0:
            num0 = ratings.count(0)
            while num0 == ratings.count(0):
                ratings = [x -1 if x> 1 else 0 for x in ratings]
            for i,v in enumerate(ratings):
                if v>0:
                    candies[i]+=1

        return sum(candies)


ratings = [1,2,2]
a = Solution()
print(a.candy(ratings))