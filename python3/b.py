import math

def main():
    X = int(input())
    ans = 0
    Y = 100
    while True:
        if Y >= X:
            print(ans)
            break
        Y = Y + math.floor(Y*0.01)
        ans += 1

if __name__ == '__main__':
    main()
