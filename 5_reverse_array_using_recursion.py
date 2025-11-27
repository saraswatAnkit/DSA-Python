# Reverse an array using recursion

num = [5, 6, 3, 2,6 , 8, 11, 32]
n = num

def reverse(l, r):
    if l > r or l == r:
        return n
    n[l], n[r] = n[r], n[l]
    return reverse(l+1, r-1)

r = len(n) -1 # if want reverse full array
print(reverse(1, 6))