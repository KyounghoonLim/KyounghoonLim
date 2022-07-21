import copy


def cube_rotate(cube, order, d):
    ref = copy.deepcopy(cube)
    fixed_idx, rule = rules[order]
    if d == '+':
        rule.reverse()

    for i in range(3):
        for j in range(4):
            if order in ['U', 'D']:
                cube[rule[j]][fixed_idx][i] = ref[rule[(j + 1) % 4]][fixed_idx][i]
            elif order in ['L', 'R']:
                w = weight[rule[j]]
                cube[rule[j]][abs(i - w)][abs(fixed_idx - w)] = ref[rule[(j + 1) % 4]][abs(i - w)][abs(fixed_idx - w)]
            else:
                if rule[j] in ['L', 'R']:
                    cube[rule[j]][i][abs(fixed_idx - 2)] = ref[rule[(j + 1) % 4]][fixed_idx][i]
                else:
                    cube[rule[j]][fixed_idx][i] = ref[rule[(j + 1) % 4]][i][abs(fixed_idx - 2)]

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
    'B': 0
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