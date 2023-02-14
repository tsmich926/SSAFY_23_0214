# f(i,k) #i단계,k목표
#     if i == k:
#         print(B) #목표도달
#         return
#     else:
#         B[i] = A[i]
#         f(i+1,k) #다음 단계
#
# A = [10,20,30]
# B = [0] * 3
# f(0,3)

#DFS
#인접행렬
V ,E = map(int,input().split())
adjm = [[0]*(V+1) for _ in range(V+1)]
adjL = [[] for _ in range(V+1)]

for _ in range(E):
    V1,V2 = arr[i*2],arr[i*2+1]
    adjm[V1][V2] = 1
    adjm[V2][V1] = 1
    adjL[V1].append(V2)
    adjL[V2].append(V1)

