class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or endWord == beginWord:
            return 0

        wordset = set(wordList)
        chars = 'qwertyuiopasdfghjklzxcvbnm'

        def getneighbors(word):
            neighbors = []
            for i in range(len(word)):
                for c in chars:
                    if c == word[i]:
                        continue
                    newword = word[:i] + c + word[i+1:]
                    if newword in wordset:
                        neighbors.append(newword)
            return neighbors
        

        visited = {beginWord}
        queue = deque()
        for n in getneighbors(beginWord):
            queue.append((n, 2))
            visited.add(n)
        
        while queue:
            curr, cnt = queue.popleft()
            if curr == endWord:
                return cnt
        
            for n in getneighbors(curr):
                if n not in visited:
                    visited.add(n)
                    queue.append( (n, cnt + 1) )
        
        return 0



        
            



