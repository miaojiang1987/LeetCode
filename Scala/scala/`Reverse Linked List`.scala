import util._

import scala.annotation.tailrec

object `Reverse Linked List` {
    object Solution {
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
