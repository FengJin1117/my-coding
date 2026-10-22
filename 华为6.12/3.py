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
    n = int(input())

    for _ in range(n):
        parts = input().split()
        print(parts)


# =========================
# 主程序入口
# =========================

if __name__ == "__main__":
    solve()