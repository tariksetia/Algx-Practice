def peak_find(data):
    lo, hi = 0, len(data)-1

    while lo<=hi:
        mid = (lo+hi)//2
        if mid > hi-1 : return hi #When the array is sorted but not rotated mid = hi so mid+1 doesn't exist

        if data[mid] < data[mid-1]:
            hi = mid-1
        elif data[mid] < data[mid+1]:
            lo = mid+1
        else:
            return mid


if __name__ == '__main__':
    a=[6,7,8,9,1,3,4,5,6]
    b=[5,6,7,8,9,1]
    c=[3,4,5,6,7,1,2]
    d=[1,2,3,4,5,6,7]

    print(peak_find(a))
    print(peak_find(b))
    print(peak_find(c))
    print(peak_find(d))
        