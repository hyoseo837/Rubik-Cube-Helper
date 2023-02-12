from cube_class import cube
import math , os, linecache

n = 0;
moves = ["U","u","D","d","L","l","R","r","F","f","B","b"]
# kkk = cube()
# f = open("cmap_new.txt","w")
# s = kkk.save()+"o\n"
# f.write(s)
# f.close()


def addcube(ccube,move,ans):
    ccc = cube(ccube.save())
    ccc.move(moves[move])
    c = open("cmap_new.txt","r")
    datas = c.readlines()
    used = False;
    while True:
        f = open("cmap_new.txt","w")
        for i in datas:
            s = ccc.save()+" "+moves[ans] + "\n"
            if i < s:
                f.write(i)
            elif i[:54]== s[:54]:
                f.write(i)
                used = True
            else:
                if not used:
                    f.write(s)
                    f.write(i)
                    used = True
                else:
                    f.write(i)

        if not used:
            f.write(s)
        f.close()
        break;
    c.close()
    return;


size = int(os.path.getsize("cmap_new.txt")/58)
print(size)
for i in range(n,size):
    dat = linecache.getline("cmap_new.txt", i+1)
    if dat == "":
        continue
    kkk = cube(dat[0:54])
    for j in range(12):
        addcube(kkk,j, j+int(math.pow(-1, j)))


