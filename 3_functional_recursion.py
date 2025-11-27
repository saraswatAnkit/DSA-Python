# sum of natural no using recursion

def func(sum, i, n):
    if i > n:
        print(sum)
        return
    func(sum + i, i+1, n)

func(0, 1, 4)

#  sum of natural no using functional recursion
def func2(n):
    if n == 1:
        return 1
    return n + func2(n-1)

print(func2(4))