def binary_search(data,value):
    
    low, high = 0, len(data)-1

    while low <= high:
        mid = (low+high)//2
        if data[mid] == value:
            return mid
        elif data[mid] > value:
            high = mid-1
        elif data[mid] < value:
            low = mid +1
    
    return None



if  __name__ == '__main__':
    data = [23,45,67,89,234,345,456,567,689,2424,675757,678688]
    print(binary_search(data, 234))
    print(binary_search(data, 12))
