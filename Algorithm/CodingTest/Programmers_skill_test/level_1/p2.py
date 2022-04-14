def solution(numbers, hand):
    answer = ''
    keyboard = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    L, R = [3, 0], [3, 2]
    for n in numbers:
        pos = False

        for i in range(4):
            if pos:
                break
            for j in range(3):
                if n == keyboard[i][j]:
                    pos = [i, j]
                    break

        if n in [1, 4, 7, '*']:
            answer += 'L'
            L = pos
        elif n in [3, 6, 9, '#']:
            answer += 'R'
            R = pos
        else:
            d = abs(pos[0] - L[0]) + abs(pos[1] - L[1]) - (abs(pos[0] - R[0]) + abs(pos[1] - R[1]))
            if d > 0:
                answer += 'R'
                R = pos
            elif d == 0:
                if hand == 'right':
                    answer += 'R'
                    R = pos
                else:
                    answer += 'L'
                    L = pos
            else:
                answer += 'L'
                L = pos

    return answer