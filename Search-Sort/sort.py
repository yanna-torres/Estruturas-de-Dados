
def bubble_sort(list_to_sort):
    s = len(list_to_sort)
    for i in range(s):
        for j in range(0, s - i - 1):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]


def insertion_sort(list_to_sort):
    s = len(list_to_sort)
    for i in range(1, s):
        j = i
        while j > 0 and list_to_sort[j - 1] > list_to_sort[j]:
            list_to_sort[j], list_to_sort[j - 1] = list_to_sort[j - 1], list_to_sort[j]
            j -= 1


def selection_sort(list_to_sort):
    s = len(list_to_sort)
    for i in range(s):
        min_index = i
        for j in range(i + 1, s):
            if list_to_sort[j] < list_to_sort[min_index]:
                min_index = j

        if list_to_sort[min_index] != list_to_sort[i]:
            list_to_sort[i], list_to_sort[min_index] = list_to_sort[min_index], list_to_sort[i]


if __name__ == "__main__":
    l = [6, 3, 5, 4, 2]
    bubble_sort(l)
    print(l)

    l = [1, 6, 5, 4, 2, 3]
    insertion_sort(l)
    print(l)

    l = [6, 3, 5, 4, 2]
    selection_sort(l)
    print(l)
