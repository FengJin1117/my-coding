# =========================
# 调试
# =========================
from io import StringIO
import sys

sys.stdin = StringIO("""3
10
1 5 100
2 3 50
3 1 20
""")

# =========================
# 解题代码
# =========================

def solve():
    n = int(input())
    S = int(input())
    a = []
    cur = 0

    for _ in range(n):
        h, l, r = map(int, input().split())
        a.append((h, l, r))
        cur += r

    # 最终的答案
    ans = abs(cur-S)

    # 按照h从低到高排序
    a.sort()

    # 开始依次减值，让r->l
    # 这里要相同阈值，重复减值
    i = 0
    while i < n:
        # 相同元素必须一起变化
        h = a[i][0]

        j = i
        # 这是一个阶梯渐变的过程
        while j < n and a[j][0] == h:
            cur += l - r
            j += 1

        ans = min(ans, abs(cur-S))
        i = j 

    print(ans)



# =========================
# 主程序入口
# =========================

solve()