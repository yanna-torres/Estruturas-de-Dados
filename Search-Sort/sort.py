from functools import reduce


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

