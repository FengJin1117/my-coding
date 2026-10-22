# =========================
# 调试
# =========================
from io import StringIO
import sys

sys.stdin = StringIO("""
""")

# =========================
# 解题代码
# =========================

def solve():
    import sys
    input = sys.stdin.readline
    # 单个数
    n = int(input())
    # 多个数
    m, n = map(int, input().split())
    # 列表
    arr = list(map(int, input().split()))



# =========================
# 主程序入口
# =========================

solve()