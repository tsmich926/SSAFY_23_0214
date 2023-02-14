
while (True):
        a = input()
        print(a)
        n = len(a)
        lst = []
        for i in range(n-1,-1,-1):
            lst.append(a[i])
        lst_str = str(lst)[1:-1]
        print(lst_str)
        #리스트에서 수 꺼내서 원래의 입력과 비교
        if lst_str == a:
            print('yes')
        else:
            print('no')

#다른 풀이
while True:
    n = input()
    stack = []
    res = ''
    if n == '0':
        break
    else:
        for i in n:
            stack.append(i)
        for i in range(len(stack)):
            res += stack.pop()
        if res == n:
            print('yes')
        else:
            print('no')


#다른 풀이
https://wondytyahng.tistory.com/47
