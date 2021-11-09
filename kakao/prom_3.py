def solution(fees, records):
    answer = []
    park_dict = {}
    for t in range(len(records)):
        records[t] = records[t].split()
        park_dict[records[t][1]] = 0
    for key in park_dict.keys():
        i, o = 0, 0
        for car in records:
            if car[1] == key:
                if car[2] == 'IN':
                    i += int(car[0][:2]) * 60
                    i += int(car[0][3:])
                elif car[2] == 'OUT':
                    o += int(car[0][:2]) * 60
                    o += int(car[0][3:])
                    park_dict[key] += o - i
                    i, o = 0, 0
            elif i and car == records[len(records)-1]:
                park_dict[key] += 1439 - i
    for key in park_dict.keys():
        temp = park_dict[key] - fees[0]
        if temp < 0:
            temp = 0
        temp2 = temp // fees[2]
        if temp2 % fees[2]:
            temp2 += 1
        answer.append(fees[1] + temp2 * fees[3])

    return answer


fee = [180, 5000, 10, 600]
record = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT",
          "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
          "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
print(solution(fee, record))