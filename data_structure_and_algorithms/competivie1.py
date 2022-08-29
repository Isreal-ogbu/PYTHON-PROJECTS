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
    for i in range(len(nums)-k+1):
        maxi = max(sum(nums[i:k + i]), maxi)
    return maxi


print(max_sum_of_k([1, 4, 2, 10, 2, 3, 1, 0, 20], 4))
print(max_sum_of_k([5, 2, -1, 0, 3], 3))

# Anagram substring search (Less Efficient)

def anagram_subtring(nums, com):
    table = dict()
    for i in com:
        if i in table:
            table[i] += 1
        else:
            table[i] = 1
    siz = len(com)
    count = 0
    for p in range(len(nums)-siz+1):
        val = nums[p:siz + p]
        tab = table.copy()
        for i in val:
            if i in tab.keys():
                if i in tab:
                    tab[i] -= 1
                if tab[i] == 0:
                    del tab[i]
                if len(tab) == 0:
                    count += 1
            else:
                break
    return count


print(anagram_subtring("forxxorfxdofr", "for"))

# Anagram substring (Efficint solution)

def anagram_substring(nums, num):
    s, p = len(nums), len(num)
    arr = []
    if s < p or p == 0:
        return
    hs, hp = [0 for _ in range(26)], [0 for _ in range(26)]
    for i in num:
        hp[ord(i) - ord('A')] += 1
    for i in range(0, p):
        hs[ord(nums[i]) - ord('A')] += 1

    flag = True

    for i in range(0, 26):
        if hp[i] != hs[i]:
            flag = False

    if flag:
        arr.append(0)

    for i in range(p, s):
        hs[ord(nums[i - p]) - ord('A')] -= 1
        hs[ord(nums[i]) - ord('A')] += 1

        if hs[ord(nums[i]) - ord('A')] == hp[ord(nums[i]) - ord('A')] and hs[ord(nums[i - p]) - ord('A')] == hp[
            ord(nums[i - p]) - ord("A")]:
            flag = True
            for j in range(0, 26):
                if hs[j] != hp[j]:
                    flag = False

        else:
            flag = False

        if flag:
            arr.append(i - p + 1)
    return arr


print(anagram_substring("BACDGABCDA", "ABCD"))


