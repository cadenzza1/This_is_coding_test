k = int(input())

stack = []

for i in range(k):
    temp = int(input())
    if temp != 0:
        stack.append(temp)
    else:
        stack.pop()

print(sum(stack))