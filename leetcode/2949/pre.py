cnts = []
for k in range(1, 1001):
    cnt = 0
    for i in range(1, 50001):
        if (i * i) % k == 0:
            cnt += 1
    cnts.append(cnt)
    print(f"k = {k}, cnt = {cnt}")
print(max(cnts))