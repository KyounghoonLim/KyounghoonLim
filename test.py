import json

import requests
import pprint

result = []
n = 1
while n < 200:
    n += 1
    ### 장르 가져오기 ###
    # r = requests.get(f'https://api.themoviedb.org/3/genre/movie/list?api_key=d23456a72d11547629c9720c034aecb5&language=ko-KR').json()

    # # pprint.pp(r)
    # for t in r['genres']:
    #     print(t)
    #     genre = {
    #         'model': 'movies.genre',
    #         'pk': t['id'],
    #         'fields': {
    #             'name': t['name']
    #         }
    #     }
    #     result.append(genre)

    ### 영화 가져오기 ###
    r = requests.get(f'https://api.themoviedb.org/3/movie/popular?api_key=d23456a72d11547629c9720c034aecb5&language=ko-KR&page={n}').json()

    if len(r) < 4:
        continue

    for t in r['results']:
        flag = 0
        pprint.pp(t)
        try:
            if len(t['release_date']) < 5:
                continue
            movie = {
                'model': 'movies.movie',
                'fields': {
                    'title': t['title'],
                    'overview': t['overview'],
                    'vote_average': t['vote_average'],
                    'poster_path': t['poster_path'],
                    'genres': t['genre_ids'],
                    'release_date': t['release_date']
                }
        }
        except:
            continue
        # if result:
        #     for t2 in result:
        #         if t2['fields']['title'] == movie['fields']['title']:
        #             flag = 1
        #             break
        if not flag:
            result.append(movie)


### 가져온 정보 갯수 ###
print(len(result))

### 가져온 정보 json으로 dump ###
with open('movies.json', 'w', encoding="utf-8") as make_file:
    json.dump(result, make_file, ensure_ascii=False, indent="\t")