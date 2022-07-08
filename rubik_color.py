class cube:

    colors = [];
    def __init__(self,string):
        for i in range(54):
            self.colors.append(string[i])

    def prt(self):
        print(f'''
        {self.colors[0]} {self.colors[1]} {self.colors[2]}
        {self.colors[3]} {self.colors[4]} {self.colors[5]}
        {self.colors[6]} {self.colors[7]} {self.colors[8]}
        
{self.colors[9]} {self.colors[10]} {self.colors[11]}   {self.colors[18]} {self.colors[19]} {self.colors[20]}   {self.colors[27]} {self.colors[28]} {self.colors[29]}   {self.colors[36]} {self.colors[37]} {self.colors[38]}
{self.colors[12]} {self.colors[13]} {self.colors[14]}   {self.colors[21]} {self.colors[22]} {self.colors[23]}   {self.colors[30]} {self.colors[31]} {self.colors[32]}   {self.colors[39]} {self.colors[40]} {self.colors[41]}
{self.colors[15]} {self.colors[16]} {self.colors[17]}   {self.colors[24]} {self.colors[25]} {self.colors[26]}   {self.colors[33]} {self.colors[34]} {self.colors[35]}   {self.colors[42]} {self.colors[43]} {self.colors[44]}

        {self.colors[45]} {self.colors[46]} {self.colors[47]}
        {self.colors[48]} {self.colors[49]} {self.colors[50]}
        {self.colors[51]} {self.colors[52]} {self.colors[53]}
        ''')
    
    def move(self, code):
        if code == 'U':
            tmp = self.colors[0]
            self.colors[0] = self.colors[6]
            self.colors[6] = self.colors[8]
            self.colors[8] = self.colors[2]
            self.colors[2] = tmp

            tmp = self.colors[1]
            self.colors[1] = self.colors[3]
            self.colors[3] = self.colors[7]
            self.colors[7] = self.colors[5]
            self.colors[5] = tmp

            tmp = (self.colors[9],self.colors[10],self.colors[11])
            (self.colors[9],self.colors[10],self.colors[11]) = (self.colors[18],self.colors[19],self.colors[20])
            (self.colors[18],self.colors[19],self.colors[20]) = (self.colors[27],self.colors[28],self.colors[29])
            (self.colors[27],self.colors[28],self.colors[29]) = (self.colors[36],self.colors[37],self.colors[38])
            (self.colors[36],self.colors[37],self.colors[38]) = tmp
            
        if code == 'u':
            tmp = self.colors[0]
            self.colors[0] = self.colors[2]
            self.colors[2] = self.colors[8]
            self.colors[8] = self.colors[6]
            self.colors[6] = tmp

            tmp = self.colors[1]
            self.colors[1] = self.colors[5]
            self.colors[5] = self.colors[7]
            self.colors[7] = self.colors[3]
            self.colors[3] = tmp

            tmp = (self.colors[9],self.colors[10],self.colors[11])
            (self.colors[9],self.colors[10],self.colors[11]) = (self.colors[36],self.colors[37],self.colors[38])
            (self.colors[36],self.colors[37],self.colors[38]) = (self.colors[27],self.colors[28],self.colors[29])
            (self.colors[27],self.colors[28],self.colors[29]) = (self.colors[18],self.colors[19],self.colors[20])
            (self.colors[18],self.colors[19],self.colors[20]) = tmp

foo = cube("111222111212212212333333333444444444555555555666666666")
foo.prt()
print("====================================")
foo.move("u")
foo.prt()