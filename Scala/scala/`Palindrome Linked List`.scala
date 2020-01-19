import util.ListNode

object `Palindrome Linked List` {
    object Solution {
        def isPalindrome(head: ListNode): Boolean = {
            val rhead = reverse(head)
            var h = head; var rh = rhead
            while(h != null) {
                if(h._x != rh._x)
                    return false
                h = h.next
                rh = rh.next
            }
            true
        }

        def reverse(head: ListNode, cur: ListNode=null): ListNode = {
            if(head != null) {
                val next = head.next
                val node = new ListNode(head._x)
                node.next = cur
                reverse(next, node)
            }
            else
                cur
        }
    }
}
