user_input = []
user_input.append(list(map(int,input().split())))

for i in user_input:
    i.sort()
    print(i[len(i)//2])