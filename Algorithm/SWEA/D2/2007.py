T = int(input())
user_input = []
for test_case in range(T):
    user_input.append(input())

ans = []

for words in user_input:
    for i in range(1, len(words) // 2):
        word = words[0:i]
        if word * (len(words) // (i)) in words:
            ans.append(word)
            break
            
for i in range(len(ans)):
    print(f'#{i+1} {len(ans[i])}')
