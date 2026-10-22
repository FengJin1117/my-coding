'''
定义 cur_sum：以当前结点为终点的最大值。

如果是树的根节点，cur_sum = 0
看祖先能给后代留下多少遗产。其实只要是负资产，子代就不会选。
max(nodel.val, node.val + cur_sum)
'''

# 树节点
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
def max_downward_path_sum(root):
    if not root:
        return 0

    ans = float("-inf")

    # T: O(n)。遍历全局，每个节点都拿来问一下，如果以此终止，是不是最大值。
    def dfs(node, cur_sum): # cur_sum：祖先的最大值
        if not node:
            return

        nonlocal ans

        # 判断是否继承祖先遗产
        cur_sum = max(node.val, node.val+cur_sum)

        ans = max(cur_sum, ans)

        dfs(node.left, cur_sum)

        dfs(node.right, cur_sum)

    return ans