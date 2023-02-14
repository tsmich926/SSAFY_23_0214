def paper(cm):
    if cm == 1 or cm == 0:
        return 1
    else:
        t = paper(cm-1) + 2*paper(cm-2)
        return t

        # return paper(cm-1) + 2*paper(cm-2)

T = int(input())
for tc in range(1,T+1):
    N = int(input())
    cm = N//10
    ans = paper(cm)
    print(f'{tc} {ans}')
