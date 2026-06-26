class Twitter:

    def __init__(self):
        self.posts = []
        self.users = set()
        self.adj = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users.add(userId)
            self.adj[userId] = set()
            self.adj[userId].add(userId)

        self.posts.append( (userId, tweetId) )

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        feed = []

        idx = len(self.posts) - 1
        while len(feed) < 10 and idx >= 0:
            user, tweet = self.posts[idx]
            if user in self.adj[userId]:
                feed.append(tweet)
            idx -= 1
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users.add(followerId)
            self.adj[followerId] = set()
        if followeeId not in self.users:
            self.users.add(followeeId)
            self.adj[followeeId] = set()
        self.adj[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users.add(followerId)
            self.adj[followerId] = set()
        if followeeId not in self.users:
            self.users.add(followeeId)
            self.adj[followeeId] = set()
        if followerId == followeeId or followeeId not in self.adj[followerId]:
            return
        
        self.adj[followerId].remove(followeeId)
        
