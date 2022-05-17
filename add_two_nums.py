#problem
#two chains of nodes representing reversed numbers
#with no leading zeros
#-> add them together

class Solution:
    def mkListNode(self, num):
        numStr = str(num)
        numl = len(numStr)
        nodes = [ListNode() for x in range(0,numl)]
        for y in range(0,numl):
            nodes[y].val = (int) (numStr[-1])
            numStr = numStr[:-1]
            if y != numl-1:
                nodes[y].next = nodes[y+1]
        return nodes
    def gibNum(self, l1):
        offset = 1
        val = 0
        while True:
            val = val + l1.val*offset
            offset = offset * 10
            if l1.next != None:
                l1 = l1.next
            else:
                break
        return val

    def addTwoNumbers(self, l1, l2):
        return self.mkListNode(self.gibNum(l1)+self.gibNum(l2))[0]
