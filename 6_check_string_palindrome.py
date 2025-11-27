s = "nitin"
# if (s == s[::-1]):
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# temp = ""
# n = len(s) -1
# while(n >= 0):
#     temp += s[n]
#     n -= 1

# if temp == s:
#     print("Palindrome")

# n = len(s)
# check = 1
# left = 0
# right =  n -1
# while left < right:
#     if s[left] != s[right]:
#         check = 0
#     left += 1
#     right -= 1
# if check == 0:
#     print("Not Plaindrome")
# else:
#     print("Palindrome")    

#  Using Recursion
def func(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    return func(s, left + 1, right - 1)

if func(s, 0, len(s)-1):
    print("Palindrome")
else:
    print("Not Palindrome")
