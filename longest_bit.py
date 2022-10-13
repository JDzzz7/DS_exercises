# 0000011101000
def count_bits(strArray: list)->list:
    maxcount = 0
    count = 1
    for i in range(len(strArray)):
        if i != (len(strArray)-1):
            print(f"i:{i} strArray[i]: {strArray[i]}")
            nxt = strArray[i+1]
            if strArray[i] != nxt:
                print(f"i+1:{i+1}")
                strArray = strArray[i+1:]  
                break
    if len(strArray) == 0:
        return 0
    for j in range(len(strArray)-1, -1, -1): # start, step, end
        if j != 0:
            print(f"j:{j} strArray[j]: {strArray[j]}")
            prev = strArray[j-1]
            if (strArray[j] != prev):
                strArray = strArray[:j]
                print("Am I here papi?")
                break
        else:
            print("Are we there yet?")
            strArray = []
            
    if len(strArray) == 0:
        return 0
    print(strArray)
    for z in range(len(strArray)):
        if z != (len(strArray)-1):
            n = strArray[z+1]
            if strArray[z] != n:
                if count > maxcount:
                    maxcount = count
                    count = 0
            count += 1
    return maxcount

if __name__ == '__main__':
    strArray = ['0', '0', '1', '0', '0', '1', '0', '1']
    print(count_bits(strArray))
