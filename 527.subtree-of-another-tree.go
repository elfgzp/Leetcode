/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
func isSubtree(s *TreeNode, t *TreeNode) bool {
    if s == nil {
        return false
    }
    return isSubtree(s.Left, t) || isSameTree(s, t) || isSubtree(s.Right, t)
}

func isSameTree(t1 *TreeNode, t2 *TreeNode) bool {
    if t1 == nil || t2 == nil {
        return t1 == t2
    }

    return isSameTree(t1.Left, t2.Left) && t1.Val == t2.Val && isSameTree(t1.Right, t2.Right)
}
