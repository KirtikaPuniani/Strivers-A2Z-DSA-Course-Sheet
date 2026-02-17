#print name N times using recursion

class Name():
    def printName(self, name, count, n):
        if count == n:
            return
        print(name)
        
        self.printName(name, count+1, n)

x = Name()
n = 3
name = "Kirtika"

print(x.printName(name, 0, n))

#Time Complexity : O(N)
#Space Complexity : O(N) ----- stack space used for recursive calls