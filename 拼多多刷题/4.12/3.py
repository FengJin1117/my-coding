'''
第三题：戴森环能源转运问题
题目描述
飞船从坐标 s 出发，沿一条直线收集能源仓。飞船总燃料为 N（每走 1 单位距离消耗 1 单位燃料），经过某个能源仓的位置时自动收集该仓的能源。共有 M 个能源仓，分布在直线上各个位置。求在燃料限制下，最多能收集多少能源。

样例
输入

1
4 3 5
8 4 6
4 7 2
输出

9
思路分析
第一步：分析最优路线结构

飞船从原点 s 出发，可以向左走也可以向右走。关键观察：最优策略一定是先往一个方向走到某个距离，然后折返往另一个方向走。不需要来回折返多次，因为每次折返都浪费双倍燃料。因此只有两种路线形态：先左后右，或先右后左。

第二步：将能源仓分为左右两侧

以起点 s 为界，将所有能源仓分成左侧（坐标 < s）和右侧（坐标 >= s）。每侧按照距离从近到远排序，因为走到距离 d 的仓会自动收集途中所有仓。构建距离数组和能源前缀和。

第三步：枚举一侧 + 二分另一侧

对于”先左后右”路线：左侧走了 l_cost 距离，消耗燃料 2 * l_cost（去程 + 折返），剩余燃料 N - 2 * l_cost 可用于右侧。对于”先右后左”路线：右侧走了 r_cost 距离，消耗 2 * r_cost，剩余用于左侧。枚举一侧取前 i 个仓，通过二分在另一侧的距离数组上找到剩余燃料最多能到达的位置，累加两侧的能源前缀和取最大值。
'''

# 最大化最小距离
'''
max (d)

簇间距离，取最相近的两个点的距离
'''

# =========================
# 调试
# =========================
from io import StringIO
import sys

sys.stdin = StringIO("""1
4 3 5
8 4 6
4 7 2
""")

# =========================
# 解题代码
# =========================

def solve():
    import sys
    input = sys.stdin.readline

    # 单个数
    T = int(input())

    for _ in range(T):
        # 多个数
        N, M, s = map(int, input().split()) # 燃料数，能源仓数，原点位置（s: start）
        # 列表
        pos = list(map(int, input().split()))
        energy = list(map(int, input().split()))

        # 枚举 + 前缀和
        # 枚举一个方向走多远，另一个方向用剩余燃料能走多远走多远

        '''
        算法思路：
        1. 将能源仓分为左右两侧，计算距离和前缀和
        2. 枚举一侧 + 二分另一侧
         - 先左后右：枚举左侧走了 l_cost，剩余燃料 N - 2*l_cost 用于右侧，二分找到右侧能到达的最大距离 r_cost，计算总能源
         - 先右后左：枚举右侧走了 r_cost，剩余燃料 N - 2*r_cost 用于左侧，二分找到左侧能到达的最大距离 l_cost，计算总能源
         - 取两种路线的最大值
         3. 注意边界情况：只走一侧的情况（即 l_cost=0 或 r_cost=0）
        '''
        # 1. 分左右两侧
        left = []
        right = []
        for p, e in zip(pos, energy):
            if p < s:
                left.append((s - p, e)) # 距离，能源
            else:
                right.append((p - s, e))
        # 分别排序
        left.sort()
        right.sort()

        # 计算前缀和
        left_dist = [0] # 距离前缀和
        left_energy = [0] # 能源前缀和
        for d, e in left:
            left_dist.append(left_dist[-1] + d)
            left_energy.append(left_energy[-1] + e)
        right_dist = [0]
        right_energy = [0]
        for d, e in right:
            right_dist.append(right_dist[-1] + d)
            right_energy.append(right_energy[-1] + e)

        # 2. 枚举一侧 + 二分另一侧
        max_energy = 0
        # 先左后右：枚举左侧走了 l_cost，剩余燃料 N - 2*l_cost 用于右侧，二分找到右侧能到达的最大距离 r_cost，计算总能源
        for i in range(len(left) + 1): # 因为要枚举left的所有情况，所以要len(left)+1
            l_cost = left_dist[i]
            # 边界情况：根本无法折返
            if l_cost * 2 > N:
                if l_cost <= N:
                    max_energy = max(max_energy, left_energy[i]) 
                break
            remaining = N - 2 * l_cost
            # 二分右侧能到达的最大距离 r_cost
            import bisect
            j = bisect.bisect_right(right_dist, remaining) - 1
            total_energy = left_energy[i] + right_energy[j] # 利用前缀和算路上获得的能量
            max_energy = max(max_energy, total_energy)

        
       # 先右后左：枚举右侧走了 r_cost，剩余燃料 N - 2*r_cost 用于左侧，二分找到左侧能到达的最大距离 l_cost，计算总能源
        for j in range(len(right) + 1):
            r_cost = right_dist[j]
            if r_cost * 2 > N:
                if r_cost <= N:
                    max_energy = max(max_energy, right_energy[j])
                break
            remaining = N - 2 * r_cost
            i = bisect.bisect_right(left_dist, remaining) - 1
            total_energy = right_energy[j] + left_energy[i]
            max_energy = max(max_energy, total_energy)

        print(max_energy)


# =========================
# 主程序入口
# =========================

solve()