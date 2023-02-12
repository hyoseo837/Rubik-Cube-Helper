f = open("cmap_new.txt", "r")
datas = f.readlines()

def find(target, max_limit, min_limit):
    while True:
        if datas[min_limit+max_limit//2] == target:
            return datas[min_limit+max_limit//2][-2]
        elif datas[min_limit+max_limit//2] < target:
            find(target,max_limit, min_limit+max_limit//2)
        else:
            find(target,min_limit+max_limit//2, min_limit)

length = len(datas)
m = 0
M = len(datas)

print(find(input(), M, m))