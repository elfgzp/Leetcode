/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func removeNthFromEnd(head *ListNode, n int) *ListNode {
    dummyHead := &ListNode{0, head}
    pre := dummyHead
    end := dummyHead

    i := 0
    for (i <= n) {
        end = end.Next
        i += 1
    }

    for (end != nil) {
        pre = pre.Next
        end = end.Next
    }

    pre.Next = pre.Next.Next
    return dummyHead.Next
}
