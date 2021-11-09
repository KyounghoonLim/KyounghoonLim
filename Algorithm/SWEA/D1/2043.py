user_input = (input())
input_list = user_input.split()
P, K = int(input_list[0]), int(input_list[1])

count = 1

while True:
    if P == K:
        break
    else:
        K += 1
        count +=1

print(count)
