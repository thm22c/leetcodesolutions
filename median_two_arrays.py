#Problem:
#input: two sorted lists
#output: median of both lists

class Solution:
    def median(self, list):
        list_len = len(list)
        if list_len % 2 ==0:
            return (list[list_len//2]+list[(list_len//2)-1])/2
        else:
            return list[((list_len//2))]
    def findMedianSortedArrays(self, num1, num2):
        while True:
            if num1 == []:

                return self.median(num2)
            if num2 == []:
                return self.median(num1)
            #next trivial cases: min(num1)>max(num2) or reverse

            if (num1[0] >= num2[-1]):
                num2.extend(num1)
                return self.median(num2)
            if (num2[0] >= num1[-1]):
                num1.extend(num2)
                return self.median(num1)
            placed = False
            if len(num1) > len(num2):
                return self.findMedianSortedArrays(num2,num1)
            x = num1.pop(0)
            for i in range(0, len(num2)):
                if num2[i]>=x:
                    num2.insert(i,x)
                    placed = True
                    break
            if not placed:# should not be reachable code?
                num2.append(x)
