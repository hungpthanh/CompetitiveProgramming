class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def checkDiff(wordA, wordB):
            cnt = 0
            for i in range(len(wordA)):
                if wordA[i] != wordB[i]:
                    cnt += 1
            return cnt == 1
        if beginWord not in wordList:
            wordList.append(beginWord)
        try:
            target = wordList.index(endWord)
            source = wordList.index(beginWord)
        except:
            return 0
        n = len(wordList)
        adj = {i: [] for i in range(n)}
        mark = {i: False for i in range(n)}
        for i in range(n - 1):
            for j in range(i + 1 , n):
                if checkDiff(wordList[i], wordList[j]):
                    adj[i].append(j)
                    adj[j].append(i)
        Q = deque()
        mark[source] = True
        Q.append((source, 1))
        while len(Q) > 0 :
            wordIndex, step = Q.popleft()
            if wordIndex == target:
                return step
            for adj_index in adj[wordIndex]:
                if not mark[adj_index]:
                    mark[adj_index] = True
                    Q.append((adj_index, step + 1))
        return 0
