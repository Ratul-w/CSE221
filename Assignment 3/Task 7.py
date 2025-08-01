def build_post_order(inorder, preorder, in_start, in_end, pre_idx, postorder):
    if in_start > in_end:
        return pre_idx
    root_value = preorder[pre_idx]
    root_pos = -1
    for i in range(in_start, in_end + 1):
        if inorder[i] == root_value:
            root_pos = i
            break

    pre_idx = build_post_order(inorder, preorder, in_start, root_pos - 1, pre_idx + 1, postorder)

    pre_idx = build_post_order(inorder, preorder, root_pos + 1, in_end, pre_idx, postorder)

    postorder.append(root_value)

    return pre_idx


num_nodes = int(input())
inorder_traversal = [int(x) for x in input().split()]
preorder_traversal = [int(x) for x in input().split()]

postorder_result = []
build_post_order(inorder_traversal, preorder_traversal, 0, num_nodes - 1, 0, postorder_result)

print(" ".join(map(str, postorder_result)))