######upper 메소드 쓰는 방법######
# user_input = input()
# ans = user_input.upper()

# print(ans)
######반복문 돌리는 방법######
user_input = input()
ans = ''
for i in user_input:
    if ord(i) > 96 and ord(i) < 123:
        ans += chr(ord(i)-32)
    else:
        ans += i

print(ans)