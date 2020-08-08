def pick_peaks(arr):
    c = 1
    peaks = {"pos":[], "peaks":[]}
    while c < len(arr) - 1:
        if arr[c] > arr[c-1] and arr[c] > arr[c+1]:
            peaks["pos"].append(c)
            peaks["peaks"].append(arr[c])
            c += 1
        elif arr[c] > arr[c-1] and arr[c] == arr[c+1]:
            for  j in range(c+1,len(arr)-1):
                #print(c, j, arr[j])
                if arr[j] > arr[c]:
                    break
                if arr[j] == arr[c] and arr[j] > arr[j+1]:
                    print(c, j, arr[j])
                    peaks["pos"].append(c)
                    peaks["peaks"].append(arr[c])
                    c = j+1 
                    break
         else:
            c += 1
    return peaks

print(pick_peaks([1,2,5,4,3,2,3,6,4,1,2,3,3,4,5,3,2,1,2,3,5,5,4,3]))
