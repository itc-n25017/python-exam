phrase = 'PythonProgramming'
list_p = []  #空のリストを作成
for p in phrase: #phraseの一文字ずつを繰り返しでチェック
    if p not in list_p: #チェック文字化list_pにない場合
        list_p.append(p) #pをlist_pに追加(:append)する
print(len(phrase) - len(list_p))