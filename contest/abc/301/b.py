N = int(input())
A = [*map(int ,input().split())]

for i in range(N-1):
    print(A[i], end=' ')
    if abs(A[i] - A[i+1]) > 1:
        if A[i] < A[i+1]:
            for j in range(A[i]+1, A[i+1]):
                print(j, end = ' ')
        else:
            for j in range(A[i]-1, A[i+1], -1):
                print(j, end = ' ')
print(A[-1])