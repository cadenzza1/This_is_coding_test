docu = list(input())
wanna_find = list(input())

l = len(wanna_find)
cnt = 0
index = 0

for i in range(len(docu) - l):
    if docu[index:index+l] == wanna_find:
        cnt += 1
        index += l
    else:
        index += 1

print(cnt)