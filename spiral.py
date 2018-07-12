def spiral(n):
    cstart, cend, rstart, rend = 0, n-1, 0, n-1

    while cstart <= cend and rstart <=rend:
        
        for i in range(cstart,cend+1):
            yield (rstart,i)
        rstart += 1

        for i in range(rstart, rend+1):
            yield (i,cend)
        cend -= 1

        for i in range(cend,cstart-1,-1):
            yield (rend,i)
        rend -= 1

        for i in range(rend,rstart-1,-1):
            yield (i,cstart)
        cstart += 1

    
if __name__ == '__main__':
    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    matrix = [[0]*4,[0]*4,[0]*4,[0]*4]
    for i in matrix: print(i)

    for pos,val  in zip(spiral(4),raw_input()):
        x,y = pos
        matrix[x][y] = val

    for i in matrix: print(i)
