def solution(A):

    l = [0] * (len(A)+1)

    for i in A:
        if 0 >= i or i > len(A):
            continue
        l[i-1] = 1
    
    return l.index(0)+1


def solution(A):
    m = len(A)
    a = [0] *m

    for i in A:
        if 0 < i < m+1:
            a[i-1] =1
    try:
        return a.index(0)+1
    except :
        return len(A)+1