max_size = 0

def get_max_rectangle(field):
    for i in range(len(field)):
        for j in range(len(field[0])):
            if field[i][j] == 1:
                max_rectangle(field, {'x0':j, 'y0':i, 'x1':j, 'y1':i})
    

def check_expandable(field, rect, a0, a1, b, c):
    return rect[a1] - rect[a0] + 1 == len([i for i in range(rect[a0], rect[a1]+1) if field[rect[b]+c][i] == 1])

def check_fill_ones(field, rect):
    for i in range(rect['x0'], rect['x1']+1):
        for j in range(rect['y0'], rect['y1']+1):
            if field[j][i] == 0:
                return False
    return True

def max_rectangle(field, rect):
    #右拡張
    if check_expandable(field, rect, 'y0', 'y1', 'x1', 1):
        tmp_rect = rect
        tmp_rect['x1'] += 1
        max_rectangle(field, tmp_rect)

    #上拡張
    if check_expandable(field, rect, 'x0', 'x1', 'y0', -1):
        tmp_rect = rect
        tmp_rect['y0'] += -1
        max_rectangle(field, tmp_rect)

    #左拡張
    if check_expandable(field, rect, 'y0', 'y1', 'x0', -1):
        tmp_rect = rect
        tmp_rect['x0'] += -1
        max_rectangle(field, tmp_rect)

    #下拡張
    if check_expandable(field, rect, 'x0', 'x1', 'y1', 1):
        tmp_rect = rect
        tmp_rect['y1'] += 1
        max_rectangle(field, tmp_rect)

    global max_size
    if check_fill_ones(field, rect):
        max_size = max(max_size, (rect['x1']-rect['x0']+1) * (rect['y1']-rect['y0']+1))


#def input_field():

#field = input_field()
field = [[0, 0, 0, 0, 0], [0, 1, 1, 0, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]]
get_max_rectangle(field)
print(max_size)
