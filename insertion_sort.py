import analyze_data
import time

def insertion_sort(array):
    for i in range(len(array)):
        analyze_data.statement()

        current = array[i]
        analyze_data.statement()
        
        j = i-1
        analyze_data.statement()

        while j >= 0 and array[j] > current:
            analyze_data.statement()

            array[j+1] = array[j]
            analyze_data.statement()

            j = j-1
            analyze_data.statement()

        array[j+1] = current
        analyze_data.statement()


def test_performance(array, name):
    analyze_data.num_statements = 0

    if analyze_data.print_arrays: print(array)
    start_time = time.time()
    insertion_sort(array)
    end_time = time.time()
    if analyze_data.print_arrays: print(array)

    formatted_time = "{:.12f}".format(end_time - start_time)
    analyze_data.print_results(name, len(array), analyze_data.num_statements, formatted_time)
    return end_time - start_time