
'''
dp[i][j]：array1[:i]和array2[:j]的最小dtw距离。
转移公式：
dtw[i][j] = abs(arr1[i-1] - arr2[j-2]) + min(
    dtw[i-1][j-1], # arr1, arr2都往前走
    dtw[i-1][j], # arr1 往前走
    dtw[i][j-1] # arr2 往前走
)
'''
def dtw(array1, array2):
    n, m = len(array1), len(array2)

    dp = [[float("inf")] * (m+1) for _ in range(n+1)]
    dp[0][0] = 0

    for i in range(1, n+1):
        for j in range(1, m+1):
            cost = abs(array1[i-1] - array2[j-1])
            dp[i][j] = cost + min(
                dp[i-1][j],
                dp[i][j-1],
                dp[i-1][j-1]
            )

    return float(dp[n][m])

print(dtw([1,2,3],  [1,2,3]))
print(dtw([5], [1,2,3,8]))