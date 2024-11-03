class Twitter:

    def __init__(self):
        self.newFeed = []
        self.followList = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.newFeed.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        for (uId, itemID) in self.newFeed[::-1]:
            if (userId in self.followList and uId in self.followList[userId]) or (uId == userId):
                feed.append(itemID)
                if len(feed) == 10:
                    break
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if not (followerId in self.followList):
            self.followList[followerId] = set()
        self.followList[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if not followerId in self.followList:
            return
        self.followList[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
