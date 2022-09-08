# RETURN MOST FREQUENT ELEMENT
def most_freq(val):
    arr = []
    maxi = 1
    for i in val:
        if arr and arr[-1][0] == i:
            arr[-1][1] += 1
        else:
            arr.append([i, 1])

        maxi = max(arr[-1][1], maxi)
    arr1 = []
    for i, j in arr:
        if j == maxi:
            arr1.append([i, j])
    return str(arr1[-1][0]) + str(arr1[-1][1])


print(most_freq("bbbcccbbbba"))
