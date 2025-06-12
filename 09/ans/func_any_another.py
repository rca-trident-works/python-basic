def out_csvdata(**kwargs):
    '''
    辞書型のデータをcsvで出力する
    Breakfast,Lunch,Dinnerの順に出力する
    '''
    out_list = ['-', '-', '-']
    for k, v in kwargs.items():
        if k == 'B':
            out_list[0] = v
        elif k == 'L':
            out_list[1] = v
        elif k == 'D':
            out_list[2] = v

    print(out_list)             # リストでの出力
    print(",".join(out_list))   # カンマ区切りでの出力


# main
eat = {}
while True:
    menu = input("朝食(B) 昼食(L) 夕食(D)と食べたものを入力してください：")
    if menu == '':
        break
    token, menu = menu.split(',')
    if token in ['B', 'L', 'D']:
        eat[token] = menu
    else:
        print('記号が間違っています。登録しません')
        continue


out_csvdata(**eat)
