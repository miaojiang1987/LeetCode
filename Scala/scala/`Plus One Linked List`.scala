object `Plus One Linked List` {
    import util.ListNode
    import scala.annotation.tailrec

    object Solution {
        def plusOne(head: ListNode): ListNode = {
            @tailrec def plus(cur: ListNode, increment: Int): Unit = {
                val sum = cur.x + increment
                val carry = sum / 10
                cur.x = sum % 10
                if(cur.next == null) {
                    if(carry > 0)
                        cur.next = new ListNode(carry)
                }
                else {
                    plus(cur.next, carry)
                }
            }
            val reversed = reverseList(head)
            plus(reversed, 1)
            reverseList(reversed)
        }

        def reverseList(head: ListNode): ListNode = {
            @tailrec def reverse(head: ListNode, reversed: ListNode): ListNode = {
                if(head == null)
                    reversed
                else {
                    val next = head.next
                    head.next = reversed
                    reverse(next, head)
                }
            }
            if(head == null)
                head
            else {
                val next = head.next
                head.next = null
                reverse(next, head)
            }
        }
    }
}
