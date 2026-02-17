#print number n to 1 using recursion

#backtracking
class Number():
    def printNum(self, curr, n):
        if curr > n:
            return
        
        self.printNum(curr + 1, n)
        
        print(curr, end = ' ')

x = Number()
n = 9
print(x.printNum(1,n))

#Time Complexity : O(N)
#Space Complexity : O(N) ----- stack space used for recursive calls