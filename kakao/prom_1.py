def no_repeat(arr):
    for t in range(1, len(arr)-1):
        for t2 in range(t+1, len(arr)):
            if arr[t] == arr[t2]:
                arr.pop(t2)

    return arr


def solution(id_list, report, k):
    answer = [0] * len(id_list)
    cnt_dict = {}
    for t in id_list:
        cnt_dict[t] = [0]
    for t in range(len(report)):
        report[t] = report[t].split()
    for rep in report:
        for t in range(1, len(rep)):
            cnt_dict[rep[0]].append(rep[t])
        cnt_dict[rep[0]] = no_repeat(cnt_dict[rep[0]])
    for key in cnt_dict.keys():
        for t in range(1, len(cnt_dict[key])):
            cnt_dict[cnt_dict[key][t]][0] += 1
    i = 0
    for val in cnt_dict.values():
        for t in range(1, len(val)):
            if cnt_dict[val[t]][0] >= k:
                answer[i] += 1
        i += 1

    return answer


report = ["ryan con", "ryan con", "ryan con", "ryan con"]
id_list = ["con", "ryan"]
print(solution(id_list, report, 2))