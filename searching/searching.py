def find_first_occurance(data, val): #In Sorted array

    low, mid, high = 0, 0, len(data)-1
    index = None
    while (low < high):
        mid = (low + high)//2
        if data[mid] == val:
            index = mid
            high = mid-1
        if data[mid] < val:
            low = mid +1
        if data[mid] > val:
            high = mid-1
    return index

def find_last_occurance(data, val):
    low, mid, high = 0,0,len(data)-1
    index = None
    while low<high:
        mid = (low+high)//2
        if data[mid] == val:
            index=mid
            low = mid +1
        if data[mid] < val:
            low = mid +1
        else:
            high = mid -1
    return index

if __name__ == '__main__':
    data = [1, 23, 23, 32, 32, 32, 34, 34, 43, 54, 54, 54, 56, 67, 87]

    vals = [23,54,32]
    for i in vals:
        first = find_first_occurance(data,i)
        last = find_last_occurance(data,i) 
        print('{} : {}, {}'.format(i,first,last))