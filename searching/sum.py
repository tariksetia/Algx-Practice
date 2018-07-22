###
# Find Two elements in array such that their sum =K
###

# Assuming Array is sorted

def two_sum1(arr,k):
    lo, hi = 0, len(arr)-1
    while lo < hi :
        sum = arr[lo] + arr[hi]
        if sum == k:
            return arr[lo], arr[hi]
        elif sum < k:
            lo += 1
        else:
            hi -= 1
    return None,None

def sum_close_to_zero(data):
    data.sort()
    lo, hi = 0, len(data)-1
    total = data[lo] + data[hi]
    abs_sum  = abs(total)
    indexes = (lo,hi)
    values = (data[lo],data[hi])

    while lo < hi: 
        total = data[lo] + data[hi]
        #print('{} = {} + {}'.format(abs(total), data[lo], data[hi]))
        if abs(total) < abs_sum:
            abs_sum = abs(total)
            indexes = (lo, hi)
            values = (data[lo],data[hi])

        if total > 0:
            hi -= 1
        if total <0:
            lo += 1
        if total == 0:
            return abs_sum,indexes,values
        
    return abs_sum,indexes,values

def three_sum(data, target):
    data.sort()
    n = len(data)

    for i in range(n-2):
        left = i+1
        right = n-1

        while left < right:
            sum_ = sum([data[k] for k in [i, left, right]])
            #print('{} = {} + {} + {}'.format(sum_,data[i],data[left],data[right]))
            if sum_ == target:
                return i, left, right
            if sum_ < target:
                left += 1
            if sum_ > target:
                right -= 1
        
    return None, None ,None
            
            
    

    
if __name__ == '__main__':
    a = [-1313,-3424,-23,123,324,143,4353,231435,413,1313]
    b = sorted(a)
    print('two_sum1, k= -3447 : {}'.format(two_sum1(b,-3447)))
    print('two_sum1, k= 467 : {}'.format(two_sum1(b,467)))
    print('two_sum1, k= 466 : {}'.format(two_sum1(b,466)))
    print('\n')
    sum_, index, value = sum_close_to_zero(b)
    print('sum close to zero = {} for {} at {}'.format(sum_, index, value))
    print('\n')
    print('ThreeSum, k=323: {}'.format(three_sum(b,323)))
    print('ThreeSum, k=226698: {}'.format(three_sum(b,226698)))

