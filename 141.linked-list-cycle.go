/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
    if (head == nil) {
        return false
    }

    slow := head
    fast := slow.Next
    if (fast == nil || fast.Next == nil) {
        return false
    }
    fast = fast.Next

    for (slow != nil && fast != nil) {
        if (slow.Val == fast.Val) {
            return true
        }

        slow = slow.Next
        fast = fast.Next
        if (fast == nil) {
            break
        }

        fast = fast.Next
    }
    return false
}
