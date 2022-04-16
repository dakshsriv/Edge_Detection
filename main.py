from pprint import pprint
sample = [[10,20,200,200], 
          [20,30,145,100], 
          [30,40,255,230],
          [10,20,100,100]]

def calcDeriv(table):
    pprint(table)
    Deriv_N = 5*(table[0][0] + table[0][1] + table[0][2]) - 3*(table[1][0] + table[1][2] + table[2][0] + table[2][1] + table[2][2])
    Deriv_NE = 5*(table[0][1] + table[0][2] + table[1][2]) - 3*(table[0][0] + table[1][0] + table[2][0] + table[2][1] + table[2][2])
    Deriv_E = 5*(table[0][2] + table[1][2] + table[2][2]) - 3*(table[0][1] + table[0][0] + table[1][0] + table[2][0] + table[2][1])
    Deriv_SE = 5*(table[1][2] + table[2][1] + table[2][2]) - 3*(table[0][0] + table[0][1] + table[0][2] + table[1][0] + table[2][0])
    Deriv_S = 5*(table[2][0] + table[2][1] + table[2][2]) - 3*(table[0][0] + table[0][1] + table[0][2] + table[1][0] + table[1][2])
    Deriv_SW = 5*(table[1][0] + table[2][0] + table[2][1]) - 3*(table[0][0] + table[0][1] + table[0][2] + table[1][2] + table[2][2])
    Deriv_W = 5*(table[0][0] + table[1][0] + table[2][0]) - 3*(table[0][1] + table[0][2] + table[1][2] + table[2][1] + table[2][2])
    Deriv_NW = 5*(table[0][0] + table[0][1] + table[1][0]) - 3*(table[0][2] + table[1][2] + table[2][0] + table[2][1] + table[2][2])
    derivDict = {'W':Deriv_W, 'NW':Deriv_NW, 'N':Deriv_N, 'NE':Deriv_NE, 'E':Deriv_E, 'SE':Deriv_SE, 'S':Deriv_S, 'SW':Deriv_SW}
    max_number = 0
    direction = ""
    for (k,v) in derivDict.items():
        if v > max_number:
            max_number = v
            direction = k
    if max_number <= 800:
        direction = "no edge"
    return derivDict, direction


if __name__ == "__main__":
    sendTable = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(1, len(sample)-1):
        for j in range (1, len(sample)-1):
            for m in range(0, 3):
                for n in range(0, 3):
                    print(i, j, m, n)
                    sendTable[m][n] = sample[i+m-1][j+n-1]
            print(calcDeriv(sendTable))
            sendTable=[[0,0,0],[0,0,0],[0,0,0]]