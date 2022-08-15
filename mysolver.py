from rubik.cube import Cube
from rubik import solve
from rubik import optimize

from cube_class import cube as cb

def mysolve(string):
    newtxt = string[0:12] +string[18:21] +string[27:30] +string[36:39] +string[12:15] + string[21:24] \
        +string[30:33] +string[39:42] +string[15:18] +string[24:27] +string[33:36] +string[42:54]

    c = Cube(newtxt)
    solution = solve.Solver(c)
    solution.solve()

    opt = optimize.optimize_moves(solution.moves)
    # print(" ".join(opt))

    result = []
    for i in range(len(opt)):
        if i[-1] == "i":
            opt[i] = opt[i][0].lower()

    for i in opt:
        if i == "M":
            result.append("R")
            result.append("l")
            result.append("x")
            continue
        if i == "m":
            result.append("r")
            result.append("L")
            result.append("X")
            continue
        if i == "E":
            result.append("U")
            result.append("d")
            result.append("y")
            continue
        if i == "e":
            result.append("u")
            result.append("D")
            result.append("Y")
            continue
        if i == "S":
            result.append("f")
            result.append("B")
            result.append("Z")
            continue
        if i == "s":
            result.append("F")
            result.append("b")
            result.append("z")
            continue
        result.append(i)


if __name__ == "__main__":
    kkkk = cb("302200325030112041201123032411533355544444314205552154")