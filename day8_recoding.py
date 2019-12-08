from collections import defaultdict

digits = [int(num) for num in open('data/day8.txt').read().strip()]
layers = len(digits) // (25*6)
C = defaultdict(lambda: defaultdict(int))
for l in range(layers):
    for i in range(25*6):
        C[l][digits[l*25*6 + i]] += 1


for l in range(layers):
    if l == 0:
        best = (C[l][0], l)
    else:
        if (C[l][0], l) <= best:
            best = (C[l][0], l)

l = best[1]
print(C[l][1]*C[l][2])


