def max_sequence(arr):
    ''' 
    returns a maximal sum of a contiguos subsequence in an array with
    '''
    if len(arr) == 0:
        return 0
    if sum([0 if i >= 0 else 1 for i in arr]) == 0:
        return sum(arr)
    else:
        biggest_sum = 0
        for idx in range(len(arr)):
            for x in range(idx, len(arr)):
                new_sum = sum(arr[idx:x+1])
                if new_sum > biggest_sum:
                    biggest_sum = new_sum
        return biggest_sum

print(max_sequence([-1, 3, 0]))
    
    
