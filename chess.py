board = [
    ["Br", "Bn", "Bb", "Bq", "Bk", "Bb", "Bn", "Br"],
    ["Bp", "Bp", "Bp", "Bp", "Bp", "Bp", "Bp", "Bp"],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    [" ", " ", " ", " ", " ", " ", " ", " "],
    ["Wp", "Wp", "Wp", "Wp", "Wp", "Wp", "Wp", "Wp"],
    ["Wr", "Wn", "Wb", "Wq", "Wk", "Wb", "Wn", "Wr"]
]

def flipcoords(x, y=None):
    convlist = ["a", "b", "c", "d", "e", "f", "g", "h"]
    if y is None:
        # d6
        if type(x) == str:
            f=8-int(x[1])
            r=convlist.index(x[0])
            return (f, r)
        else:
            raise TypeError
    else:
        if type(x) and type(y) == int:
            # 2, 3
            print(board[x][y])
            f=str(8-x)
            r=convlist[y]
            return f+r

def getboardpos(strpos):
    x, y = flipcoords(strpos)
    return board[x][y]

def lateral_betweens(pos1, pos2):
    pass

def isvalid(piecepos, newpos):

    piece_x, piece_y = flipcoords(piecepos)
    new_x, new_y = flipcoords(newpos)
    piece = getboardpos(piecepos)
    color = piece[0]
    piecetype = piece[1]

    if piecepos == newpos:
        return 0

    if piecetype == "p":
        if color == "B":
            if piece_x == 1:
                if new_x not in [2,3]:
                    return 0
            elif piece_x == 7:
                return 0
            else:
                if new_x is not piece_x+1:
                    return 0
        if color == "W":
            if piece_x == 6:
                if new_x not in [4,5]:
                    return 0
            elif piece_x == 0:
                return 0
            else:
                if new_x is not piece_x-1:
                    return 0
        if getboardpos(newpos) is not " ":
            if new_y == piece_y:
                return 0
            elif new_y not in [piece_y-1, piece_y+1]:
                return 0
        return 1

    if piecetype == "r":
        if new_x is not piece_x:
            if new_y is not piece_y:
                return 0
        else:
            if new_y == piece_y:
                return 0
        if new_x is not piece_x:
            l = sorted[new_y, piece_y]
            betweens = list(map(lambda x: (new_x, l[0]+x), list(range(l[1]))))[1:]
            for x, y in betweens:
                if board[x,y] is not " ":
                    return 0
        return 1





