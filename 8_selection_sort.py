nums = [1, 7, 5, 8, 4, 6, 8, 0, 1]

def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if nums[j] < nums[i]:
                min_index = j
        nums[i], nums[min_index] = nums[min_index], nums[i]

selection_sort(nums)
print(nums)

def selection_sort_desc(nums):
    n = len(nums)
    max_index = 0
    for i in range(n):
        max_index = i
        for j in range(i + 1, n):
            if nums[j] > nums[max_index]:
                max_index = j
        nums[i], nums[max_index] = nums[max_index], nums[i]
    return nums

print(selection_sort_desc(nums))