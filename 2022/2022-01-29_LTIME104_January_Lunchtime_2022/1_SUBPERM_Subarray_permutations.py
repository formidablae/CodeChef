import itertools


def isPermOfLenN(arr, n):
    if len(arr) != n:
        return False
    # create an empty set
    s = set()
    for i in range(n):
        if arr[i] > n or arr[i] < 1:
            return False
        # check if the element is present in the set else add it
        if arr[i] in s:
            return False
        else:
            s.add(arr[i])
    return True

def countGoodSubsegmentsEqualK(arr, n, k):
    count = 0
    for i in range(n):
        if count > k:
            return False
        for j in range(i, n):
            if count > k:
                return False
            if isPermOfLenN(arr[i:j + 1], j - i + 1):
                count += 1
    return count == k

def getPermutationOfLenNWithKSubsegments(n, k):
    perms = itertools.permutations(range(1, n + 1), n)
    for perm in perms:
        listPerm = list(perm)
        if countGoodSubsegmentsEqualK(listPerm, n, k):
            return listPerm
    return [-1]
    
T = int(input())
for tc in range(T):
    N, K = map(int, input().split())
    print(*getPermutationOfLenNWithKSubsegments(N, K))
    # TLE
    # solution to be optimized
