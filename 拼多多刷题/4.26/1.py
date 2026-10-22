# =========================
# 调试
# =========================
from io import StringIO
import sys

sys.stdin = StringIO("""3 10 10
5 5 2 8
4 3 3 5
8 2 4 6
""")

'''
第一题：多多的Token
题目描述
n 个任务，每个可以不执行、以常规模式执行（花费 a_i  token + b_i 时间）或以降耗模式执行（花费 c_i token + d_i 时间）。总 token 预算 m，总时间预算 t。求最多完成多少个任务。


n≤100，

m≤200，

t≤200。

样例
输入

3 10 10
5 5 2 8
4 3 3 5
8 2 4 6
输出

2
'''

# =========================
# 解题代码
# =========================

def solve():
    import sys
    input = sys.stdin.readline

    # 多个数
    n, m, t = map(int, input().split()) # 任务数，token预算，时间预算

    # 输入n个任务：(a, b, c, d)。两种模式
    tasks = []
    for _ in range(n):
        a, b, c, d =  map(int, input().split())
        tasks.append((a, b, c, d))

    '''
        算法思路：二维背包dp。
        定义dp[i][j][k]表示前i个任务，使用j token，花费k时间，最多完成的任务数。
        优化目标：任务数
        约束条件：token j < m, 时间k < t
        状态转移：
        dp[i][j][k] = max(
            dp[i-1][j][k], # 不执行第i个任务
            dp[i-1][j-a_i][k-b_i] + 1 if j>=a_i and k>=b_i else 0, # 常规模式
            dp[i-1][j-c_i][k-d_i] + 1 if j>=c_i and k>=d_i else 0 # 降耗模式
        )
        最终答案为max(dp[n][j][k]) for j in [0, m] and k in [0, t]
    ''' 
    # 算法实现
    # 初始化dp数组
    dp = [[[0]*(t+1) for _ in range(m+1)] for _ in range(n+1)]

    # 状态转移
    for i in range(1, n+1):
        a, b, c, d = tasks[i-1]
        for j in range(m+1):
            for k in range(t+1):
                # 不执行第i个任务
                dp[i][j][k] = dp[i-1][j][k]

                # 常规模式
                if j >= a and k >= b:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-a][k-b] + 1)

                # 降耗模式
                if j >= c and k >= d:
                    dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-c][k-d] + 1)
    
    # 选择答案
    ans = 0
    for j in range(m+1):
        for k in range(t+1):
            ans = max(ans, dp[n][j][k])
    print(ans)


# =========================
# 主程序入口
# =========================

solve()