    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []
        while l1!=None:
            stack1.append(l1.val)
            l1 = l1.next
        while l2!=None:
            stack2.append(l2.val)
            l2 = l2.next
        c = 0
        preNode = None
        while stack1 or stack2:
            c,val = self.helper(stack1,stack2,c)
            newListNode = ListNode(val)
            newListNode.next = preNode
            preNode = newListNode
        if c:
            newListNode = ListNode(c)
            newListNode.next = preNode
        return newListNode
    def helper(self,stack1,stack2,c):
        if stack1 and stack2:
            val1 = stack1.pop()
            val2 = stack2.pop()
        elif stack1:
            val1 = stack1.pop()
            val2 = 0
        elif stack2:
            val1 = 0
            val2 = stack2.pop()
        return (val1+val2+c)//10,(val1+val2+c)%10