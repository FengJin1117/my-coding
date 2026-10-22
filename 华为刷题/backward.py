# =========================
# 调试
# =========================
from io import StringIO
import sys

sys.stdin = StringIO("""2 2 2
0.4 0.3
-0.5 0.6
0.1 -0.2
0.5 -0.3
0.2 0.4
0.0 0.1
1.0 0.5
0.5 0.3
0.2
""")


# 思路
'''
梯度 = 终点误差 × 起点激活值
'''

# =========================
# 解题代码
# =========================

def solve():
    import sys
    import numpy as np
    input = sys.stdin.readline

    din, dhid, dout = map(int, input().split())

    W1 = np.array([list(map(float, input().split())) for _ in range(dhid)]) # [dhid, din]
    b1 = np.array(list(map(float, input().split()))) # [dhid,]
    W2 = np.array([list(map(float, input().split())) for _ in range(dout)]) # [dout, dhid]
    b2 = np.array(list(map(float, input().split()))) # [dout,]
    x = np.array(list(map(float, input().split()))) # [din,]
    ytrue = np.array(list(map(float, input().split()))) # [dout,]
    lr = float(input())

    # 正向传播
    z1 = W1 @ x + b1 # [dhid,]
    a1 = np.maximum(z1, 0.0) # [dhid,] 
    ypred = W2 @ a1 + b2  # [dout,]

    # 反向传播
    delta2 = ypred - ytrue # [dout,]
    dW2 = np.outer(delta2, a1) # [dout, dhid]
    db2 = delta2
    # 隐藏层误差 = 后一层权重 × 后一层误差
    delta1 = (W2.T @ delta2) * (z1 > 0)  # [dhid,]
    dW1 = np.outer(delta1, x) # [dhid, din]
    db1 = delta1

    # 更新参数
    W1 -= lr * dW1
    b1 -= lr * db1
    W2 -= lr * dW2
    b2 -= lr * db2

    # 收集输出: W1, b1, W2, b2, ypred
    lines = []
    for row in W1:
        lines.append(" ".join(f"{v:.6f}" for v in row))
    lines.append(" ".join(f"{v:.6f}" for v in b1))
    for row in W2:
        lines.append(" ".join(f"{v:.6f}" for v in row))
    lines.append(" ".join(f"{v:.6f}" for v in b2))
    lines.append(" ".join(f"{v:.6f}" for v in ypred))
    print("\n".join(lines))

# =========================
# 主程序入口
# =========================

if __name__ == "__main__":
    solve()