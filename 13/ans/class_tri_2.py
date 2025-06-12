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

q = TridentStudent()
q.class_name = 'ST2'
q.num = 30
q.name = '河合 花子'
q.gender = '女'

pprint(q.__dict__)
pprint(p.__dict__)
