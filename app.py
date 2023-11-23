import bubble_sort
import heap_sort
import analyze_data
import insertion_sort
import merge_sort
import quick_sort
import selection_sort

#No imprimir los arreglos en consola
analyze_data.print_arrays = False

#Cantidad de elementos a ordenar
analyze_data.generate_ramdon(100)

algorithms = [
    "Bubble sort - Complejidad Big O(N^2)",
    "Heap sort - Complejidad Big O(N log N)",
    "Insertion sort - Complejidad Big O(N^2)",
    "Merge sort - Complejidad Big O(N log N)",
    "Quick sort - Complejidad Big O(N log N)",
    "Selection sort - Complejidad Big O(N^2)"
]

results_array_num = [0] * len(algorithms)
results_array_let = [0] * len(algorithms)

analyze_data.print_head(algorithms[0])
results_array_num[0] = bubble_sort.test_performance(analyze_data.array_num.copy(), 'array_num')
results_array_let[0] = bubble_sort.test_performance(analyze_data.array_let.copy(), 'array_let')

analyze_data.print_head(algorithms[1])
results_array_num[1] = heap_sort.test_performance(analyze_data.array_num.copy(), 'array_num')
results_array_let[1] = heap_sort.test_performance(analyze_data.array_let.copy(), 'array_let')

analyze_data.print_head(algorithms[2])
results_array_num[2] = insertion_sort.test_performance(analyze_data.array_num.copy(), 'array_num')
results_array_let[2] = insertion_sort.test_performance(analyze_data.array_let.copy(), 'array_let')

analyze_data.print_head(algorithms[3])
results_array_num[3] = merge_sort.test_performance(analyze_data.array_num.copy(), 'array_num')
results_array_let[3] = merge_sort.test_performance(analyze_data.array_let.copy(), 'array_let')

analyze_data.print_head(algorithms[4])
results_array_num[4] = quick_sort.test_performance(analyze_data.array_num.copy(), 'array_num')
results_array_let[4] = quick_sort.test_performance(analyze_data.array_let.copy(), 'array_let')

analyze_data.print_head(algorithms[5])
results_array_num[5] = selection_sort.test_performance(analyze_data.array_num.copy(), 'array_num')
results_array_let[5] = selection_sort.test_performance(analyze_data.array_let.copy(), 'array_let')



#Imprimir resultados
worst_algorithm = max(results_array_num) 
worst_algorithm_name = algorithms[results_array_num.index(worst_algorithm)]

best_algorithm = min(results_array_num) 
best_algorithm_name = algorithms[results_array_num.index(best_algorithm)]

analyze_data.print_head("Resultados numéricos")
print("El peor algoritmo: ",worst_algorithm_name.upper())
print("Tiempo utilizado : ","{:.12f}".format(worst_algorithm))
print()

print("El mejor algoritmo: ",best_algorithm_name.upper())
print("Tiempo utilizado: ","{:.12f}".format(best_algorithm))
print()


worst_algorithm = max(results_array_let) 
worst_algorithm_name = algorithms[results_array_let.index(worst_algorithm)]

best_algorithm = min(results_array_let) 
best_algorithm_name = algorithms[results_array_let.index(best_algorithm)]

analyze_data.print_head("Resultados de letras")
print("El peor algoritmo: ",worst_algorithm_name.upper())
print("Tiempo utilizado : ","{:.12f}".format(worst_algorithm))
print()

print("El mejor algoritmo: ",best_algorithm_name.upper())
print("Tiempo utilizado: ","{:.12f}".format(best_algorithm))
print()
