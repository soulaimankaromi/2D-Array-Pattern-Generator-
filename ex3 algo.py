T = []
for i in range(0, 9):
    N = float(input("Type the number: "))
    T.append(N)
S = T[0] + T[1] + T[2] + T[3]
K = 0
for i in range(1, 6):
    k = T[i] + T[i + 1] + T[i + 2] + T[i + 3]
    if k > S:
        S = k
        K = i
print("The maximum sum is [", T[K], ",", T[K + 1], ",", T[K + 2], ",", T[K + 3], "] with a sum of", S)