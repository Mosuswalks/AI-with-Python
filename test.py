

tbl = [[15,29,6,2],
        [16,9,8,0],
        [7,27,16,0]]

def avgby(tbl,col,by):
    averages = {}
    counts = {}
    if range(len(tbl)) == 0:
        return {0.0}
    for x in range(len(tbl)):
        if tbl[x][by] in averages.keys():
            averages[tbl[x][by]] += tbl[x][col]
            counts[tbl[x][by]] += 1
        if tbl[x][by] not in averages.keys():
            averages[tbl[x][by]] = tbl[x][col]
            counts[tbl[x][by]] = 1
    for x in averages:
        averages[x] = averages[x]/counts[x]
    return averages



print(avgby(tbl,0,3))