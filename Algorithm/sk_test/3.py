def facto(num):
    fac = num
    for n in range(n-1, -1, -1):
        fac *= n

    return fac


def solution(width, height, diagonals):
    answer = 0
    for slash in diagonals:
        way_1 = facto((slash[1] + 1) + slash[0])/facto(slash[1] + 1) * facto(slash[0])
        way_2 = facto(slash[1] + (slash[0] + 1))/facto(slash[1]) * facto(slash[0] + 1)
        way_3 = facto(slash[1] + slash[0])/facto(slash[1]) * facto(slash[0])

        

    return answer