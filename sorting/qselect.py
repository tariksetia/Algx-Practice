from partition import partition

def qselect(start, end, k, data):
    while low<high:
        pivot = partition(start,end,data):
        if k < pivot:
            end = pivot - 1
        elif k > pivot:
            start pivot + 1
        else:
            return data[k]