from time import sleep

class NumberTooBig(Exception):
    pass


def displayNumber(board, number, a, b, c, d, e, f, g):
    
    if number > 9:
        raise NumberTooBig

    elif number == 0:
        board.digital[a].write(1)
        board.digital[b].write(1)
        board.digital[c].write(1)
        board.digital[d].write(1)
        board.digital[e].write(1)
        board.digital[f].write(1)
        board.digital[g].write(0)
    elif number == 1:
        board.digital[a].write(0)
        board.digital[b].write(1)
        board.digital[c].write(1)
        board.digital[d].write(0)
        board.digital[e].write(0)
        board.digital[f].write(0)
        board.digital[g].write(0)
    elif number == 2:
        board.digital[a].write(1)
        board.digital[b].write(1)
        board.digital[c].write(0)
        board.digital[d].write(1)
        board.digital[e].write(1)
        board.digital[f].write(0)
        board.digital[g].write(1)
    elif number == 3:
        board.digital[a].write(1)
        board.digital[b].write(1)
        board.digital[c].write(1)
        board.digital[d].write(1)
        board.digital[e].write(0)
        board.digital[f].write(0)
        board.digital[g].write(1)
    elif number == 4:
        board.digital[a].write(0)
        board.digital[b].write(1)
        board.digital[c].write(1)
        board.digital[d].write(0)
        board.digital[e].write(0)
        board.digital[f].write(1)
        board.digital[g].write(1)
    elif number == 5:
        board.digital[a].write(1)
        board.digital[b].write(0)
        board.digital[c].write(1)
        board.digital[d].write(1)
        board.digital[e].write(0)
        board.digital[f].write(1)
        board.digital[g].write(1)
    elif number == 6:
        board.digital[a].write(1)
        board.digital[b].write(0)
        board.digital[c].write(1)
        board.digital[d].write(1)
        board.digital[e].write(1)
        board.digital[f].write(1)
        board.digital[g].write(1)
    elif number == 7:
        board.digital[a].write(1)
        board.digital[b].write(1)
        board.digital[c].write(1)
        board.digital[d].write(0)
        board.digital[e].write(0)
        board.digital[f].write(0)
        board.digital[g].write(0)
    elif number == 8:
        board.digital[a].write(1)
        board.digital[b].write(1)
        board.digital[c].write(1)
        board.digital[d].write(1)
        board.digital[e].write(1)
        board.digital[f].write(1)
        board.digital[g].write(1)
    elif number == 9:
        board.digital[a].write(1)
        board.digital[b].write(1)
        board.digital[c].write(1)
        board.digital[d].write(1)
        board.digital[e].write(0)
        board.digital[f].write(1)
        board.digital[g].write(1)



def sevDisplay(board, number, a, b, c, d, e, f, g, first, second, third, fourth):
    if number > 9999:
        raise NumberTooBig
    ones = number % 10
    tens = number // 10 % 10
    hundreds = number // 100 % 10
    thousands = number // 1000
    lst = [ones,tens,hundreds,thousands]
    while True:
        for i in lst:
            dg = lst.index(i) + 1
            displayNumber(board, i, a, b, c, d, e, f, g)
            setDigit(board,dg,first,second,third,fourth)
            sleep(0.3)

def decimalp(board, dp, onOrOff=True):
    if onOrOff:
        board.digital[dp].write(1)
    else:
        board.digital[dp].write(0)


def setDigit(board, n, first, second, third, fourth):
    if n > 4:
        raise NumberTooBig
    lst = [fourth,third,second,first]

    for i in lst:
        if lst.index(i) + 1 == n:
            board.digital[i].write(0)
            continue
        board.digital[i].write(1)
