import analyze_data
import time

array_num = analyze_data.array_num
array_let = analyze_data.array_let

def heap_sort(array):
    for i in range(len(array)//2, -1, -1):
        analyze_data.statement()

        heapify(array, len(array), i)
        analyze_data.statement()

    for i in range(len(array)-1, 0, -1):
        analyze_data.statement()

        temp = array[i]
        analyze_data.statement()

        array[i] = array[0]
        analyze_data.statement()

        array[0] = temp
        analyze_data.statement()

        heapify(array, i, 0)
        analyze_data.statement()

def heapify(array, n, i):
    largest = i
    analyze_data.statement()

    left = 2*i+1
    analyze_data.statement()

    right = 2*i+2
    analyze_data.statement()

    if left < n and array[left] > array[largest]:
        analyze_data.statement()

        largest = left
        analyze_data.statement()

    if right < n and array[right] > array[largest]:
        analyze_data.statement()

        largest = right
        analyze_data.statement()

    if largest != i:
        analyze_data.statement()

        temp = array[i]
        analyze_data.statement()

        array[i] = array[largest]
        analyze_data.statement()

        array[largest] = temp
        analyze_data.statement()

        heapify(array, n, largest)
        analyze_data.statement()

def test_performance(array, name):
    analyze_data.num_statements = 0

    if analyze_data.print_arrays: print(array)
    start_time = time.time()
    heap_sort(array)
    end_time = time.time()
    if analyze_data.print_arrays: print(array)

    formatted_time = "{:.12f}".format(end_time - start_time)
    analyze_data.print_results(name, len(array), analyze_data.num_statements, formatted_time)
    return end_time - start_time



