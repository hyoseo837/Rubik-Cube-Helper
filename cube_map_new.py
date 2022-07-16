from cube_class import cube
import math , os, linecache

n = 0;
moves = ["U","u","D","d","L","l","R","r","F","f","B","b"]
kkk = cube()
f = open("cmap_new.txt","w")
s = kkk.save()+"o\n"
f.write(s)
f.close()


def addcube(ccube,move,ans):
    ccc = cube(ccube.save())
    ccc.prt()
    ccc.move(moves[move])
    ccc.prt()
    print("=================================")
    c = open("cmap_new.txt","r")
    while True:
        data = c.readline()
        if data[:54] == ccc.save():
            c.close()
            return;
        if data == "":
            c.close()
            f = open("cmap_new.txt","a")
            s = ccc.save()+moves[ans] + "\n"
            f.write(s)
            f.close()
            return;


for foo in range(3):
    size = int(os.path.getsize("cmap_new.txt")/57)
    for i in range(n,size):
        dat = linecache.getline("cmap_new.txt", i+1)
        kkk = cube(dat[0:54])
        for j in range(12):
            addcube(kkk,j, j+int(math.pow(-1, j)))
    n = size;


