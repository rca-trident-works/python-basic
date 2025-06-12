vote_box = []   # 投票箱
label = '票'


def vote():
    """投票を行い、投票箱に「票」を追加する"""
    print('投票します')
    vote_box.append(label)


def reset_box():
    """投票箱を空にする"""
    print('箱を空にします')
    vote_box.clear()


def check_box():
    """投票箱内の票を数える"""
    print('票の数は{}です'.format(len(vote_box)), end=" ")
    print('vote_box:', vote_box)


# main
check_box()
for i in range(10):
    vote()

check_box()
reset_box()
vote()
vote()
check_box()
