/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
    preHead := &ListNode{}
    node := preHead
    for l1 != nil && l2 != nil {
        if l1.Val < l2.Val {
            node.Next = l1
            l1 = l1.Next
            node = node.Next
        } else {
           node.Next = l2
           l2 = l2.Next 
           node = node.Next
        }
    }
    
    for l1 != nil {
        node.Next = l1
        l1 = l1.Next
        node = node.Next
    }
    
    for l2 != nil {
        node.Next = l2
        l2 = l2.Next
        node = node.Next
    }
    
    return preHead.Next
}
