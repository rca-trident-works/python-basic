# 与えられたリストから偶数のみを取り出して新しいリストを作成し出力する

m_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

n = [i for i in m_list if i % 2 == 0]

print('元のデータ: ' + str(m_list))
print('偶数のリスト: ' + str(n))
