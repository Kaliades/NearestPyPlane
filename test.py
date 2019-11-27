import math


def bin_search(T, A):
    L = 0
    R = len(A)
    points = []
    while L < R:
        m = math.floor((L + R) / 2)
        if A[m] > T:
            R = m
        else:
            L = m + 1
    points.append(L)
    points.append(L-1)

    check1 = T - A[points[0]]
    check2 = T - A[points[1]]

    if check1 == check2:
        #print("The program found two same geodesic coordinates")
        result = [check1, check2]

    elif check1 > check2:
        result = check2
        #print("The program found one correct geodesic coordinate")
    else:
        result = check1
        #print("The program found one correct geodesic coordinate")


    return result



print(bin_search(16, [1,2,3,4,5,6,7,8]))

