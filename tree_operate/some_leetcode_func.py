

# N 叉树的前序遍历
# https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
def pre_order(root):
    stack, res = [root], list()
    while stack:
        node = stack.pop()
        if not node:
            continue

        res.append(node.val)
        while node.children:
            # 因为是前序遍历，所以下一次处理的是该节点的第一个自节点，于是将所有孩子倒序后添加到 stack 中
            stack.extend(node.children[::-1])
            node = stack.pop()
            res.append(node.val)
    return res
