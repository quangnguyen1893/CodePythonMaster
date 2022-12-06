def findMedian(array):
    md = 0
    l = len(array)
    array.sort()
    if l % 2 == 0:
        md = (int(array[l // 2]) + int(array[(l // 2 - 1)])) / 2
        return md
    else:
        md = int(array[l // 2])
        return md
if __name__ == '__main__':
    n = int(input())
    l = []
    des = []
    for x in range(n):
        for y in range(1):
            type = input().split()
            if len(des) == 0 and type[0] == 'r':
                print('Wrong!')
                continue
            elif len(des) == 1 and type[0] == 'r':
                print('Wrong!')
                continue
            else:
                if type[0] == 'r':
                    des.pop(y)
                    print(findMedian(des))
                else:
                    des.append(int(type[1]))
                    print(findMedian(des))

