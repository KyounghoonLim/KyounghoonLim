import copy


def cube_rotate_plane(cube, order, d):
    plane = cube[order]
    result = [[0] * 3 for _ in range(3)]
    if d == '+':
        for i in range(3):
            for j in range(3):
                result[j][2 - i] = plane[i][j]
    else:
        for i in range(3):
            for j in range(3):
                result[2 - j][i] = plane[i][j]
    cube[order] = result


def cube_rotate(cube, order, d):
    ref = copy.deepcopy(cube)
    idx, rule = rules[order]
    if d == '+':
        rule = list(reversed(rule))

    for i in range(3):
        for j in range(4):
            if order in ['U', 'D']:
                cube[rule[j]][idx][i] = ref[rule[(j + 1) % 4]][idx][i]
            elif order in ['L', 'R']:
                w_my, w_target = weight[rule[j]], weight[rule[(j + 1) % 4]]
                cube[rule[j]][abs(i - w_my)][abs(idx - w_my)] = ref[rule[(j + 1) % 4]][abs(i - w_target)][abs(idx - w_target)]
            else:
                w_my, w_target = weight[rule[j]], weight[rule[(j + 1) % 4]]
                if rule[j] in ['L', 'R']:
                    cube[rule[j]][i][abs(idx - w_my)] = ref[rule[(j + 1) % 4]][abs(idx - w_target)][i]
                else:
                    cube[rule[j]][abs(idx - w_my)][i] = ref[rule[(j + 1) % 4]][i][abs(idx - w_target)]

    cube_rotate_plane(cube, order, d)

    return cube


def cube_game(cube, orders):
    for order in orders:
        cube_rotate(cube, order[0], order[1])

    return cube['U']


rules = {
    'U': [0, ['L', 'B', 'R', 'F']],
    'D': [2, ['F', 'R', 'B', 'L']],
    'L': [0, ['U', 'F', 'D', 'B']],
    'R': [2, ['B', 'D', 'F', 'U']],
    'F': [2, ['U', 'R', 'D', 'L']],
    'B': [0, ['L', 'D', 'R', 'U']]
}

weight = {
    'U': 0,
    'D': 2,
    'F': 0,
    'B': 2,
    'L': 0,
    'R': 2
}

for tc in range(int(input())):
    N = int(input())
    test_case = input().split()
    init_cube = {
        'U': [['w'] * 3 for _ in range(3)],
        'D': [['y'] * 3 for _ in range(3)],
        'L': [['g'] * 3 for _ in range(3)],
        'R': [['b'] * 3 for _ in range(3)],
        'F': [['r'] * 3 for _ in range(3)],
        'B': [['o'] * 3 for _ in range(3)]
    }

    result = cube_game(init_cube, test_case)

    for i in range(3):
        print(''.join(result[i]))