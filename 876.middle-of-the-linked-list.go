/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func middleNode(head *ListNode) *ListNode {
    mid := head
    end := head
    
    for (end != nil && end.Next != nil) {
        mid = mid.Next
        end = end.Next.Next
    }

    return mid
}
