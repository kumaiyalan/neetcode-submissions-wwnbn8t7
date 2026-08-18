class Twitter:

    def __init__(self):
        self.tweets = []
        self.follows = {}
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.append((userId, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        newsFeed = []
        i = len(self.tweets) - 1
        while len(newsFeed) < 10 and i >= 0:
            addition = self.tweets[i]
            if (userId in self.follows and addition[0] in self.follows[userId]) or addition[0] == userId:
                newsFeed.append(addition[1])
            i -= 1
        return newsFeed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)