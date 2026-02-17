#print number 1 to n using recursion

#forward recursion
class Number():
    def printNum(self, curr, n):
        if curr > n:
            return
        print(curr, end = ' ')
        
        self.printNum(curr + 1, n)

x = Number()
n = 8
print(x.printNum(1,n))

#Time Complexity : O(N)
#Space Complexity : O(N) ----- stack space used for recursive calls


#--------------------------------------------------------------------------------------------------------------------------------------#

# what if in interview they ask to print n to 1 but without using "curr+1"??????????????????

class Number():
    def printNum(self, curr):
        if curr < 1:
            return
        print(curr, end=' ')
        self.printNum(curr - 1)

x = Number()
n = 8
x.printNum(n)
