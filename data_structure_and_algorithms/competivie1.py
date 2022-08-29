# Reversing a list O(n/2)

def reverse(nums):
    l = 0
    r = len(nums) - 1
    while l <= r:
        nums[l], nums[r] = nums[r], nums[l]
        l += 1
        r -= 1
    return nums


print(reverse([1, 2, 3, 4, 5, 6, 7]))

# Sum of string

def sum_string(nums):
    s = 0
    for i in nums:
        s+= int(i)
    return s

print(sum_string("12345"))

# Sum prefix for 2D array

def sum_prefix_2D(nums):
    row = len(nums)
    col = len(nums[0])
    new = [[0 for i in range(col)] for j in range(row)]
    new[0][0] = nums[0][0]

    for val in range(0, row):
        new[val][0] = (new[val - 1][0] + nums[val][0])
    for val in range(1, col):
        new[0][val] = (new[0][val - 1] + nums[0][val])

    for i in range(1, row):
        for j in range(1, col):
            new[i][j] = new[i - 1][j] + new[i][j - 1] - new[i - 1][j - 1] + nums[i][j]

    for i in range(0, row):
        for j in range(0, col):
            print(new[i][j], end=' ')
        print()


sum_prefix_2D([[2, 1, 1, 1, 1],
               [1, 2, 1, 1, 1],
               [1, 1, 2, 1, 1],
               [1, 1, 1, 2, 1]])

# maximium sum of k in a string or list
def max_sum_of_k(nums, k):
    if len(nums) < k:
        return None
    if len(nums) == k:
        return sum(nums)
    maxi = 0
    for i in range(len(nums)):
        maxi = max(sum(nums[i:k + i]), maxi)
    return maxi


print(max_sum_of_k([1, 4, 2, 10, 2, 3, 1, 0, 20], 4))
print(max_sum_of_k([5, 2, -1, 0, 3], 3))

