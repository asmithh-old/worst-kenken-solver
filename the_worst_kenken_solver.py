import random, numpy as np, itertools
#n is dimension of grid

def solver(n):
    rows = ['R' + str(r) for r in range(1, n+1)]
    cols = ['C' + str(c) for c in range(1, n+1)]
    cells = [r + c for (r,c) in itertools.product(rows, cols)]
    row_constraint = [r + '#' + str(n) for (r, n) in itertools.product(rows, range(1, n+1))]
    col_constraint = [c + '#' + str(n) for (c, n) in itertools.product(cols, range(1, n+1))]
    print row_constraint[7:10]
    print cells[8:10]
    bipartite_lr = {}
    for r in row_constraint:

        bipartite_lr[r] = set([r[:2] + c + '#' +r[-1] for c in cols])
        print r
        print bipartite_lr[r]
    bipartite_rl = {}

solver(5)
