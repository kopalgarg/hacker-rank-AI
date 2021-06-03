#!/usr/bin/python
'''
cleaning bot
'''
def next_move(posr, posc, board):
    x, y = 0,0
    for i,row in enumerate(board):
        for j, val in enumerate(row):
            if val == 'd':
                # manhattan distance
                dist = abs(posr-i)+abs(posc-j)
                if dist < len(board)^2:
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
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
