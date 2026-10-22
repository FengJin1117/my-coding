

# 左子树叶子 + 右子树叶子
def CountLeaves(node):
    if not node.left and not node.right:
        return 1
    
    num_left = 0
    num_right = 0

    if node.left:
        num_left = CountLeaves(node.left)

    if node.right:
        num_right = CountLeaves(node.right)

    return num_left + num_right

# 深度
# 1 + max（左子树深度，右子树深度）
def TreeDepth(node):
    if not node.left and not node.right: # 叶子：1
        return 1
    
    num_left = 0
    num_right = 0

    if node.left:
        num_left = TreeDepth(node.left)

    if node.right:
        num_right = TreeDepth(node.right)

    return 1 + max(num_left, num_right)
