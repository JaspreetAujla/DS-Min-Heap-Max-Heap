def min(M,n):
    l = left(n)
    r = right(n)
    if l < len(M) and M[l] < M[n]:
        smallest = l
    else:
        smallest = n
    if r < len(M) and M[r] < M[smallest]:
        smallest = r
    if smallest != n:
        M[n], M[smallest] = M[smallest], M[n]
        min(M, smallest)

def left(n):
    return 2 * n + 1

def right(n):
    return 2 * n + 2

def insert(M,  n):
    size = len(M)
    if size == 0:
        M.append(n)
    else:
        M.append(n)
        for i in range(size - 1, -1, -1):
           min(M, i)

def min(M,n):
    l = left(n)
    r = right(n)
    if l < len(M) and M[l] < M[n]:
        smallest = l
    else:
        smallest = n
    if r < len(M) and M[r] < M[smallest]:
        smallest = r
    if smallest != n:
        M[n], M[smallest] = M[smallest], M[n]
        min(M, smallest)

def left(n):
    return 2 * n + 1

def right(n):
    return 2 * n + 2

def insert(M,  n):
    size = len(M)
    if size == 0:
        M.append(n)
    else:
        M.append(n)
        for i in range(size - 1, -1, -1):
           min(M, i)

def display(M):
    print("Min-heap arr: " + str(M))

arr = []
insert(arr, 42)
insert(arr, 82)
insert(arr, 97)
insert(arr, 67)
insert(arr, 54)
display(arr)
