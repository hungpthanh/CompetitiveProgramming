from collections import Counter


def solve(a):
    counter = Counter(a)
    smaller = 0
    # exponents = counter.keys()
    res = 0

    for _, count in sorted(counter.items()):
        if count > 2:
            res += (count * (count - 1) * (count - 2)) // 6
        if count > 1:
            res += ((count * (count - 1)) // 2) * smaller
        smaller += count
    
    return res

if __name__ == "__main__":
    
    # sys.stdin = open("test.in", "r")
    # sys.stdout = open("test.out", "w")

    n_test = int(input())
    for _ in range(n_test):
        n = int(input())
        a = list(map(int, input().split()))
        print(solve(a))
