#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
# https://leetcode.com/problems/design-twitter/description/
#
# algorithms
# Medium (30.72%)
# Total Accepted:    57.3K
# Total Submissions: 186.2K
# Testcase Example:  '["Twitter","postTweet","getNewsFeed","follow","postTweet","getNewsFeed","unfollow","getNewsFeed"]\n' +'[[],[1,5],[1],[1,2],[2,6],[1],[1,2],[1]]'
#
# Design a simplified version of Twitter where users can post tweets,
# follow/unfollow another user and is able to see the 10 most recent tweets in
# the user's news feed. Your design should support the following methods:
#
#
#
# postTweet(userId, tweetId): Compose a new tweet.
# getNewsFeed(userId): Retrieve the 10 most recent tweet ids in the user's news
# feed. Each item in the news feed must be posted by users who the user
# followed or by the user herself. Tweets must be ordered from most recent to
# least recent.
# follow(followerId, followeeId): Follower follows a followee.
# unfollow(followerId, followeeId): Follower unfollows a followee.
#
#
#
# Example:
#
# Twitter twitter = new Twitter();
#
# // User 1 posts a new tweet (id = 5).
# twitter.postTweet(1, 5);
#
# // User 1's news feed should return a list with 1 tweet id -> [5].
# twitter.getNewsFeed(1);
#
# // User 1 follows user 2.
# twitter.follow(1, 2);
#
# // User 2 posts a new tweet (id = 6).
# twitter.postTweet(2, 6);
#
# // User 1's news feed should return a list with 2 tweet ids -> [6, 5].
# // Tweet id 6 should precede tweet id 5 because it is posted after tweet id
# 5.
# twitter.getNewsFeed(1);
#
# // User 1 unfollows user 2.
# twitter.unfollow(1, 2);
#
# // User 1's news feed should return a list with 1 tweet id -> [5],
# // since user 1 is no longer following user 2.
# twitter.getNewsFeed(1);
#
#
#
from bisect import insort
from collections import namedtuple
from typing import List, Dict, Set

Tweet = namedtuple('Tweet', ('time', 'tweet', 'author'))


class User:
    def __init__(self):
        self.tweets: List[Tweet] = []
        self.feed: List[Tweet] = []
        self.followers: Set[User] = set()


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.users: Dict[int, User] = {}
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        user = self.users.setdefault(userId, User())
        tweet = Tweet(self.timer, tweetId, user)
        user.tweets.append(tweet)
        if user not in user.followers:
            user.feed.append(tweet)
        for u in user.followers:
            u.feed.append(tweet)

        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        return list(reversed([tweet.tweet for tweet in self.users.setdefault(userId, User()).feed[-10:]]))

    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        follower = self.users.setdefault(followerId, User())
        followee = self.users.setdefault(followeeId, User())
        if follower not in followee.followers:
            followee.followers.add(follower)
            if followee != follower:
                for tweet in followee.tweets:
                    insort(follower.feed, tweet)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        follower = self.users.setdefault(followerId, User())
        followee = self.users.setdefault(followeeId, User())
        if follower in followee.followers:
            followee.followers.remove(follower)
            i = 0
            while i < len(follower.feed):
                if follower.feed[i].author == followee and follower != followee:
                    follower.feed.pop(i)
                else:
                    i += 1
