from pprint import pprint


class TridentStudent:
    '''Trident学生管理クラス'''
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

pprint(p.__dict__)
pprint(TridentStudent.__dict__)
