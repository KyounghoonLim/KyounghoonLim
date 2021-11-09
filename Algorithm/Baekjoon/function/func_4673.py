def self_num():
    self_n = set()
    i = 0
    while i < 10000:
        sigma = i
        for t in str(i):
            if sigma > 10000:
                break
            sigma += int(t)
        self_n.add(sigma)
        i += 1
    self_n = list(self_n)
    j, p = 1, 1
    while j <= 10000:
        if j == self_n[p]:
            p += 1
            j += 1
            continue
        else:
            print(j)
            j += 1


self_num()