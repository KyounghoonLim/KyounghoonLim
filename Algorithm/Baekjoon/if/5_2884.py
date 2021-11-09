hour, minute = map(int, input().strip().split())

if minute < 45:
    hour -= 1
    minute = 60 - (45 - minute)
    if hour < 0:
        hour = 24 - 1
        print(hour, minute)
    else:
        print(hour, minute)
else:
    minute -= 45
    print(hour, minute)
