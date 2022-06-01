for t in range(int(input())):
    pA, pB, qA, qB = map(int, input().split())
    if max(pA,pB) == max(qA,qB): print('TIE')
    elif max(pA,pB) < max(qA,qB): print('P')
    else: print('Q')