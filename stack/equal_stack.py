def equalStacks(h1, h2, h3):
    #
    # Write your code here.
    #
    all_stack = bool(h1) and bool(h2) and bool(h3)
    equal_sum = sum(h1) == sum(h2) == sum(h3)
    
    while not equal_sum:
        
        if sum(h1) > sum(h2) and sum(h1) > sum(h3):
            h1.pop(0)
        elif sum(h2) > sum(h1) and sum(h2) > sum(h3):
            h2.pop(0)
        elif sum(h3) > sum(h1) and sum(h3) > sum(h2):
            h3.pop(0)
        equal_sum = sum(h1) == sum(h2) == sum(h3)

    return sum(h1)
if __name__ == '__main__':
    a = [3, 2, 1, 1, 1]
    b = [4, 3, 2]
    c = [1, 1, 4, 1]
    equalStacks(a,b,c)