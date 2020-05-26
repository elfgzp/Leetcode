/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func reverseList(head *ListNode) *ListNode {
    if (head == nil) {
        return head
    }
    
    cur := head
    next := head.Next
    var tmp *ListNode
    for (next != nil) {
        tmp = next.Next
        next.Next = cur
        cur = next
        next = tmp
    }
    head.Next = nil
    return cur
}
