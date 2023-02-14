def dfs(S):
    st = []
    st.append(S)
    visited[S] = 1
    while st:
        v = st.pop()
        for w in nodes[v]:
            if not visited[w]:
                st.append(w)
                visited[w] = 1


T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split()) #노드,간선
    nodes = [[] for _ in range(V + 1)]  #
    for _ in range(E):  # E개의 줄에 걸쳐 출발도착노드의 간선정보가 주어짐
        start, end = map(int, input().split())
        nodes[start].append(end)  # 출발노드와 도착노드 배열에 저장
    S, G = map(int, input().split())  # 확인용 출발노드S와 도착노드G가 주어진다
    visited = [ 0 for _ in range(V + 1)]  # 방문 확인용 배열생성
    # dfs(S, visited, nodes) #함수호출
    # answer = 0    #ans 값 초기화
    # if visited[G] == 1: #도착노드의 방문이 1일때
    #     answer = 1
    print(f'#{tc} {answer}')

