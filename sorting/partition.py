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

def partition_event_odd(data):
    data = list(data)
    low, high = 0, len(data)-1
    while low < high:
        while data[low]%2 == 0 and low < high:
            low += 1
        while data[high]%2 ==1 and low <high:
            high -=1
        
        if low<high:
            data[low],data[high] = data[high],data[low]
            low += 1
            high -= 1
    return data
if __name__ == '__main__':
    a= [3,2,5,2,6,23,5,34,23,5,324,3421,1235,456,324]
    print(partition_event_odd(a))
    b=[1,0,2,0,1,0,2,2,1,0,0,1,1,2,0,0,2]
