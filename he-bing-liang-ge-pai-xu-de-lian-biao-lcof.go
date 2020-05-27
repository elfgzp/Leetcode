/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    if (l1 == nil) {
        return l2
    }

    if (l2 == nil) {
        return l1
    }

    preHead := ListNode{0, nil}
    var node *ListNode
    if (l1.Val <= l2.Val) {
        node = l1
        l1 = l1.Next
    } else {
        node = l2
        l2 = l2.Next
    }
    
    preHead.Next = node
    
    for (l1 != nil && l2 != nil) {
        if (l1.Val <= l2.Val) {
            node.Next = l1
            node = node.Next
            l1 = l1.Next
        } else {
            node.Next = l2
            node = node.Next
            l2 = l2.Next
        }
    }

    if l1 != nil {
        node.Next = l1
    } else {
        node.Next = l2
    }

    return preHead.Next
}
