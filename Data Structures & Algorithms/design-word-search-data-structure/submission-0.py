class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = Node()
            curr = curr.children[ch]
        curr.end = True

    def search(self, word: str) -> bool:
        
        def backtrack(idx, root):
            curr = root
            
            for i in range(idx, len(word)):
                if word[i] != '.':
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
                else:
                    for child in curr.children.values():
                        if backtrack(i+1, child):
                            return True
                    return False
            return curr.end

    
        return backtrack(0, self.root)


        
class Node():

    def __init__(self):
        self.children = {}
        self.end = False
