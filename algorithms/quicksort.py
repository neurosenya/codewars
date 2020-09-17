def quickSort(arr):
    less = []
    pivotList = []
    more = []
    arr_length = len(arr)
    if arr_length <= 1:
        return arr
    else:
        pivot = sorted([arr[0], arr[arr_length // 2], arr[-1]])[1]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        less = quickSort(less)
        more = quickSort(more)
        return less + pivotList + more
m = list(int(i) for i in input().split())
print(quickSort(m))
