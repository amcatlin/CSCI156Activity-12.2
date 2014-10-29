__author__ = 'Alicia'

L = [[1, 2], [1, -1], [5, 8], [-4, -2], [4, 3], [8, 1]]  #1

M = []
for pair in L:
    M.append((max(pair), pair))
M.sort(reverse=True)
print(M)
L = []
for max, pair in M:  # if there is a tie in the max it will look at the first element in the pair and will use the one
    L.append(pair)  # with the largest value first. If those are the same it will move on the the next element and so on.
print(L)
