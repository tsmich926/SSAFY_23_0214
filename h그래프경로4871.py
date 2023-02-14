def dfs(S, visited, nodes):
    st = []
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


T = int(input())
for tc in range(1,TC+1):
    V,E = map(int,input().split())
    nodes = [[] for _ in range(V + 1)]  #
    for _ in range(E):  # E개의 줄에 걸쳐 출발도착노드의 간선정보가 주어짐
        start, end = map(int, input().split())
        nodes[start].append(end)
    S, G = map(int, input().split())  # 확인용 출발노드S와 도착노드G가 주어진다
    visited = [0 for _ in range(V + 1)]  # 방문 확인용 배열생성
    dfs(S, visited, nodes)
    answer = 0
    if visited[G] == 1:
        answer = 1
    print('#{} {}'.format(t + 1, answer))



def dfs(node_index, visited, nodes):
    visited[node_index] = 1
    for node in nodes[node_index]:
        if visited[node] != 1:
            dfs(node, visited, nodes)


for t in range(int(input())):
    V, E = map(int, input().split())
    nodes = [[] for _ in range(V + 1)] #
    for _ in range(E): # E개의 줄에 걸쳐 출발도착노드의 간선정보가 주어짐
        start, end = map(int, input().split())
        nodes[start].append(end)
    S, G = map(int, input().split())  # 확인용 출발노드S와 도착노드G가 주어진다
    visited = [0 for _ in range(V + 1)] #방문 확인용 배열생성
    dfs(S, visited, nodes)
    answer = 0
    if visited[G] == 1:
        answer = 1
    print('#{} {}'.format(t + 1, answer))



def dfs(start, end):
    stack = []
    visit = [False] * (V+1)
    stack.append(start)
    # 입력받은 start부터 시작, 값이 있고 아직 방문하지 않은 정점이면 stack에 추가
    while stack:
        v = stack.pop()
        visit[v]=True
        for w in range(V+1):
            if not visit[w]:
                if arr[v][w]:
                    stack.append(w)
    # end 지점을 방문하였는지 반환
    return visit[end]
#테스트 케이스 수 입력
T = int(input())
for tc in range(1, T+1):
    #정점과 간선의 개수 입력
    V, E = map(int,input().split())
    arr = [[0] *(V+1) for _ in range(V+1)]
    #arr에 입력받은 연결된 정점 표시
    for _ in range(E):
        x, y = map(int,input().split())
        arr[x][y] = 1
    result = 1
    #입력받은 a가 b에 연결되어있는지 확인
    a, b= map(int,input().split())
    if not dfs(a,b):
        result = 0
    print(f'#{tc} {result}'))




    def dfs(v):
        visited[v] = True
        for j in lst[v]:
            if not visited[j]:
                dfs(j)


    T = int(input())

    for tc in range(1, T + 1):
        V, E = map(int, input().split())
        lst = [[] for _ in range(V + 1)]
        visited = [False] * (V + 1)
        for i in range(E):
            start, end = map(int, input().split())
            lst[start].append(end)

        S, G = map(int, input().split())
        dfs(S)

        if not visited[G]:
            print(f'#{tc} 0')
        else:
            print(f'#{tc} 1')