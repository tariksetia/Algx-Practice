def partition (start, end, data):
    pivot = start
    lo, hi = start, end

    while True:
        
        while data[pivot] >= data[lo] and lo < end:
            lo += 1
        while data[pivot] < data[hi] and hi >start:
            hi -= 1
                
        if hi<=lo : break
        data[hi], data[lo] = data[lo], data[hi] # This statement comes after the check
    

    data[hi], data[pivot] = data[pivot], data[hi] #hi is the pivor
    
    return hi # Hi is the pivot


def three_way_partition(start, end, data):
    pivot = start
    lt = start
    gt = end
    i = start + 1
    
    while i <= gt:
        if data[i] < data[pivot]:
            data[i], data[lt] = data[lt], data[i]
            i, lt = i+1, lt+1
        
        elif data[i] > data[pivot]:
            data[i], data[gt] = data[gt], data[i]
            gt -= 1
        
        elif data[i] == data[pivot]:
            i += 1
    
    return (lt,gt)
