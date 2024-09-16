import time


def partition(data, head, tail, drawData, timeTick):
    border = head
    pivot = data[tail]

    drawData(data, colorArray(len(data), head, tail, border, border))
    time.sleep(timeTick)
    for j in range(head,tail):
        if(data[j] < pivot):
            drawData(data, colorArray(len(data), head, tail, border, j, True))
            time.sleep(timeTick)
            data[border], data[j] = data[j], data[border]
            border+=1
        drawData(data, colorArray(len(data), head, tail, border, j))
        time.sleep(timeTick)

    drawData(data, colorArray(len(data), head, tail, border, tail, True))
    time.sleep(timeTick)

    data[border], data[tail] = data[tail], data[border]
    return border

def quick_sort(data, head, tail, drawData, timeTick):
    if head < tail:
        partitionIdx = partition(data,head, tail, drawData, timeTick)


        #LEFT Partition
        quick_sort(data, head, partitionIdx-1, drawData, timeTick)

        #RIGHT Partition
        quick_sort(data, partitionIdx+1, tail, drawData, timeTick)


def colorArray(datalen, head, tail, border, currIdx, isSwapping = False):
    colorArray = []
    for i in range(datalen):
        if i>=head and i<=tail:
            colorArray.append("grey")
        else:
            colorArray.append("white")

        if i == tail:
            colorArray[i] == 'orange'
        elif i == border:
            colorArray[i] = 'red'
        elif i == currIdx:
            colorArray[i] = 'yellow'

        if isSwapping:
            if i==border or i == currIdx:
                colorArray[i] = '#A90042'

    return colorArray       