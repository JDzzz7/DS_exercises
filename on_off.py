def end_product(start: list, days: int)->list:
    temp = start[:]
    for i in range(days):
        start = temp[:]
        for j in range(len(start)):
            if j == 0:
                temp[j] = 0
                continue
            if j == (len(start)-1):
                temp[j] = 0
                break
            if start[j-1] == start[j+1]:
                temp[j] = 0
            if start[j-1] != start[j+1]:
                temp[j] = 1
    return temp

if __name__ == '__main__':
    begin = [1, 1, 1, 0, 0, 1, 0, 0, 1]
    num = 3
    print(end_product(begin, num))

# 1, 1, 1, 0, 0, 1, 0, 0, 1 <--Given
# 0, 0, 1, 1, 1, 0, 1, 1, 0
# 0, 1, 1, 0, 1, 0, 1, 1, 0
# 0, 1, 1, 0, 0, 0, 1, 1, 0 <--Ans
