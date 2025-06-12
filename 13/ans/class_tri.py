class TridentStudent:
    class_name = ''
    num = 0
    name = ''
    gender = ''


# main
p = TridentStudent()
p.class_name = 'NT1'
p.num = 10
p.name = '虎井 太郎'
p.gender = '男'

print(p.__dict__)  # Instanceの持つ変数の一覧を確認
