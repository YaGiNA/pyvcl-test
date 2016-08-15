def getfname(str):
    strlist = str.split("\t")
    fname = strlist[-1]
    print(fname)  #末尾の値がファイル値を示すため
    return fname
