# =========================
# 调试
# =========================
from io import StringIO
import sys

sys.stdin = StringIO("""aabb355dd
""")

# =========================
# 解题代码
# =========================

def solve():
    s = input()

    '''
    （偶，奇）（偶，奇）| 插入值 | （奇，偶）（奇，偶）
    因为pair的这种特性，因此可以二分
    '''
    n = len(s)
    l, r = 0, n-1
    while l < r:
        mid = (l+r) // 2

        # 因为要成对，因此强制为偶数
        if mid % 2 == 1:
            mid -= 1

        if s[mid] == s[mid+1]: # （偶，奇）
            l = mid + 2
        else:
            r = mid
        

    print(l)

# =========================
# 主程序入口
# =========================

solve()