#재귀
#n! = n*(n-1)!
def factorial(n):
    if n == 1:
        return 1
    t = n * factorial(n-1)
    return t

print(factorial(5))

#n ** m = n**(m-1)
def mul(n,m):
    if m == 1:
        return n
    t = n *mul(n,m-1)
    return t

#피보나치
#0,1,1,2,3,5..
#fibo(n) = fibo(n-1)+fibo(n-2)
def fibo(n):
    if n == 0 or n==1:
        return n
    t1 = fibo(n-1)
    t2 = fibo(n-2)
    return t1 + t2
print(fibo(6))

#메모이제이션
#호출을 기억해 놓는 것
fi = [0] * 100
fi[0]=0
fi[1]=1
def fibo(n):
    if n>=2 and fi[n] == 0:이미 계산되어 있지 않으면
        t1 = fibo(n-1)
        t2 = fibo(n-2)
        fi[n] = t1+t2

    return fi[n]

print(fibo(6))

#2
def fibo(n):
    fi = [0] * 100
    fi[0] = 0
    fi[1] = 1
    for i in range(2, n + 1):
        fi[i] = fi[i - 1] + fi[i - 2]

    return fi[n]

#그래프 자료담기
#자료 연습문제3
V = 7+1 #(0번은 안씀)
S = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
S = S.split()
G= [[] for _ in range(V)]
print(S,G)
for idx in range(0,len(S),2):
    v1 = S[idx]
    v2 = S[idx+1]
    G[v1].append(v2)
    G[v2].append(v1)
print(G)

# G = [[],[2,3],[1,4,5],[1,7],[2,6],[2,6],[4,5,7],[3,6]]

V = 7+1 #(0번은 안씀)
S = '1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7'
S = S.split()
G= [[0,0,0,0,0,0,0,0],
    [0,0,1,1,0,0,0,0],
    [0,0,0,0,1,1,0,0],
    [0,1,0,0,0,0,0,1],
    [0,0,1,0,0,0,1,0],
    [0,0,1,0,0,0,1,0],
    [0,0,0,0,0,1,0,1],
    [0,0,0,1,0,0,0,1]]
G = [[0]*V for _ in range(V)]
for idx in range(0,len(S),2):
    v1 = s[idx]
    v2 = s[idx+1]
    G[v1][v2] = 1
    G[v2][v1] = 1
print(G)

#DFS알고리즘
G = [[],[2,3],[1,4,5],[1,7],[2,6],[2,6],[4,5,7],[3,6]]
def dfs(v):
    st = []
    visited = [False] * v
    st.append(v)
    visited[v] = True
    while st:
        v = st.pop()
            if v not in visited: #w가 안간길이면 방문
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
