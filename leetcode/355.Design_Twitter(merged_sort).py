class Twitter:

    def merge(self, posts, k: int):
        indexes = [-1] * len(posts)
        results = []
        while len(results) < k:
            save_index = 0
            save_value = -1
            for idx, post in enumerate(posts):
                if (indexes[idx] >= -len(post)) and (post[indexes[idx]][0] > save_value):
                    save_value = post[indexes[idx]][0]
                    save_index = idx
            if save_value != -1:
                results.append(posts[save_index][indexes[save_index]][1])
                indexes[save_index] -= 1
            else:
                break
        return results
        
    def __init__(self):
        self.newFeed = {}
        self.followList = {}
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        if not userId in self.newFeed:
            self.newFeed[userId] = []
        self.newFeed[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        candidates = []
        if userId in self.newFeed:
            candidates = [self.newFeed[userId]]
        if userId in self.followList:
            candidates += [self.newFeed.get(item, []) for item in self.followList[userId]]
        return self.merge(candidates, 10)

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
