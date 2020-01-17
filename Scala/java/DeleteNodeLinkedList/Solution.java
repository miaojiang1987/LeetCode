package DeleteNodeLinkedList;
import javaUtil.ListNode;

public class Solution {
    public void deleteNode(ListNode node) {
        ListNode next = node.next;
        int temp = next.val;
        next.val = node.val;
        node.val = temp;
        node.next = next.next;
    }
}
