from cube_class import Cube,MOVES,counterMove

def c_write(string):
    f = open("cmap.txt","a")
    f.write(string)
    f.close()

def make_string(element):
    return element[0] + " " + element[1]+"\n"

def make_dict():
    solution_map = {"000000000111111111222222222333333333444444444555555555":"C"}
    for i in MOVES:
        tmpCube = Cube()
        tmpCube.move(i)
        opposite_move = counterMove(i)
        string = tmpCube.save()
        if string in list(solution_map.keys()):
            continue
        solution_map[string]=opposite_move

    for j in MOVES:
        for i in MOVES:
            tmpCube = Cube()
            tmpCube.move(j)
            tmpCube.move(i)
            opposite_move = counterMove(i)
            string = tmpCube.save()
            if string in list(solution_map.keys()):
                continue
            solution_map[string]=opposite_move
            
    for k in MOVES:
        for j in MOVES:
            for i in MOVES:
                tmpCube = Cube()
                tmpCube.move(k)
                tmpCube.move(j)
                tmpCube.move(i)
                opposite_move = counterMove(i)
                string = tmpCube.save()
                if string in list(solution_map.keys()):
                    continue
                solution_map[string]=opposite_move
    for l in MOVES:
        for k in MOVES:
            for j in MOVES:
                for i in MOVES:
                    tmpCube = Cube()
                    tmpCube.move(l)
                    tmpCube.move(k)
                    tmpCube.move(j)
                    tmpCube.move(i)
                    opposite_move = counterMove(i)
                    string = tmpCube.save()
                    if string in list(solution_map.keys()):
                        continue
                    solution_map[string]=opposite_move
    for m in MOVES:
        for l in MOVES:
            for k in MOVES:
                for j in MOVES:
                    for i in MOVES:
                        tmpCube = Cube()
                        tmpCube.move(m)
                        tmpCube.move(l)
                        tmpCube.move(k)
                        tmpCube.move(j)
                        tmpCube.move(i)
                        opposite_move = counterMove(i)
                        string = tmpCube.save()
                        if string in list(solution_map.keys()):
                            continue
                        solution_map[string]=opposite_move

    return solution_map
        

        
for i in sorted(make_dict().items()):
    c_write(make_string(i))