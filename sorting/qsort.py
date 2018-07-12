from partition import partition, three_way_partition

def qsort(start, end, data):
    if end > start:
        pivot = partition(start, end, data)
        qsort(start, pivot-1, data)
        qsort(pivot+1, end, data)

def qsort_three_way(start, end, data):
    if end > start:
        lt, gt = three_way_partition(start, end, data)
        qsort(start, lt-1, data)
        qsort(gt+1, end, data)

if __name__ == '__main__':
    print(" Hoare's Quick Sort")
    data = [4,6,5,1,8,3,5,2,5,9,7]
    print(data)
    qsort(0, len(data)-1, data)
    print(data)

    print("\nDijkstra Threeway Prtition/Dutch National Flag")
    data =[
        [1,0,0,0,0,0,1,0,1,0,1,0,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,0,1,0,1,1,0,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1],
        [1,2,3,4,1,2,4,1,2,4,1,2,3,4,2,1,3,4,2,3,4,2,3,1,4,3,2,1,4,1,2,4,3,1,2,4,1,2,4,1,2,3,4,2,1,3,4,1,2,4,3,2,1,4,2,3,4,2,3,1,4,2,3,4,2,3,4,2,4,2,1,3,1,3,1,4,1,2,3,1,3,1,2,4,1,3,1,3,1,4,2,1,3,1,4,1,4]
    ]
    qsort_three_way(0, len(data[0])-1, data[0] )
    qsort_three_way(0, len(data[1])-1, data[1] )
    for i in data: print(i)