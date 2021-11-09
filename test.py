a = []

for i in range(10):
    a.append({
        'num': f'{i} hello',
        'vote_average': i,
    })


movies = []
for t in range(len(temp)):
    movies.append(temp)


for t1 in range(len(movies)-1):
    maxi = t1
    for t2 in range(t1+1, len(movies)):
        if movies[maxi]['vote_average'] < movies[t2]['vote_average']:
            maxi = t2
    movies[maxi], movies[t1] = movies[t1], movies[maxi]


print(my_sort(a))