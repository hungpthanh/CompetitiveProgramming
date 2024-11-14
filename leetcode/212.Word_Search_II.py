class Node:
    def __init__(self, data=None):
        self.data: str = data
        self.childs: List['Node'] = []

    def add(self, c: str):
        for child in self.childs:
            if child.data == c:
                return child
        new_child = Node(c)
        self.childs.append(new_child)
        return new_child

    def search(self, word: str) -> bool:
        if not word:
            return True
        for child in self.childs:
            if child.data == word[0]:
                found = child.search(word[1:])
                return found
        return False

    def __str__(self, level=0) -> str:
        result = "  " * level + (self.data if self.data else "Root") + ("\n" if level else "")
        for child in self.childs:
            result += child.__str__(level + 1)
        return result

class Solution:

    def build_multiple_tree(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])
        M = {}
        mark = [[False] * n for _ in range(m)]
        cx = [-1, 1, 0, 0]
        cy = [0, 0, -1, 1]
        # ss = ""
        # built_words = []
        def dfs(i: int, j: int, node: 'Node', cnt: int) -> None:
            cnt += 1
            if cnt > 10:
                # built_words.append(ss)
                return
            next_node = node.add(board[i][j])
            for k in range(4):
                x = i + cx[k]
                y = j + cy[k]
                if (0 <= x < m) and (0 <= y < n) and (not mark[x][y]):
                    mark[x][y] = True
                    # ss = ss + board[x][y]
                    dfs(x, y, next_node, cnt)
                    # ss = ss[0:-1]
                    mark[x][y] = False
        mark = [[False] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                mark[i][j] = True
                M[(i, j)] = Node("root")
                dfs(i, j, M[(i, j)], 0)
                mark[i][j] = False
        return M

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        M = self.build_multiple_tree(board)
        results = []
        for word in words:
            for trie in M.values():
                found = trie.search(word)
                if found:
                    results.append(word)
                    break
        return results
