# This is python3 code implementing the Simplex algorithm for zero sum matrix games.  It
# will find one extreme optimal mixed strategy to a matrix game.
#
# The input is a zero sum game matrix.  The output is a list [r,c,v] where r is an optimal
# row strategy, c is an extreme optimal column strategy, and v is the value of the game.

def gamesolution(A):

    m, n = len(A), len(A[0])

    # pad entries to ensure that the value is positive and create initial tableau
    p = min(A[0] + [0])
    T = [[j-p+1 for j in A[i]]+[0]*i+[1]+[0]*(m-i-1)+[1] for i in range(m)]
    T += [[-1]*n + [0]*(m+1)]

    # implement simplex algorithm
    while min(T[-1]) < 0:

        # find pivot column c
        c = T[-1].index(min(T[-1]))
        
        # find pivot row r
        ratios = [i[-1]/float(i[c]) if i[c] > 0 else 'inf' for i in T[:-1]]
        r = ratios.index(min([a for a in ratios if a != 'inf']))

        # perform pivot
        T[r] = [i/float(T[r][c]) for i in T[r]] 
        for i in range(m + 1):
            if i != r:
                T[i] = [T[i][j] - T[i][c]*T[r][j] for j in range(m + n + 1)]
                #watch out for roundoff errors
                for j in range(m + n + 1): 
                    if abs(T[i][j]) < pow(10,-8): T[i][j] = 0

    # get strategies from final tableau
    v = 1/float(T[-1][-1])

    row = [v*i for i in T[-1][-m-1:-1]]

    col = [0 for i in A[0]]
    for i in range(m):
        c = list(zip(*T)).index(tuple([0]*i+[1]+[0]*(m-i)))
        if c < len(col):
            col[c] += v*T[i][-1]

    return [row, col, v+p-1]

# Below is an example of calling gamesolution.

print(gamesolution([[2,1,2],[1,4,1]]))
