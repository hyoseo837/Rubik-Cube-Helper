from cube_class import cube

targetCube = cube("414414431113323113623433663466646246555551555221265222")
nowCube = cube("414414431113323113623433663466646246555551555221265222")
targetCube.prt()
ans = []

f = open("cmap_5.txt","r")
while True:
    data = f.readline()
    if data[0:54] == nowCube.save():
        ans.append(data[-2])
        nowCube.move(data[-2])
        break
    if data == "":
        break
f.close()

f = open("cmap_4.txt","r")
while True:
    data = f.readline()
    if data[0:54] == nowCube.save():
        ans.append(data[-2])
        nowCube.move(data[-2])
        break
    if data == "":
        break
f.close()

f = open("cmap_3.txt","r")
while True:
    data = f.readline()
    if data[0:54] == nowCube.save():
        ans.append(data[-2])
        nowCube.move(data[-2])
        break
    if data == "":
        break
f.close()

nowCube.prt()

f = open("cmap_2.txt","r")
while True:
    data = f.readline()
    if data[0:54] == nowCube.save():
        ans.append(data[-2])
        nowCube.move(data[-2])
        break
    if data == "":
        break
f.close()

f = open("cmap_1.txt","r")
while True:
    data = f.readline()
    if data[0:54] == nowCube.save():
        ans.append(data[-2])
        nowCube.move(data[-2])
        break
    if data == "":
        break
f.close()

for i in ans:
    print(i)