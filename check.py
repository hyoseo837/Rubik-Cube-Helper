def check(string):
    mids = [string[4],string[13],string[22],string[31],string[40],string[49]]
    edges = [string[1],string[3],string[5],string[7],string[10],string[12],
             string[14],string[16],string[19],string[21],string[23],string[25],
             string[28],string[30],string[32],string[34],string[37],string[39],
             string[41],string[43],string[46],string[48],string[50],string[52]]
    vertexes = [string[0],string[2],string[6],string[8],string[9],string[11],
                string[15],string[17],string[18],string[20],string[24],string[26],
                string[27],string[29],string[33],string[35],string[36],string[38],
                string[42],string[44],string[45],string[47],string[51],string[53]]
    for i in mids:
        if mids.count(i) != 1:
            return False
        if edges.count(i) != 4:
            return False
        if vertexes.count(i) != 4:
            return False
    return True