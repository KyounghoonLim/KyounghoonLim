def move(pos, arrow):
    if arrow == 'U' and pos[0] > 0:
        pos[0] -= 1
    elif arrow == 'D' and pos[0] < 10:
        pos[0] += 1
    elif arrow == 'L' and pos[1] > 0:
        pos[1] -= 1
    elif arrow == 'R' and pos[1] < 10:
        pos[1] += 1

    return pos


def rev(do):
    if do == 'U': return 'D'
    elif do == 'D': return 'U'
    elif do == 'L': return 'R'
    else: return 'L'


def solution(dirs):
    answer = 0
    pos = [5, 5]
    Map = [[[] for _ in range(11)] for _ in range(11)]
    for do in dirs:
        next_pos = move(pos.copy(), do)
        print(pos, next_pos)
        if (next_pos[0] != pos[0] or next_pos[1] != pos[1]) and\
                do not in Map[next_pos[0]][next_pos[1]] and rev(do) not in Map[pos[0]][pos[1]]:
            Map[next_pos[0]][next_pos[1]].append(do)
            answer += 1
        pos = next_pos

    return answer

print(solution('UD'))