def pers(line, num):
    strlist = line.split("\t")  #まずはタブで分割
    strlist.insert(0, num+1)    #先頭にIdを追加
    print(strlist)
    header = ["Id", "CHROM", "POS", "ID", "REF",
              "ALT", "QUAL", "FILTER"]
    sa


    for (header, strlist) in zip(header, strlist):
        print(str(header) + ":" + str(strlist))


def paticular pers
