"""Решение задачи 1363С"""
for _ in range(int(input())):
    A = []
    n, x = map(int, input().split(sep=' '))
    if n > 1:
        for _ in range(n-1):
            u, v = input().split(sep=' ')
            A.append(u)
            A.append(v)
        if A.count(f'{x}') == 1:
            print('Ayush')
        else:
            if n % 2 == 0:
                print('Ayush')
            else:
                print('Ashish')
    else:
        print('Ayush')
