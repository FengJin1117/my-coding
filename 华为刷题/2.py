from io import StringIO
import sys

sys.stdin = StringIO("""8
ADD 10 35
ADD 20 55
QUERY 15
ADD 30 78
QUERY 25
ADD 25 69
QUERY 40
QUERY 5
""")



def solve():
    samples = []

    sum_x = 0
    sum_y = 0
    sum_xy = 0
    sum_x2 = 0
    n = 0

    def query(x):
        if n == 0:
            return 0
        
        xs = [x for x,y  in samples]

        # 所有 x 相同（解不唯一），使用平均值
        if len(set(xs)) == 1:
            return sum_y / n
        
        # 进行正常拟合预测
        a = (n*sum_xy - sum_x * sum_y) / (n*sum_x2 - sum_x**2)
        b = (sum_y - a * sum_x) / n

        return a * x + b

    # == IO ==
    number_of_query = int(input())

    for _ in range(number_of_query):
        line = input().strip() # 去除换行
        parts = line.split()

        # ADD x y
        if parts[0] == "ADD":
            x, y = float(parts[1]), float(parts[2])
            samples.append((x, y))
            sum_x += x
            sum_y += y
            sum_xy += x * y
            sum_x2 += x**2
            n += 1
        else:
        # QUERY x0
            x0 = float(parts[1])
            print(f"{query(x0):.6f}")

solve()