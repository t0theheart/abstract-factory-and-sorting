

def selection_sort(array: list):
    for i in range(len(array)):
        lowest_value_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[lowest_value_index]:
                lowest_value_index = j
        array[i], array[lowest_value_index] = array[lowest_value_index], array[i]
