/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
    pre := &ListNode{Val:0}
    carry := 0
    node := pre

    for l1 != nil || l2 != nil {
        val1 := 0
        if l1 != nil {
            val1 = l1.Val
            l1 = l1.Next
        }

        val2 := 0
        if l2 != nil {
            val2 = l2.Val
            l2 = l2.Next
        }

        val := val1 + val2 + carry
        if val >= 10 {
            val -= 10
            carry = 1
        } else {
            carry = 0
        }

        node.Next = &ListNode{Val: val}
        node = node.Next

    }

    if carry == 1 {
        node.Next = &ListNode{Val: 1}
    }

    return pre.Next
}
