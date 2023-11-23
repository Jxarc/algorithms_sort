import analyze_data
import time

def seletion_sort(array):
    for i in range(len(array)):
        analyze_data.statement()

        min_val = i
        analyze_data.statement()

        for j in range(i+1, len(array)):
            analyze_data.statement()

            if array[min_val] > array[j]:
                analyze_data.statement()

                min_val = j
                analyze_data.statement()
        
        temp = array[i]
        analyze_data.statement()

        array[i] = array[min_val]
        analyze_data.statement()

        array[min_val] = temp
        analyze_data.statement()


def test_performance(array, name):
    analyze_data.num_statements = 0

    if analyze_data.print_arrays: print(array)
    start_time = time.time()
    seletion_sort(array)
    end_time = time.time()
    if analyze_data.print_arrays: print(array)

    formatted_time = "{:.12f}".format(end_time - start_time)
    analyze_data.print_results(name, len(array), analyze_data.num_statements, formatted_time)
    return end_time - start_time



