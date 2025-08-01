def build_tree(inorder, postorder):
    inorder_index = {}
    idx = 0
    for value in inorder:
        inorder_index[value] = idx
        idx += 1

    post_index = [len(postorder) - 1]

    def helper(in_left, in_right):
        if in_left > in_right:
            return []

        root_val = postorder[post_index[0]]
        post_index[0] -= 1

        root_idx = inorder_index[root_val]

        right = helper(root_idx + 1, in_right)
        left = helper(in_left, root_idx - 1)

        return [root_val] + left + right

    return helper(0, len(inorder) - 1)


n = int(input())
inorder = [int(x) for x in input().split()]
postorder = [int(x) for x in input().split()]

preorder = build_tree(inorder, postorder)
print(" ".join(map(str, preorder)))