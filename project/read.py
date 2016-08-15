import re
import perspective as prs
import getfilename as gfn

f = open("KA004.sift.vcf", "r")
line = f.readline() #ファイルの規模が未知数なので、1行ずつ処理する
cnt = 0

while 1:
    d_match = re.search("\A##", line) #冒頭の注釈部分を省く
    n_match = re.search("\A#", line)

    if n_match:
        fname = gfn.getfname(line.strip())
    elif d_match is None:   #注釈じゃない時にプログラムを実行する
        prs.pers(line.strip(), cnt, fname)
        #パースメソッドへ。改行文字はここで削除
        cnt += 1

    line = f.readline()
    if (cnt > 0): break #テストなので1行に制限(完成したらコメントアウト、for文にする)

f.close()
