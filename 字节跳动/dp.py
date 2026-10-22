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
from typing import List

def solve(nums: List[int]) -> int:
    '''
    定义被删除元素，前后的dp数组：
    pre[i]表示以nums[i]结尾的，最大长度
    post[i]表示以nums[i]开头的
    三种选择：
    - 选择前面的
    - 选择后面的
    - 跨过去。nums[i+1] > nums[i-1]
    '''
    n = len(nums)
    if n == 0:
        return 0
    
    ans = 1

    pre = [1] * n
    post = [1] * n

    for i in range(1, n):
        if nums[i] > nums[i-1]:
            pre[i] += pre[i-1]

    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            post[i] += post[i+1]

    # 枚举每个元素，尝试删除

    for i in range(n):
        if i > 0:
            ans = max(ans,  pre[i-1])

        if i < n-1:
            ans = max(ans, post[i+1])

        if (0 <= i < n-1) and nums[i+1] > nums[i-1]:
            ans = max(ans, pre[i-1]+post[i+1])

    return ans

nums = [1, 3, 9, 5, 7]
ans = solve(nums)
print(ans)