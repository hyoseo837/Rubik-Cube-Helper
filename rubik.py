class cube:

    vertex = []
    edge = []
    def __init__(self,string_vertex, string_edge):
        for i in range(8):
            self.vertex.append(string_vertex[i])
        for i in range(12):
            self.edge.append(string_edge[i])
    
    def prt(self):
        for i in self.vertex:
            print(i)

    def move(self,code):
        if code == "U":
            tmp = self.vertex[0]
            self.vertex[0] = self.vertex[3]
            self.vertex[3] = self.vertex[2]
            self.vertex[2] = self.vertex[1]
            self.vertex[1] = tmp
        if code == "u":
            tmp = self.vertex[0]
            self.vertex[0] = self.vertex[1]
            self.vertex[1] = self.vertex[2]
            self.vertex[2] = self.vertex[3]
            self.vertex[3] = tmp

        if code == "D":
            tmp = self.vertex[4]
            self.vertex[4] = self.vertex[5]
            self.vertex[5] = self.vertex[6]
            self.vertex[6] = self.vertex[7]
            self.vertex[7] = tmp
        if code == "d":
            tmp = self.vertex[4]
            self.vertex[4] = self.vertex[7]
            self.vertex[7] = self.vertex[6]
            self.vertex[6] = self.vertex[5]
            self.vertex[5] = tmp

        if code == "R":
            tmp = self.vertex[1]
            self.vertex[1] = self.vertex[2]
            self.vertex[2] = self.vertex[6]
            self.vertex[6] = self.vertex[5]
            self.vertex[5] = tmp
        if code == "r":
            tmp = self.vertex[1]
            self.vertex[1] = self.vertex[5]
            self.vertex[5] = self.vertex[6]
            self.vertex[6] = self.vertex[2]
            self.vertex[2] = tmp
            
        if code == "L":
            tmp = self.vertex[0]
            self.vertex[0] = self.vertex[4]
            self.vertex[4] = self.vertex[7]
            self.vertex[7] = self.vertex[3]
            self.vertex[3] = tmp
        if code == "l":
            tmp = self.vertex[0]
            self.vertex[0] = self.vertex[3]
            self.vertex[3] = self.vertex[7]
            self.vertex[7] = self.vertex[4]
            self.vertex[4] = tmp

        if code == "F":
            tmp = self.vertex[7]
            self.vertex[7] = self.vertex[6]
            self.vertex[6] = self.vertex[2]
            self.vertex[2] = self.vertex[3]
            self.vertex[3] = tmp
        if code == "f":
            tmp = self.vertex[7]
            self.vertex[7] = self.vertex[3]
            self.vertex[3] = self.vertex[2]
            self.vertex[2] = self.vertex[6]
            self.vertex[6] = tmp
            
        if code == "B":
            tmp = self.vertex[0]
            self.vertex[0] = self.vertex[1]
            self.vertex[1] = self.vertex[5]
            self.vertex[5] = self.vertex[4]
            self.vertex[4] = tmp
        if code == "b":
            tmp = self.vertex[0]
            self.vertex[0] = self.vertex[4]
            self.vertex[4] = self.vertex[5]
            self.vertex[5] = self.vertex[1]
            self.vertex[1] = tmp

foo = cube("12345678","abcdefghijkl")
foo.prt()
print("========================")
foo.move('D')
foo.prt()