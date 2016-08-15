import re
import perspective

f = open("KA004.sift.vcf", "r")
line = f.readline() #ファイルの規模が未知数なので、1行ずつ処理する
cnt = 0

while 1:
    match = re.search( "\A#", line) #冒頭の注釈部分を省く
    if match is None:   #注釈じゃない時にプログラムを実行する
        print(line) #本来ならここでデータベースに入力するプログラムへ飛ぶ
        perspective.pers(line.strip(), cnt) #パースメソッドへ。改行文字はここで削除
        cnt += 1
    line = f.readline()
    if (cnt > 0): break #テストなので1行に制限(完成したらコメントアウト、for文にする)

f.close()
