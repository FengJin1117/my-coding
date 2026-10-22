# =========================
# 调试
# =========================
from io import StringIO
import sys

sys.stdin = StringIO("""7 3
-7 -1 3 6 2 -4 9
0 3
-1 4
-10 10
""")

# =========================
# 解题代码
# =========================

# 最大化最小距离
'''
max (d)

簇间距离，取最相近的两个点的距离
'''


from bisect import bisect_left, bisect_right

def solve():
    input = sys.stdin.readline
    # 多个数
    n, q = map(int, input().split())
    # 列表
    arr = list(map(int, input().split()))
    arr.sort()

    for _ in range(q):
        # 找到在[l, r]数值内的区间
        l, r = map(int, input().split())
        
        left = bisect_left(arr, l) # 第一个>=l的位置
        right = bisect_right(arr, r) # 第一个>r的位置

        print(right - left)



# =========================
# 主程序入口
# =========================

solve()