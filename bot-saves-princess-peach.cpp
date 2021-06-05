'''
Bot saves princess
'''
#!/usr/bin/python

def displayPathtoPrincess(n,grid):
    # given: n by n grid
    # find coordinates for 'm' and 'p'
    for i in range(0, n):
        for j in range(0, n):
            if (grid[i][j] == 'm'): xm = i; ym = j
            if (grid[i][j] == 'p'): xp = i; yp = j
    # distance between 'm' and 'p'
    x = xp-xm
    y = yp-ym
    while (x != 0) and (y!=0):
        if (x > 0):
            print("RIGHT")
            if (y > 0):
                print("DOWN")
                # update y
                y = abs(y)-1
            elif (y>0):
                print("UP")
                y+=1
            x-=1
        else:
            print("LEFT")
            if (y > 0):
                print("DOWN")
                y = abs(y)-1
            elif (y>0):
                print("UP")
                y+=1
            x+=1
    return


m = int(input())
grid = []
for i in range(0, m):
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
