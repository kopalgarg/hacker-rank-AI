#!/usr/bin/python
'''
cleaning bot
'''
# Head ends here

'''
Input:
bd---
-d---
---d-
---d-
--d-d
'''

def next_move(posr, posc, board):
    d = len(board)^2  # traverse all tiles
    x, y = 0,0
    for i,row in enumerate(board):
        for j, val in enumerate(row): #    0 b   1 d   2 - ...
            if val == 'd':
                # check if all dirty tiles covered
                dist = abs(posr-i)+abs(posc-j)
                if dist < d:
                    x,y,d = i,j,dist
    if y > posc:
        print("RIGHT")
    elif y < posc:
        print("LEFT")
    elif x < posr:
        print("UP")
    elif x > posr:
        print("DOWN")
    else: print("CLEAN")
    return

# Tail starts here

if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
