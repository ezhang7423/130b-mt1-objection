import numpy as np

X = "abdbabfgd"
Y = "betfdbafr"

dp = np.zeros((len(Y), len(X)))
for i in range(len(Y)):
    for j in range(len(X)):
        if Y[i] != X[j]:
            continue

        best_last = 0
        for r in range(i):
            best_last = max(best_last, dp[r, j - 1])
        
        dp[i, j] = best_last + 1
print(dp)
