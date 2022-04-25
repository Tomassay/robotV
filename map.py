import random


def make_map(rows, cols, obstacles):
    arr = []
    for i in range(rows * cols):
        if i < obstacles:
            arr.append(1)
        else:
            arr.append(0)

    random.shuffle(arr)

    start_position = {'x': 0, 'y': 0}
    random_position = random.randint(0, rows*cols - obstacles -1)

    #map = [[0 for x in range(rows)] for x in range(cols)]
    map = []
    #print(map)
    counter = 0

    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(arr[i*cols+j])
            #if arr[j] == 0:
            #    if counter == random_position:
            #        start_position = {'x': j, 'y':i}
            counter += 1
        map.append(row)
        print('itt', map, 'row', row)
    return map
#, start_position
