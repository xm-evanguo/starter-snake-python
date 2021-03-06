import collections
import random

def next_move_state(map, head_xy, direction):
    switcher = {
        'left': (-1, 0),
        'right': (1, 0),
        'up': (0, -1),
        'down': (0, 1)
    }
    return map[head_xy[1] + switcher.get(direction)[1]][head_xy[0] + switcher.get(direction)[0]]

def next_direction(map, head_xy, move_xy):
    switcher = {
        (-1, 0): 'left',
        (1, 0): 'right',
        (0, -1): 'up',
        (0, 1): 'down'
    }
    return switcher.get(((move_xy[0] - head_xy[0]), (move_xy[1] - head_xy[1])))

def shortest_path(map, starting, goal):
    queue = collections.deque([[(starting[0], starting[1])]])
    seen = set([starting])
    tmp_map = map
    if tmp_map[goal[1]][goal[0]] != 7:
        tmp_map[goal[1]][goal[0]] = 1
    while queue:
        path = queue.popleft()
        x, y = path[-1]
        if (x,y) == goal:
            return path;
        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
            if 0 <= x2 < len(map) and 0 <= y2 < len(map) and map[y2][x2] < 2 and (x2,y2) not in seen:
                queue.append(path + [(x2,y2)])
                seen.add((x2,y2))

def random_move(map, head_xy):
    directions = ['left', 'right', 'up', 'down']
    if head_xy[0] is 0:
        directions.remove('left')
    elif head_xy[0] is len(map) - 1:
        directions.remove('right')

    if head_xy[1] is 0:
        directions.remove('up')
    elif head_xy[1] is len(map) - 1:
        directions.remove('down')

    for direction in directions:
        if next_move_state(map, head_xy, direction) > 1 and len(directions) > 1:
            directions.remove(direction)

    return random.choice(directions)
