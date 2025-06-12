from typing import List, Any

def combine_list(list1: Any, list2: Any) -> List[Any]:
# def combine_list(list1, list2):
    '''
    2つのリストを結合し、リストで返す

    Args:
        list1: 結合する最初のリスト
        list2: 結合する2番目のリスト

    Returns:
        List[Any]: 結合されたリスト。引数がリストでない場合は、引数を要素とするリスト

    Note:
        - 引数がリストでない場合は、エラーメッセージを出力し、引数を要素とするリストを返します
        - キーワード引数での呼び出しにも対応しています
    '''
    if isinstance(list1, list) and isinstance(list2, list):
        return list1 + list2
    else:
        # print(f'引数がリストではありません。list1: {type(list1)}, list2: {type(list2)}')
        print('引数がリストではありません')
        return [list1, list2]


# main
# 正常な引数
print(combine_list([1, 2, 3], [4, 5, 6]))
print(combine_list(list2=[1, 2, 3], list1=[4, 5, 6]))
# 誤った引数
print(combine_list('a', [1, 2, 3]))
print(combine_list([1, 2, 3], 'xyz'))
print(combine_list(10, 'abc'))
