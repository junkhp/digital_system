# -*- coding: utf-8 -*-


def check_setcover(indexes_list, elements, correct_setcover):
    '''全ての要素をカバーできているかどうかをチェック'''
    setcover = set()
    for idx in indexes_list:
        for e in elements[idx]:
            setcover.add(e)
    print('カバーできている要素')
    print(setcover)
    if setcover == correct_setcover:
        return False
    else:
        return True


def main():
    # 全要素の集合
    set_cover = {1, 2, 3, 4, 5, 6}
    # 要素の数
    num_elements = len(set_cover)
    # 集合
    sets = [
        [1, 2, 3],
        [3, 2],
        [4, 5],
        [1, 6],
        [3, 5],
        [2]
    ]
    # 集合の数
    num_sets = len(sets)
    # 密な集合のリストを疎なリストに変換
    sets_list = [[0] * num_elements for i in range(num_sets)]
    for i, s in enumerate(sets):
        for element in s:
            sets_list[i][element - 1] = 1

    # 各集合の重み
    s_weights = [4, 6, 3, 2, 2, 6]

    # チェック済みのインデックス
    checked_indexes = []
    sets_copy = sets_list.copy()
    all_value = 0
    while(check_setcover(checked_indexes, sets, set_cover)):
        print('------------------------------------------------')
        print('チェック済みのインデックス')
        print(checked_indexes)
        min_weight = 100
        for j, s in enumerate(sets_copy):
            # 空集合でないかを確認
            if sum(s) != 0:
                value = s_weights[j]/sum(s)
            else:
                continue
            if value < min_weight:
                min_weight = value
                min_index = j
        all_value += min_weight
        checked_indexes.append(min_index)
        for i in range(num_sets):
            for e in sets[min_index]:
                sets_copy[i][e-1] = 0
    
    print('必要な集合のインデックス')
    print(checked_indexes)
    print('コスト')
    print(all_value)

if __name__ == "__main__":
    main()