docu = input()
wanna_find = input()

cnt = 0 # 문서 내에 찾고자 하는 단어의 개수
idx = 0

while wanna_find in docu:
    docu = docu.replace(wanna_find,'',1)
    cnt += 1

print(cnt)

