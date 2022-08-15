from rubik.cube import Cube
from rubik import solve
from rubik import optimize

from cube_class import cube as cb
MOVES = ["U","u","D","d","L","l","R","r","F","f","B","b"]

def mysolve(string):
    newtxt = string[0:12] +string[18:21] +string[27:30] +string[36:39] +string[12:15] + string[21:24] \
        +string[30:33] +string[39:42] +string[15:18] +string[24:27] +string[33:36] +string[42:54]

    c = Cube(newtxt)
    if c.is_solved():
        return []
    for i in MOVES:
        tmpc = cb(string)
        tmpc.move(i)
        if Cube(tmpc.save()[0:12] +tmpc.save()[18:21] +tmpc.save()[27:30] +tmpc.save()[36:39] +tmpc.save()[12:15] + tmpc.save()[21:24] \
        +tmpc.save()[30:33] +tmpc.save()[39:42] +tmpc.save()[15:18] +tmpc.save()[24:27] +tmpc.save()[33:36] +tmpc.save()[42:54]).is_solved():
            return list(i)
    
    for i in MOVES:
        for j in MOVES:
            tmpc = cb(string)
            tmpc.move(i)
            tmpc.move(j)
            if Cube(tmpc.save()[0:12] +tmpc.save()[18:21] +tmpc.save()[27:30] +tmpc.save()[36:39] +tmpc.save()[12:15] + tmpc.save()[21:24] \
            +tmpc.save()[30:33] +tmpc.save()[39:42] +tmpc.save()[15:18] +tmpc.save()[24:27] +tmpc.save()[33:36] +tmpc.save()[42:54]).is_solved():
                return [i,j]
                
    for i in MOVES:
        for j in MOVES:
            for k in MOVES:
                tmpc = cb(string)
                tmpc.move(i)
                tmpc.move(j)
                tmpc.move(k)
                if Cube(tmpc.save()[0:12] +tmpc.save()[18:21] +tmpc.save()[27:30] +tmpc.save()[36:39] +tmpc.save()[12:15] + tmpc.save()[21:24] \
                +tmpc.save()[30:33] +tmpc.save()[39:42] +tmpc.save()[15:18] +tmpc.save()[24:27] +tmpc.save()[33:36] +tmpc.save()[42:54]).is_solved():
                    return [i,j,k]
                
    for i in MOVES:
        for j in MOVES:
            for k in MOVES:
                for l in MOVES:
                    tmpc = cb(string)
                    tmpc.move(i)
                    tmpc.move(j)
                    tmpc.move(k)
                    tmpc.move(l)
                    if Cube(tmpc.save()[0:12] +tmpc.save()[18:21] +tmpc.save()[27:30] +tmpc.save()[36:39] +tmpc.save()[12:15] + tmpc.save()[21:24] \
                    +tmpc.save()[30:33] +tmpc.save()[39:42] +tmpc.save()[15:18] +tmpc.save()[24:27] +tmpc.save()[33:36] +tmpc.save()[42:54]).is_solved():
                        return [i,j,k,l]
                 

    solution = solve.Solver(c)
    solution.solve()


    opt = optimize.optimize_moves(solution.moves)
    # print(" ".join(opt))

    result = []
    for i in opt:
        if i == "M":
            result.append("R")
            result.append("Li")
            result.append("Xi")
            continue
        if i == "Mi":
            result.append("Ri")
            result.append("L")
            result.append("X")
            continue
        if i == "E":
            result.append("U")
            result.append("Di")
            result.append("Yi")
            continue
        if i == "Ei":
            result.append("Ui")
            result.append("D")
            result.append("Y")
            continue
        if i == "S":
            result.append("Fi")
            result.append("B")
            result.append("Z")
            continue
        if i == "Si":
            result.append("F")
            result.append("Bi")
            result.append("Zi")
            continue
        result.append(i)
    result = optimize.optimize_moves(result)
    for i in range(len(result)):
        if result[i][-1] == "i":
            result[i] = result[i][0].lower()

    return result


if __name__ == "__main__":
    kkkk = cb("302200325030112041201123032411533355544444314205552154")
    print(" ".join(mysolve("302200325030112041201123032411533355544444314205552154")))