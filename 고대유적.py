#####수정하자

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr = [[input().split()] for _ in range(M)]
    nr = [0,1]
    nc = [1,0]
    for row in range(N):
        for col in range(M):
            cnt = 0 #컬럼이 바뀔때마다 cnt갯수는 초기화
            if arr[row][col] == 1:
                cnt +=1
                if 0 <= row+nr[1] <N and 0 <= col+nc[1] <N:       #세로에 1이 있는지 검사
                    while arr[row+nr[1]][col+nc[1]]==1:
                        cnt += 1
                if 0 <= col+nc[0] <N and 0 <= row+nr[0] <N:
                    while arr[row+nr[1]][col+nc[1]]==1:   #가로에 1이 있는지 검사
                        cnt += 1
    print(cnt)