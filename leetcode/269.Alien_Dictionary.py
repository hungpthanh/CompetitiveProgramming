class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adj = {}
        visit = {}
        topo = []
        set_of_chars = set()

        for i in range(n - 1):
            set_of_chars.update(list(words[i]))
            m = min(len(words[i]), len(words[i + 1]))
            found = False
            for j in range(m):
                if words[i][j] != words[i + 1][j]:
                    found = True
                    adj.setdefault(words[i + 1][j], set()).add(words[i][j])
                    break
            if not found and len(words[i]) > len(words[i + 1]):
                return ""
        set_of_chars.update(list(words[n - 1]))
        invalid = False
        def dfs(u):
            nonlocal invalid, visit
            if invalid:
                return
            visit[u] = 1
            if u in adj:
                for v in adj[u]:
                    if v not in visit:
                        dfs(v)
                    else:
                        if visit[v] == 1:
                            invalid = True
            topo.append(u)
            visit[u] = 2

        for element in set_of_chars:
            if (element not in visit):
                dfs(element)
        if invalid:
            return ""
        return "".join(topo)
        
