import math

def dijkstra(s,n,w,cost):
    #始点sから各頂点への最短距離
    #n:頂点数,　w:辺の数, cost[u][v] : 辺uvのコスト(存在しないときはinf)
    d = [float("inf")] * n
    used = [False] * n
    d[s] = 0
    
    while True:
        v = -1
        #まだ使われてない頂点の中から最小の距離のものを探す
        for i in range(n):
            if (not used[i]) and (v == -1):
               v = i
            elif (not used[i]) and d[i] < d[v]:
                v = i
        if v == -1:
               break
        used[v] = True
               
        for j in range(n):
               d[j] = min(d[j],d[v]+cost[v][j])
    return d

def main():
    N,M,Q = [int(x) for x in input().split()]
    m = {}
    for i in range(Q):
        a,b,c,d = [int(x) for x in input().split()]
        if d == 0:
            continue
        m.update({d: (a,b,c)})

    p = 0
    A = [0]*N
    for d,(a,b,c) in sorted(m.items(), reverse=True):
        # print(d,a,b,c)
        if A[b-1] == 0 and A[a-1] == 0:
            A[b-1] = M
            A[a-1] = M - c
            p += d
            # print('1',d)
            continue
        if A[b-1] == 0:
            A[b-1] = A[a-1] + c
            p += d
            # print('2',d)
            continue
        if A[a-1] == 0:
            A[a-1] = A[b-1] - c
            p += d
            # print('3',d)
            continue
        if A[b-1] - A[a-1] == c:
            p += d
            # print('4',d)
            continue
    p2 = 0
    A = [0]*N
    for d,(a,b,c) in sorted(m.items()):
        if A[b-1] == 0 and A[a-1] == 0:
            A[b-1] = M
            A[a-1] = M - c
            p2 += d
            # print('1',d)
            continue
        if A[b-1] == 0:
            A[b-1] = A[a-1] + c
            p2 += d
            # print('2',d)
            continue
        if A[a-1] == 0:
            A[a-1] = A[b-1] - c
            p2 += d
            # print('3',d)
            continue
        if A[b-1] - A[a-1] == c:
            p2 += d
            # print('4',d)
            continue
    if p >= p2:
        print(p)
    else:
        print(p2)

if __name__ == '__main__':
    main()
