from rubik.cube import Cube
from rubik import solve
from rubik import optimize
import time

from cube_class import MOVES, Cube as cb
from map_solver import binarySearch

def mysolve(string):
    result = []
    tmpCube = cb(string)
    while True:
        tmp = binarySearch(tmpCube.save())
        if tmp in MOVES:
            result.append(tmp)
            tmpCube.move(tmp)
        elif tmp == "C":
            return result
        elif not tmp:
            break
    

    newtxt = string[0:12] +string[18:21] +string[27:30] +string[36:39] +string[12:15] + string[21:24] \
        +string[30:33] +string[39:42] +string[15:18] +string[24:27] +string[33:36] +string[42:54]
    
    c = Cube(newtxt)
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
    start_time = time.perf_counter()

    print(" ".join(mysolve("302200325030112041201123032411533355544444314205552154")))
    end_time = time.perf_counter()
    execution_time = end_time - start_time
    print(f"The execution time is: {execution_time}")