def pers(line, num, fname):
    strlist = line.split("\t")  #まずはタブで分割
    strlist.insert(0, num+1)    #先頭にIdを追加
    print(strlist)
    header = ["Id", "CHROM", "POS", "ID", "REF",
              "ALT", "QUAL", "FILTER"]
    #


    for (header, strlist) in zip(header, strlist):
        print(str(header) + ":" + str(strlist))
