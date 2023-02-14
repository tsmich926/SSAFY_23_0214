# #자료 연습문제3
# V = 7+1 #(0번은 안씀)
# S = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
# S = S.split()
# G= [[] for _ in range(V)]
# print(S,G)
# for idx in range(0,len(S),2):
#     v1 = S[idx]
#     v2 = S[idx+1]
#     G[v1].append(v2)
#     G[v2].append(v1)
# print(G)
#
# # G = [[],[2,3],[1,4,5],[1,7],[2,6],[2,6],[4,5,7],[3,6]]
#
# V = 7+1 #(0번은 안씀)
# S = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
# S = S.split()
# G= [[0,0,0,0,0,0,0,0],
#     [0,0,1,1,0,0,0,0],
#     [0,0,0,0,1,1,0,0],
#     [0,1,0,0,0,0,0,1],
#     [0,0,1,0,0,0,1,0],
#     [0,0,1,0,0,0,1,0],
#     [0,0,0,0,0,1,0,1],
#     [0,0,0,1,0,0,0,1]]
# G = [[0]*V for _ in range(V)]
# for idx in range(0,len(S),2):
#     v1 = s[idx]
#     v2 = s[idx+1]
#     G[v1][v2] = 1
#     G[v2][v1] = 1
# print(G)

#DFS알고리즘
G = [[],[2,3],[1,4,5],[1,7],[2,6],[2,6],[4,5,7],[3,6]]
def dfs(v):
    st = []
    visited = [False] * v
    st.append(v)
    visited[v] = True
    while st:
        for w in G[v]:
            if not visited[w]: #w가 안간길이면 방문
                visited[w] = True
                #돌아오기 위해 v를 스택에 저장
                st.append(v)
                v = w
                break
        else:
            v = st.pop()

    pass

#방법2
def dfs(v):
    st = []
    visited = [False]*v
    st.append(v)
    while st:
        v = st.pop()
        if not visited[v]:
            visited[v] = True
        for w in G[v]:
            if not visited[w]:
                st.append(w)


def dfs(v):
    st = []
    visited = [False]*v
    st.append(v)
    while st:
        v = st.pop()
        for w in G[v]:
            if not visited[w]:
                st.append(w)
                visited[w] = True

#재귀
visited = [False]*v
def dfsr(v):
    print(v)
    visited(v) = True
    for w in G[v]:
        if not visited[w]:
            dfsr(w)

def dfs(v):
    st = []
    visited = [False]*v

    st.append(v)
    visited[v] = True
    while st:
        v = st.pop()
        print(v)
        # for w in G[v]:
        for w in range(v):
            if G[v][w] and not visited[w]:
                st.append(w)
                visited[w] = True


