
def binary_search(base_list, item):
    inferior_limit = 0
    superior_limit = len(base_list) - 1
    while inferior_limit <= superior_limit:
        center = (inferior_limit + superior_limit) // 2
        if base_list[center] < item:
            inferior_limit = center + 1
        elif base_list[center] > item:
            superior_limit = center - 1
        else:
            return True
    return False


def binary_search2(base_limit, item, inferior_limit, superior_limit):
    if inferior_limit <= superior_limit:
        center = (inferior_limit + superior_limit) // 2
        if base_limit[center] == item:
            return True, f"position: {center}"
        elif base_limit[center] < item:
            return binary_search2(base_limit, item, center + 1, superior_limit)
        else:
            return binary_search2(base_limit, item, inferior_limit, center - 1)
    else:
        return False, f"not on list"


if __name__ == "__main__":
    l = [2, 1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    l.sort()
    print(l)
    print(binary_search2(l, 20, 0, len(l) - 1))
