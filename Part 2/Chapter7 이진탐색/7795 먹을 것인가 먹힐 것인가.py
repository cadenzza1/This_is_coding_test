import sys
input = sys.stdin.readline

def binary(array,target,start,end):
    total = 0
    mid = (start+end) // 2

    

t = int(input())
n,m = map(int,input().split()) # a의 수 n, b의 수 m

for i in range(t):
    a_arr = list(map(int,input().split()))
    b_arr = list(map(int,input().split()))
    
    a_arr.sort()
    b_arr.sort()
