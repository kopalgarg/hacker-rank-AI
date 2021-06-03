'''
Bot saves princess - 2
'''
#!/usr/bin/python

def nextMove(n,r,c,grid):
    # given n by n grid
    xm = r
    ym = c
    # find coordinates for 'p'
    for i in range(0, n):
        for j in range(0, n):
            if (grid[i][j] == 'p'): xp = i; yp = j
    # distance between 'm' and 'p'
    x = xp - xm
    y = yp - ym
    # move till same row
    if (xm!=xp):
        return "UP" if (xm > xp) else "DOWN"
    # move till same col
    elif (ym!=yp):
        return "LEFT" if (ym > yp) else "RIGHT"
    return

n = int(input())
r,c = [int(i) for i in input().strip().split()]
grid = []
for i in range(0, n):
    grid.append(input())

print(nextMove(n,r,c,grid))
