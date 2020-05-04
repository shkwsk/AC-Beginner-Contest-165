import itertools
import math

def dfs(vum,v,depth,max_depth,candidate,dupcombi):
    if depth == max_depth:
        dupcombi.append(candidate.copy())
    else:
        for u in vum[v]:
            candidate[depth] = u
            candidate, dupcombi = dfs(vum,u,depth+1,max_depth,candidate,dupcombi)
    return candidate, dupcombi

def main():
    N,M,Q = [int(x) for x in input().split()]
    m = []
    for i in range(Q):
        a,b,c,d = [int(x) for x in input().split()]
        m.append((a,b,c,d))

    # 数列列挙
    vum = {}
    for i in range(1,M+1):
        ul = []
        for j in range(i,M+1):
            ul.append(j)
        vum.update({i:ul})
    dupcombi = []
    candidate = [0]*N
    _, candA = dfs(vum,1,0,N,candidate,dupcombi)
    # print(len(list(itertools.product(range(1,M+1),repeat=N)))) // 重複あり順列
    # print(len(list(itertools.combinations_with_replacement(range(1,M+1),N)))) // 重複あり組み合わせ
    # print(len(candA)) // 重複あり組み合わせ (自作)

    scoreA = {}
    for cand in candA:
        score = 0
        for a,b,c,d in m:
            # print(a,b,c,d)
            if cand[b-1] - cand[a-1] == c:
                # print(cand[b-1],cand[a-1])
                score += d
        # print(cand,score)
        scoreA.update({score:cand})
    print(sorted(scoreA.items(), reverse=True)[0][0])

if __name__ == '__main__':
    main()
