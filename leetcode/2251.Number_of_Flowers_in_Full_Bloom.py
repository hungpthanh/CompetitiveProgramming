class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        points = []
        for flower in flowers:
            points.append((flower[0], -1))
            points.append((flower[1], 1))
        for idx, person in enumerate(people):
            points.append((person, 0, idx))
        points.sort()
        results = [0] * len(people)
        cnt = 0
        for point in points:
            if point[1] == -1:
                cnt += 1
            elif point[1] == 1:
                cnt -= 1
            else:
                results[point[2]] = cnt
        return results
