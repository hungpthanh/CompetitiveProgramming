from collections import Counter

def precompute_combinations(max_count):
    """Precompute combinations for nC2 and nC3."""
    comb2 = [0] * (max_count + 1)
    comb3 = [0] * (max_count + 1)
    for i in range(2, max_count + 1):
        comb2[i] = (i * (i - 1)) // 2
    for i in range(3, max_count + 1):
        comb3[i] = (i * (i - 1) * (i - 2)) // 6
    return comb2, comb3

def solve(a, comb2, comb3):
    counter = Counter(a)
    smaller = 0
    res = 0
    # print(counter)
    for x in sorted(counter.keys()):  # Sorting keys to mimic ordered traversal
        count = counter[x]
        if count > 2:
            res += comb3[count]
        if count > 1:
            res += comb2[count] * smaller
        smaller += count
    
    return res

if __name__ == "__main__":
    import sys
    # input = sys.stdin.read2

    sys.stdin = open("test.in", "r")
    # sys.stdout = open("test.out", "w")

    n_test = int(input())
    max_count = 300000  # Assumed maximum element frequency in constraints
    comb2, comb3 = precompute_combinations(max_count)

    idx = 1
    results = []
    for _ in range(n_test):
        n = int(input())
        a = list(map(int, input().split()))
        results.append(solve(a, comb2, comb3))

    sys.stdout.write("\n".join(map(str, results)) + "\n")
