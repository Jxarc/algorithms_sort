import analyze_data
import time;

def merge_sort(arr):
    analyze_data.statement()
    if len(arr) == 1: return arr

    middle = len(arr)//2
    analyze_data.statement()

    left_array = arr[:middle]
    analyze_data.statement()

    right_array = arr[middle:]
    analyze_data.statement()

    sorted_left_array = merge_sort(left_array)
    analyze_data.statement()

    sorted_right_array = merge_sort(right_array)
    analyze_data.statement()

    return merge_array(sorted_left_array, sorted_right_array)

def merge_array(left_arr, right_arr):
    arr_resultado = []
    analyze_data.statement()

    while len(left_arr) > 0 and len(right_arr) > 0:
        analyze_data.statement()

        if left_arr[0] > right_arr[0]:
            analyze_data.statement()

            arr_resultado.append(right_arr[0])
            analyze_data.statement()

            right_arr.pop(0)
            analyze_data.statement()
        else:
            arr_resultado.append(left_arr[0])
            analyze_data.statement()

            left_arr.pop(0)
            analyze_data.statement()

    while len(left_arr)>0:
        analyze_data.statement()

        arr_resultado.append(left_arr[0])
        analyze_data.statement()

        left_arr.pop(0)
        analyze_data.statement()

    while len(right_arr)>0:
        analyze_data.statement()

        arr_resultado.append(right_arr[0])
        analyze_data.statement()

        right_arr.pop(0) 
        analyze_data.statement()

    return arr_resultado;       

def test_performance(array, name):
    analyze_data.num_statements = 0

    if analyze_data.print_arrays: print(array)
    start_time = time.time()
    res = merge_sort(array)
    end_time = time.time()
    if analyze_data.print_arrays: print(res)

    formatted_time = "{:.12f}".format(end_time - start_time)
    analyze_data.print_results(name, len(array), analyze_data.num_statements, formatted_time)
    return end_time - start_time

