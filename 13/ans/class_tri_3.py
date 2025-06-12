from pprint import pprint


class TridentStudent:
    pass


# main
p = TridentStudent()
p.class_name = 'NT1'
p.num = 10
p.name = '虎井 太郎'
p.gender = '男'

pprint(p.__dict__)
