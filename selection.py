'''
implimentations of selection algorithms
'''

from sorting import merge_sort


def sort_select(i, input_list):
    '''
    sorts list using merge sort then returns selected ith smallest element (zero indexed)
    '''
    if not 0 <= i <= len(input_list):
        raise IndexError('Invalid index argument passed.  Needs to be in range (0, length of list)')
    sorted_input = merge_sort(input_list)
    return sorted_input[i]


def pivot_select(i, input_list, pivot=0.5):
    '''
    pivot selection algo to find i smallest element (zero indexed) of input input_list
    '''
    if not 0 < pivot < 1:
        raise ValueError('Pivot outside of acceptable range (0,1)')
    length = len(input_list)
    if length == 0:
        raise ValueError('Empty list given')
    if length == 1:
        return input_list[0]
    if not 0 <= i <= length:
        raise IndexError('Invalid index argument passed.  Needs to be in range (0, length of list)')
    pivot_index = int(length * pivot)
    pivot_value = input_list[pivot_index]
    left = []
    right = []
    same = []
    for element in input_list:
        if element < pivot_value:
            left.append(element)
        elif element > pivot_value:
            right.append(element)
        else:
            same.append(element)
    size_left = len(left)
    size_middle = len(same)
    if size_left < i+1 <= size_left + size_middle:
        return same[0]
    elif i+1 <= size_left:
        return randomized_select(i, left)
    else:
        return randomized_select(i-(size_left + size_middle), right)
