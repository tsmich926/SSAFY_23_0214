def dfs(S,E):
    st = []
    visited = [False] * (V+1)  #노드가 1에서부터 시작하므로 0번 인덱스가 있다고 보고 V+1을 한다

    st.append(S)
    visited[S] = True
    while st:
        v = st.pop()
        if v == E:
            return 1
        #print(v)
        for w in G[v]:
            if not visited[w]:
                st.append(w)
                visited[w]=True

T = int(input())
for tc in range(1,T+1):
    V,E = map(int,input().split()) #노드,간선


    #1.G를 생성

    #2. dfs(S)

    def dfs(S, E):
        st = []
        visited = [False] * (V + 1)

        st.append(S)
        visited[S] = True
        while st:
            v = st.pop()
            # if v == E:
            #     return 1
            # print(v)
            for w in G[v]:
                if not visited[w]:
                    if w == E:
                        return 1
                    st.append(w)
                    visited[w] = True
