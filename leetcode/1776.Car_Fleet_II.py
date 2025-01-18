class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        def catch(carA, carB):
            # print(carA)
            # print(carB)
            if carA[1] == carB[1]:
                return -1
            t = (carB[0] - carA[0]) / (carA[1] - carB[1])
            if t >= 0:
                return t
            return -1
        n = len(cars)
        cars = cars[::-1]
        cars = [None] + cars
        answers = [-1] * (n + 1)
        stack = []
        stack.append(cars[1])
        for i in range(2, n + 1):
            # print(f"i = {i}")
            ct = 0
            while len(stack) > 0:
                top = stack.pop()
                car = cars[i][0] + cars[i][1] * ct
                t = catch([car, cars[i][1]], top)
                t1 = 5e6 + 7
                add = 0
                if len(stack) > 0:
                    t1 = stack[-1][0]
                    add = (stack[-1][0] - top[0]) / top[1]
                # print(f"top = {top}, t = {t}")
                if t >= 0 and car + cars[i][1] * t < t1:
                    new_p = top[0] + top[1] * t
                    stack.append([new_p, top[1]])
                    answers[i] = t + ct
                    break
                ct = ct + add
            stack.append(cars[i])
        answers = answers[::-1]
        answers.pop()
        return answers
