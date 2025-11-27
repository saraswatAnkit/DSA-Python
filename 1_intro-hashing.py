# Prestoring values into some datastructure like list/Dictionary and then fetching it

# Ques - we need to count the occurence of every value from second list in first list

# Constraints
# 1. 1<= n[i] <=10
# 2. n can have 10**8 elements
# 3. m can have 10**8 elements

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

# Brute Soln
for num in m:
    count = 0
    for x in m:
        if num == x:
            count += 1
    print(count)  # TC:- O(n*m) ~ O(n2) -> TLE

# Optimal Soln
hash_list = [0] * 11
for num in n:
    hash_list[num] += 1

for num in m:
    if num < 1 or num > 10:
        print(0)
    else:
        print(hash_list[num])   # TC:- O(n+m) SC:- O(1) -> No TLE

# Most Optimal Soln
hash_map = {}
k = len(n)
for i in range(0, k):
    hash_map[n[i]] = hash_map.get(hash_map[n[i]], 0) + 1

for num in m:
    if hash_map[m]:
        print(hash_map[m])
    else:
        print(0)