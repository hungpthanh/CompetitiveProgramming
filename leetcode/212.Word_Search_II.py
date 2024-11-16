class Node:
    def __init__(self, data=None):
        self.data: str = data
        self.childs: List['Node'] = []
        self.is_end = False
        self.parent = None

    def add_word(self, word: str) -> None:
        if len(word) == 0:
            self.is_end = True
            return
        for child in self.childs:
            if child.data == word[0]:
                child.add_word(word[1:])
                return
        new_child = Node(word[0])
        new_child.parent = self
        self.childs.append(new_child)
        new_child.add_word(word[1:])

    def delete(node):
        parent = node.parent
        if parent:
            while (len(parent.childs)) < 2:
                parent.childs.remove(node)
                node = None
                delete(parent)

    def search(self, word: str) -> bool:
        if not word:
            return True, self.is_end
        for child in self.childs:
            if child.data ==  word[0]:
                found, is_end = child.search(word[1:])
                return found, is_end
        return False, False

    def search_char(self, c: str) -> bool:
        for child in self.childs:
            if child.data ==  c:
                return child
        return None



class Solution:

    def build_multiple_tree(self, board: List[List[str]], words) -> None:
        query_trie = Node("root")
        for word in words:
            query_trie.add_word(word)
        # print(query_trie)
        m = len(board)
        n = len(board[0])
        mark = [[False] * n for _ in range(m)]
        cx = [-1, 1, 0, 0]
        cy = [0, 0, -1, 1]
        results = set()
        tmp = []
        def dfs(i: int, j: int, cnt: int, node) -> None:
            nonlocal tmp            
            cnt += 1
            if cnt > 10:
                return
            if node.is_end:
                results.add("".join(tmp))
            # next_child, is_end = query_trie.search(board[i][j])
            
            # if not next_child and is_end:
            #     results.append(ss)

            for k in range(4):
                x = i + cx[k]
                y = j + cy[k]
                if not ((0 <= x < m) and (0 <= y < n)):
                    continue
                if mark[x][y]:
                    continue
                next_node = node.search_char(board[x][y])
                if next_node:
                    mark[x][y] = True
                    tmp.append(board[x][y])
                    dfs(x, y, cnt, next_node)
                    mark[x][y] = False
                    tmp = tmp[:-1]
        mark = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                next_node = query_trie.search_char(board[i][j])
                if next_node:
                    mark[i][j] = True
                    tmp.append(board[i][j])
                    dfs(i, j, 0, next_node)    
                    tmp = []
                    mark[i][j] = False
        return results

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        results = list(self.build_multiple_tree(board, words))
        return results
