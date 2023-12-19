maze = []
with open('10/input.txt') as f:
    for line in f:
        maze.append(line[:-1])

for i, row in enumerate(maze):
    if 'S' in row:
        start = (row.index('S'), i)

for start_dir in 'RULD':
    dir = start_dir
    x, y = start
    flag = True
    solved = False
    nodes = {start: 0}
    path = [start]
    n = 0
    while flag:
        n += 1
        if dir == 'R':
            if x + 1 < len(maze[y]):
                x += 1
            else:
                flag = False
        elif dir == 'U':
            if y > 0:
                y -= 1
            else:
                flag = False
        elif dir == 'L':
            if x > 0:
                x -= 1
            else:
                flag = False
        elif dir == 'D':
            if y + 1 < len(maze):
                y += 1
            else:
                flag = False

        if not flag:
            break

        nodes[(x, y)] = n
        path.append((x, y))

        if maze[y][x] == 'L':
            if dir == 'L':
                dir = 'U'
            elif dir == 'D':
                dir = 'R'
        elif maze[y][x] == 'J':
            if dir == 'R':
                dir = 'U'
            elif dir == 'D':
                dir = 'L'
        elif maze[y][x] == '7':
            if dir == 'R':
                dir = 'D'
            elif dir == 'U':
                dir = 'L'
        elif maze[y][x] == 'F':
            if dir == 'L':
                dir = 'D'
            elif dir == 'U':
                dir = 'R'
        elif maze[y][x] == '.':
            flag = False
        elif maze[y][x] == 'S':
            flag = False
            solved = True

    if solved:
        break

print(nodes[start]>>1)
path = path[:-1]

sum = 0
for i in range(len(path)):
    n_1 = path[i]
    n_2 = path[(i+1)%len(path)]
    x_1, y_1 = n_1
    x_2, y_2 = n_2
    sum += x_1 * y_2 - y_1 * x_2

area = abs(sum/2)

print(area-len(path)/2+1)