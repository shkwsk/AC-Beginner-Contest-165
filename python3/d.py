import math

def calc(a,b,x):
    return math.floor(a*x/b) - a*math.floor(x/b)
    
def main():
    A,B,N = [int(x) for x in input().split()]
    if N < B:
        print(calc(A,B,N))
    else:
        print(calc(A,B,B-1))

if __name__ == '__main__':
    main()
