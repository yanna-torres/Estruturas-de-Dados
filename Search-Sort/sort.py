

def bubble_sort(input_list):
    s = len(input_list)
    for i in range(s):
        for j in range(0, s - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]


def insertion_sort(input_list):
    s = len(input_list)
    for i in range(1, s):
        j = i
        while j > 0 and input_list[j - 1] > input_list[j]:
            input_list[j], input_list[j - 1] = input_list[j - 1], input_list[j]
            j -= 1


def selection_sort(input_list):
    s = len(input_list)
    for i in range(s):
        min_index = i
        for j in range(i + 1, s):
            if input_list[j] < input_list[min_index]:
                min_index = j

        if input_list[min_index] != input_list[i]:
            input_list[i], input_list[min_index] = input_list[min_index], input_list[i]


def qsort(input_list):
    if len(input_list) < 2:
        return input_list
    else:
        menores = [i for i in input_list[1:] if i <= input_list[0]]
        maiores = [i for i in input_list[1:] if i >= input_list[0]]
        return qsort(menores) + [input_list[0]] + qsort(maiores)


def merge_sort(input_list):
    if len(input_list) == 1:
        return input_list
    else:
        half = len(input_list) // 2
        left = merge_sort(input_list[:half])
        right = merge_sort(input_list[half:])
        return merge(left, right)


def merge(input_list1, input_list2):
    final = []
    while len(input_list1) != 0 and len(input_list2) != 0:
        if input_list1[0] > input_list2[0]:
            final.append(input_list2[0])
            input_list2.pop(0)
        else:
            final.append(input_list1[0])
            input_list1.pop(0)

    while len(input_list1) != 0:
        final.append(input_list1[0])
        input_list1.pop(0)

    while len(input_list2) != 0:
        final.append(input_list2[0])
        input_list2.pop(0)

    return final
