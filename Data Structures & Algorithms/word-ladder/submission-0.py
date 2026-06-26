class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or endWord == beginWord:
            return 0

        n = len(beginWord)

        def checkdiff(a, b):
            cnt = 0
            for i in range(len(a)):
                if a[i] != b[i]:
                    cnt += 1
                
                if cnt > 1:
                    return False
            return True

        adjlist = [set() for _ in range(len(wordList))]
        for i in range(len(wordList)):
            for j in range(len(wordList)):
                if checkdiff(wordList[i], wordList[j]):
                    adjlist[i].add(j)
                    adjlist[j].add(i)
        
        visited = set()
        queue = deque()
        for i in range(len(wordList)):
            if checkdiff(beginWord, wordList[i]):
                queue.append((i, 1))
        
        while queue:
            print(queue)
            curr, cnt = queue.popleft()
            if wordList[curr] == endWord:
                return cnt + 1
            
            visited.add(curr)
            for n in adjlist[curr]:
                if n in visited:
                    continue
                queue.append( (n, cnt + 1) )
        
        return 0



        
            



