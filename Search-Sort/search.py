
def binary_search(input_list, item):
    inferior_limit = 0
    superior_limit = len(input_list) - 1
    while inferior_limit <= superior_limit:
        center = (inferior_limit + superior_limit) // 2
        if input_list[center] < item:
            inferior_limit = center + 1
        elif input_list[center] > item:
            superior_limit = center - 1
        else:
            return True
    return False


def binary_search2(input_list, item, inferior_limit, superior_limit):
    if inferior_limit <= superior_limit:
        center = (inferior_limit + superior_limit) // 2
        if input_list[center] == item:
            return True, f"position: {center}"
        elif input_list[center] < item:
            return binary_search2(input_list, item, center + 1, superior_limit)
        else:
            return binary_search2(input_list, item, inferior_limit, center - 1)
    else:
        return False, f"not on list"
