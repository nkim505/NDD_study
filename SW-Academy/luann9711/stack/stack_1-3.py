import sys

# 테스트 케이스 입력
try:
    t = int(input('테스트 케이스 입력 : '))

except ValueError:
    print('ValueError : Wrong Number!!')

if not(1 <= t <= 50):
    raise ValueError

c = t + 1

def push(stack, n):
    stack.append(n)

def pop(stack):
    return stack.pop()

while t > 0:
    try:
        v, e = map(int, input('노드 수와 간선 수를 입력 : ').split())

    except ValueError:
        print('ValueError : Wrong Number!!')

    if not(5 <= v <= 50) or not(4 <= e <= 1000):
        raise ValueError

    stack = []
    visted = [False for _ in range(v + 1)]
    way_list = [[] for _ in range(v + 1)]

    def dfs(x):
        visted[x] = True
        push(stack, x)

        for y in way_list[x]:
            if visted[y] == False:
                dfs(y)
            
            if y == b:
                return True
    
    # e 의 갯수 만큼 출발노드와 도착노드의 간선정보를 입력받는다.
    for _ in range(e):
        a, b = map(int, input('출발노드와 도착노드의 간선정보를 입력 : ').split())
        way_list[a].append(b)
        way_list[b].append(a)
        print(way_list)
    
    for e in way_list:
        e.sort()
    
    # 존재를 확인 할 출발노드와 도착노드의 간선정보를 입력받는다.
    s, g = map(int, input('존재를 확인할 출발노드와 도착노드의 루트를 입력 : ').split())
    
    if dfs(a) == True:
        print(f'#{c - t} {1}')
    else:
        print(f'#{c - t} {0}')

    t -= 1