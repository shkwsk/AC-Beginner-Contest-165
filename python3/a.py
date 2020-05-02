def main():
    K = int(input())
    A,B = [int(x) for x in input().split()]
    for a in range(A,B+1):
        if a % K == 0:
            print('OK')
            return
    print('NG')

if __name__ == '__main__':
    main()
