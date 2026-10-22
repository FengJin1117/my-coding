# =========================
# 调试
# =========================
from io import StringIO
import sys
import numpy as np

sys.stdin = StringIO("""4 3 2 3
1.0 0.5 0.2
0.8 0.3 0.9
0.2 0.7 0.4
0.5 0.1 0.6
0.3 0.7
0.5 0.2
0.2 0.1
1.0 0.0 0.0
0.0 1.0 0.0
0.0 0.0 1.0
0.5 0.0 0.0
0.0 0.5 0.0
0.0 0.0 0.5
""")

# =========================
# 解题代码
# =========================

def softmax(logits): # [N, C]
    # 技巧：为了数值稳定性，减去每行的最大值
    logits -= np.max(logits, axis=1, keepdims=True)
    exp = np.exp(logits)
    return exp / np.sum(exp, axis=1, keepdims=True)

def solve():
    n, d, e, s = map(int, input().split())

    # 如果参数存在0，return 0
    if n == 0 or d == 0 or e == 0 or s == 0:
        return 0

    # [n, d]
    X = np.array([list(map(float, input().split())) for _ in range(n)]) 
    # [[1.  0.5 0.2]
    # [0.8 0.3 0.9]
    # [0.2 0.7 0.4]
    # [0.5 0.1 0.6]]

    Wg = np.array([list(map(float, input().split())) for _ in range(d)]) # [d, e]
    We = np.array([list(map(float, input().split())) for _ in range(e * s)]) # [e*d, d]

    # print(n, d, e, s) # 4 3 2 3
    # print(X)
    # print(Wg)
    # print(We)

    expert_score = X @ Wg # [n, e]
    # print(expert_score)

    probs = softmax(expert_score)
    # print(probs) # n, e
    '''
    [[0.44275215 0.55724785] # token 0
    [0.46505705 0.53494295] # token 1
    [0.54239794 0.45760206] # token 2
    [0.4725277  0.5274723 ]] # token 3
    '''

    # top-s。选择前3的token
    # expert 0：选择token 1,2,3。在维度0上选择最大的s个元素
    # expert 1：选择token 0,1,3。在维度1上选择最大的s个元素
     # [n, e]
    '''
    [[0 0.55724785] # token 0
    [0.46505705 0.53494295] # token 1
    [0.54239794 0] # token 2
    [0.4725277  0.5274723 ]] # token 3
    '''
    selected_probs = np.zeros_like(probs) # [n, e]
    for i in range(e):
        top_indices = np.argsort(probs[:, i])[-s:] # 选择第i列最大的s个元素的索引
        selected_probs[top_indices, i] = probs[top_indices, i] # 保留这些元素的概率，其他置0

    print(selected_probs) # [n, e]

    # 最后的结果，token只需要乘以对应的专家权重
    # 比如token 0：只乘以专家1的权重；token 1：乘以专家0和专家1的权重；token 2：只乘以专家0的权重；token 3：乘以专家0和专家1的权重
    # 因此结果中需要对We进行分割，匹配对应的专家权重，保持维度
    # token 0：乘以We的第1块（对应专家1的权重）；token 1：乘以We的第0块和第1块；token 2：乘以We的第0块；token 3：乘以We的第0块和第1块
    output = np.zeros((n, d)) # [n, d]
    for i in range(e):
        # 选择第i块权重
        We_i = We[i * d:(i + 1) * d, :] # [d, d]
        # 将选中的概率乘以对应的权重
        output += selected_probs[:, i:i+1] * (X @ We_i) # [n, d]
    
    # 输出最终结果，保留两位精度输出
    print(np.round(output, 2)) # [n, d]

    # 按照字符串形式输出，去除列表
    for row in output:
        print(" ".join(f"{x:.2f}" for x in row))

# =========================
# 主程序入口
# =========================

if __name__ == "__main__":
    solve()