class Node:
    def __init__(self, data=None):
        self.data: str = data
        self.childs: List['Node'] = []
        self.is_end: bool = False

    def add(self, word: str) -> None:
        if len(word) == 0:
            self.is_end = True
            return
        for child in self.childs:
            if child.data == word[0]:
                child.add(word[1:])
                return
        new_child = Node(word[0])
        self.childs.append(new_child)
        new_child.add(word[1:])
    
    def search(self, word: str):
        if len(word) == 0:
            return True, self.is_end
        
        for child in self.childs:
            if (child.data == word[0]) or (word[0] == '.'):
                found, is_end = child.search(word[1:])
                if found and is_end:
                    return found, is_end
        return False, False

class WordDictionary:

    def __init__(self):
        self.root = Node("root")

    def addWord(self, word: str) -> None:
        self.root.add(word)

    def search(self, word: str) -> bool:
        found, is_end = self.root.search(word)
        return found


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
