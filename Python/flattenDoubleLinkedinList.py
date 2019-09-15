class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        node = head
        children = []
        prev = None
        while node:
            node.prev = prev
            if node.child:
                if node.next:
                    children.append(node.next)
                node.next = node.child
                node.child = None
                prev = node
                node = node.next
            elif node.next:
                prev = node
                node = node.next
            else:
                if children:
                    node.next = children.pop()
                    prev = node
                    node = node.next
                else:
                    prev = node    
                    node=node.next
        return head