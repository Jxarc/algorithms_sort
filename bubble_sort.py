import analyze_data
import time

def bubble_sort(array):
    
    for i in range(len(array)):
        analyze_data.statement()

        for j in range(len(array)-i-1):
            analyze_data.statement()

            if array[j] > array[j+1]:
                analyze_data.statement()

                temp = array[j]
                analyze_data.statement()

                array[j] = array[j+1]
                analyze_data.statement()

                array[j+1]= temp
                analyze_data.statement()


def test_performance(array, name):
    analyze_data.num_statements = 0
    
    if analyze_data.print_arrays: print(array)
    start_time = time.time()
    bubble_sort(array)
    end_time = time.time()
    if analyze_data.print_arrays: print(array)

    formatted_time = "{:.12f}".format(end_time - start_time)
    analyze_data.print_results(name, len(array), analyze_data.num_statements, formatted_time)
    return end_time - start_time




