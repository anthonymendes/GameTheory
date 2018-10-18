# This is python code implementing the Simplex algorithm for games.
# This code will find one extreme optimal mixed strategy to a matrix game.
#
# CHANGE MATRIX A BELOW TO BE YOUR GAME MATRIX 
# Enter the decimal approximation for rational numbers; for example, use .5, not 1/2.

A = [[2,1,2],[1,4,1]]

# The output is a list of extreme optimal row strategies, column strategies, and value.

def gamesolution(A):
    m = min(A[0] + [0]) #used to make value > 0
    
    T = [[j-m+1 for j in A[i]]+[0]*i+[1]+[0]*(len(A)-i-1)+[1] for i in range(len(A))]
    T += [[-1]*len(A[0]) + [0]*(len(A)+1)] #initial tableau
 
    while min(T[-1]) < 0:
        c = T[-1].index(min(T[-1])) #pivot column

        ratios = []
        for i in T[:-1]:
            if i[c] > 0: ratios += [i[-1]/float(i[c])]
            else: ratios += ['inf']
        r = ratios.index(min(ratios)) #pivot row

        T[r] = [i/float(T[r][c]) for i in T[r]] 
        for i in range(len(T)):
            if i != r:
                T[i] = [T[i][j] - T[i][c]*T[r][j] for j in range(len(T[i]))] #pivot
                for j in range(len(T[i])): #watch out for roundoff errors
                    if abs(T[i][j]) < pow(10,-8): T[i][j] = 0

    v = 1/float(T[-1][-1])

    row = [v*i for i in T[-1][-len(A)-1:-1]]

    col = [0 for i in A[0]]
    for i in range(len(A)):
         c = map(list,zip(*T)).index([0]*i+[1]+[0]*(len(A)-i))
         if c < len(col): col[c] += v*T[i][-1]

    return [row,col,v+m-1]


for i in gamesolution(A):
    print i
