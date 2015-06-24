'''
some list sorting functions
'''


def is_sorted(input_list):
    '''
    tests whether input list is sorted
    '''
    if len(input_list) == 0 or len(input_list) == 1:
        return True
    if input_list[0] > input_list[1]:
        return False
    else:
        return is_sorted(input_list[1:])


def bubble_sort(input_list):
    '''
    sort using bubble sort algorithm
    '''
    while is_sorted(input_list) is False:
        for i in range(len(input_list)-1):
            value = input_list[i]
            next_value = input_list[i+1]
            if value > next_value:
                input_list[i] = next_value
                input_list[i+1] = value
    return input_list


def merge_sort(input_list):
    '''
    sorts using merge sort algorithm.  depends on merge_two_lists()
    '''
    length = len(input_list)
    if length < 2:
        return input_list
    middle = length / 2
    left = input_list[:middle]
    right = input_list[middle:]
    return merge_two_lists(merge_sort(left), merge_sort(right))


def merge_two_lists(left, right):
    '''
    merges two lists, if both are in order result is in order
    '''
    out_list = []
    while len(left) != 0 and len(right) != 0:
        if left[0] < right[0]:
            out_list.append(left[0])
            left = left[1:]
        elif right[0] < left[0]:
            out_list.append(right[0])
            right = right[1:]
        else:
            out_list.append(left[0])
            left = left[1:]
    if len(left) != 0:
        out_list += left
    if len(right) != 0:
        out_list += right
    return out_list


def quick_sort(input_list, pivot=0.5):
    '''
    sort using quick sort / pivot sort
    '''
    if 0 < pivot < 1:
        raise ValueError('Pivot outside of acceptable range (0,1)')
    length = len(input_list)
    if length == 0 or length == 1:
        return input_list
    pivot_index = int(length*pivot)
    pivot_value = input_list[pivot_index]
    left = []
    right = []
    same = []
    for element in input_list:
        if element < pivot_value:
            left.append(element)
        if element > pivot_value:
            right.append(element)
        if element == pivot_value:
            same.append(element)
    return quick_sort(left) + same + quick_sort(right)
