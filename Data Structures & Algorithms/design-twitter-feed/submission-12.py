from collections import defaultdict
import heapq 

class Twitter:

    def __init__(self):
        self.followlist = defaultdict(set) #map followee : follower
        self.tweets = defaultdict(list) #for each user it's a list of tweetIds
        self.count = 0 #counter for # of tweets to get a timestamp

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count,tweetId))
        self.count += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        q = []
        #we need the values with the highest countId (i.e. recent ones), so we use a minheap
        for followee in self.followlist[userId]:
            #we need to process all of the tweets from this guy
            if len(self.tweets[followee]) > 10:
                self.tweets[followee] = self.tweets[followee][-10:]
            for count,tweetId in self.tweets[followee]:
                heapq.heappush(q,(count,tweetId))
        for count,tweetId in self.tweets[userId]:
            heapq.heappush(q,(count,tweetId))
        while len(q)>10:
            heapq.heappop(q)
        res = []
        for i in range(len(q)):
            count, tweetId = heapq.heappop(q)
            res.append(tweetId)
        return res[::-1]


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followlist[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followlist[followerId].discard(followeeId)
        
