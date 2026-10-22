# 最大化最小距离
# 二分 + 贪心
'''
max (d)

簇间距离，取最相近的两个点的距离

k选n
'''

# =========================
# 调试
# =========================
from io import StringIO
import sys

sys.stdin = StringIO("""1
3 2
1 6 8
""")

# =========================
# 解题代码
# =========================

# 假设最小距离至少是d，能否在xs里面放下n个点
# 从左边开始放
# def can_place_points(xs, n, d):
#     # 贪心：前面越紧凑越好，够后面留空间
#     count = 1
#     last_position = xs[0]

#     for i in range(1, len(xs)):
#         if xs[i] - last_position >= d:
#             count += 1
#             last_position = xs[i]
#             if count >= n:
#                 return True

#     return False

# 假设最小距离至少是d，能否在xs里面放下n个点
def can_place_points(xs, n, d):
    count = 1 # 最左边的点
    last_position = xs[0]

    # 遍历数组
    for i in range(1, len(xs)):
        if  xs[i]-last_position >= d:
            count += 1
            last_position = xs[i]
            if count >= n:
                return True
            
    return False


def find_max_distance(n, xs):
    # 从长度为n的数组xs中，选择k个点，让这k个点之间的最小距离最大
    # k=3, n=2
    # xs = [1 6 8]
    # 选择：1, 8。最小距离7。此时距离最大化
    # 返回最小距离的最大值:7
    # 算法：二分答案。假设距离为d，能否选出n个点，使得任意两个点之间的距离都大于等于d
    '''
        二分的是距离
        问能否选择出k个点，满足最小距离>=2
        出现：
        d = 2 √
        d = 3 √
        d = 4 √
        d = 5 ×
        d = 6 ×

        具有单调性

    贪心：前面越紧凑越好，够后面留空间
    '''
    # 二分距离
    # xs.sort()
    # left, right = 0, max(xs) - min(xs)
    # while left < right:
    #     mid = (left + right + 1) // 2
    #     if can_place_points(xs, n, mid):
    #         left = mid
    #     else:
    #         right = mid - 1
    # return left

    # 二分距离
    xs.sort()
    left, right = 0, xs[-1] - xs[0]
    while left < right:
        mid = (left + right + 1) // 2
        if can_place_points(xs, n, mid):
            left = mid
        else:
            right = mid - 1

    return left

def solve():
    input = sys.stdin.readline
    q = int(input())

    for _ in range(q):
        k, n =  map(int, input().split())
        xs = list(map(int, input().split()))
        ans = find_max_distance(n, xs)
        print(ans)

# =========================
# 主程序入口
# =========================

solve()