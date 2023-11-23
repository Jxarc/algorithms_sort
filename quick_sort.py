import analyze_data
import time

statements = 0

def move_to_pivote(array, min_val, pivote):
    global statements

    for i in range(len(array)): 
        analyze_data.statement()

        value = array[i]
        analyze_data.statement()
        
        if value <= pivote: 
            analyze_data.statement()
            
            min_val = min_val+1
            analyze_data.statement()
            
            array[i] = array[min_val]
            analyze_data.statement()

            array[min_val] = value
            analyze_data.statement()

    return min_val


def quick_sort(arr):
    if len(arr) <= 1 : return arr

    pi = move_to_pivote(arr,-1, arr[len(arr)-1])
    analyze_data.statement()
    
    new_arr = arr[:pi]
    analyze_data.statement()

    new_arr2 = arr[pi:]
    analyze_data.statement()

    result1 = quick_sort(new_arr)
    analyze_data.statement()

    result2 = quick_sort(new_arr2)
    analyze_data.statement()

    return result1 + result2


def test_performance(array, name):
    analyze_data.num_statements = 0

    if analyze_data.print_arrays: print(array)
    start_time = time.time()
    res = quick_sort(array)
    end_time = time.time()
    if analyze_data.print_arrays: print(res)

    formatted_time = "{:.12f}".format(end_time - start_time)
    analyze_data.print_results(name, len(array), analyze_data.num_statements, formatted_time)
    return end_time - start_time





