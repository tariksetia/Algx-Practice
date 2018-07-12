def twoStacks(x, a, b):
    #
    # Write your code here.
    #
    total = 0
    moves = 0
    while total < x:
        if a and b:
            if a[0]<=b[0]:
                total = total + a.pop(0)
                moves += 1
            else:
                total = total + b.pop(0)  
                moves += 1
        elif a:
            total = total +a.pop(0)
            moves += 1
        elif b:
            total = total +b.pop(0)
            moves += 1
        
    
    return moves-1

if __name__ == '__main__':
    a=[19,9,8,13,1,7,18,0,19,19,10,5,15,19,0,0,16,12,5,10]

    b = [11,17,1,18,14,12,9,18,14,3,4,13,4,12,6,5,12,16,5,11,16,8,16,3,7,8,3,3,0,1,13,4,10,7,14]
    x=67
    twoStacks(67,a,b)