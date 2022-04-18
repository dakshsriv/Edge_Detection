from pprint import pprint
example = [[0 ,0  ,0  ,0  ,230], 
          [0  ,0  ,0  ,210,0], 
          [0  ,0  ,255,220,223],
          [0  ,220,255  ,255  ,255],
          [250,255  ,255  ,255  ,255]]
x=          [[0, 0, 0, 0, 140, 0, 0]
          , [0, 0, 0, 70, 140, 0, 0], 
          [0, 0, 70, 70, 140, 70, 0], 
          [0, 0, 70, 210, 210, 70, 0], 
          [0, 0, 140, 255, 255, 70, 0], 
          [0, 0, 70, 70, 140, 0, 0], 
          [0, 0, 0, 0, 0, 0, 0]]
def calc_derivatives(table):
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

def make_edge_map(sample):
    output = []
    for x in range(0, len(sample)):
        preSend=[]
        for y in range(0, len(sample[x])):
            preSend.append("no edge")
        output.append(preSend)

    sendTable = [[0,0,0],[0,0,0],[0,0,0]]
    for i in range(1, len(sample)-1):
        for j in range (1, len(sample[0])-1):
            for m in range(0, 3):
                for n in range(0, 3):
                    sendTable[m][n] = sample[i+m-1][j+n-1]
            print(calc_derivatives(sendTable))
            output[i][j] = calc_derivatives(sendTable)[1]
            sendTable=[[0,0,0],[0,0,0],[0,0,0]]
    return output

if __name__ == "__main__":
    for d in range(0,len(example)):
        example[d].insert(0,0)
        example[d].append(0)
    example.insert(0,[0,0,0,0,0,0,0])
    example.append([0,0,0,0,0,0,0])
    edge_map = make_edge_map(example)
    print(edge_map)
    rendered = []
    for x in range(0, len(edge_map)):
        preSend=[]
        for y in range(0, len(edge_map[x])):
            preSend.append(0)
        rendered.append(preSend)
    for a in range(0, len(edge_map)):
        for b in range(0, len(edge_map[a])):
            if edge_map[a][b] == "E":
                rendered[a-1][b+1] += 70
                rendered[a][b+1] += 70
                rendered[a+1][b+1] += 70
            if edge_map[a][b] == "W":
                rendered[a-1][b-1] += 70
                rendered[a][b-1] += 70
                rendered[a+1][b-1] += 70
            if edge_map[a][b] == "N":
                rendered[a-1][b-1] += 70
                rendered[a-1][b] += 70
                rendered[a-1][b+1] += 70
            if edge_map[a][b] == "S":
                rendered[a+1][b-1] += 70
                rendered[a+1][b] += 70
                rendered[a+1][b+1] += 70
            if edge_map[a][b] == "NE":
                rendered[a-1][b+1] += 70
            if edge_map[a][b] == "NW":
                rendered[a-1][b-1] += 70
            if edge_map[a][b] == "SE":
                rendered[a+1][b+1] += 70
            if edge_map[a][b] == "SW":
                rendered[a+1][b-1] += 70
    for c in range(0, len(rendered)):
        for d in range(0, len(rendered[c])): 
            if rendered[c][d] > 255:
                rendered[c][d] = 255
    print(rendered)