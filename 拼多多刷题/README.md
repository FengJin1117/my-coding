
# 基础
- 前缀和、差分


# 真实经验

- 大数据用`sys.stdin.readline`，普通input会直接超时
- 记得删除调试代码

## 二分

例如统计 2 出现多少次：

cnt = bisect_right(arr, 2) - bisect_left(arr, 2)

求区间 [L,R] 内元素个数

这是你刚做的题：
```python
count = bisect_right(arr, R) - bisect_left(arr, L)
```

把数组想象成：
```
< x | == x | > x
```