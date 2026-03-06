def sumNatural(n):
    if n <= 1:
        return n
    else:
        return n + sumNatural(n-1)

print(sumNatural(10))

#Time Complexity : O(N)
#Space Complexity : O(N) ----- stack space used for recursive calls