class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        n = len(cars)
        cars = cars[::-1]
        answers = [-1] * n
        last = 0
        for i in range(2, n):
            l, r = last, i - 1
            if cars[i][1] < cars[last][1]:
                answers[i] = -1
                continue
            save_t = -1
            while l <= r:
                mid = (l + r) // 2
                if cars[i][1] < cars[mid][1]:
                    l = mid + 1
                    continue
                t = (cars[mid][0] - cars[i][0]) / (cars[i][1] - cars[mid][1])
                if answers[mid] < 0:
                    save_t = t
                    r = mid - 1
                else:
                    if t <= answers[mid]:
                        save_t = t
                        l = mid + 1
                    else:
                        r = mid - 1
            answers[i] = save_t
            if save_t == -1:
                last = i
        return answers[::-1]
