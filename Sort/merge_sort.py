def Merge(arr, LeftIdx, MidIdx, RightIdx):
    LeftAreaIdx = LeftIdx
    RightAreaIdx = MidIdx + 1
    TempIdx = LeftIdx

    tmparr = [0] * (RightIdx - LeftIdx + 1)

    while LeftAreaIdx <= MidIdx and RightAreaIdx <= RightIdx:
        if arr[LeftAreaIdx] <= arr[RightAreaIdx]:
            tmparr[TempIdx - LeftIdx] = arr[LeftAreaIdx]
            LeftAreaIdx += 1
        else:
            tmparr[TempIdx - LeftIdx] = arr[RightAreaIdx]
            RightAreaIdx += 1
        TempIdx += 1
    
    if LeftAreaIdx > MidIdx:
        for i in range(RightAreaIdx, RightIdx+1):
            tmparr[TempIdx - LeftIdx] = arr[i]
            TempIdx += 1
    else:
        for i in range(LeftAreaIdx, MidIdx+1):
            tmparr[TempIdx - LeftIdx] = arr[i]
            TempIdx += 1

    for i in range(LeftIdx, RightIdx + 1):
        arr[i] = tmparr[i - LeftIdx]

def MergeSort(arr, LeftIdx, RightIdx):
    if LeftIdx < RightIdx:
        MidIdx = (LeftIdx+RightIdx)//2
        MergeSort(arr, LeftIdx, MidIdx)
        MergeSort(arr, MidIdx+1, RightIdx)
        Merge(arr, LeftIdx, MidIdx, RightIdx)
    return arr

print("=====Merge Sort=====")
arr = [3,5,2,4,1,7,6,8]
merge_sorted_arr = MergeSort(arr, 0, len(arr)-1)
print(merge_sorted_arr)
