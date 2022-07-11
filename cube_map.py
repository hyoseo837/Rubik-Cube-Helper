from cube_class import cube
import math

def iter(ccc, n, p,count):
    if n > 0:
        for m in range(12):
            localcount = count
            localCube = cube(ccc.save())
            if m == p:
                continue
            if p == m+int(math.pow(-1, m)):
                localcount += 1
            else:
                localcount = 1
            if localcount == 4:
                continue
            localCube.move(moves[m])
            iter(localCube, n-1, m+int(math.pow(-1, m)),localcount)
    else:
        s = ccc.save()+" "+ moves[p] + "\n"
        f.write(s)

moves = ["U","u","D","d","L","l","R","r","F","f","B","b"]

for great in range(6):
    f = open(f"cmap_{great}.txt","w")
    kkk = cube()
    iter(kkk, great, -2,0)

    f.close()
