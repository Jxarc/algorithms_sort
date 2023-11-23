import random
import string

print_arrays = True
num_statements = 0

array_num = []
array_let = []


def statement():
    global num_statements
    num_statements +=1

def generate_ramdon(lenght):
    global array_num, array_let

    array_num = [random.randint(1, 100) for _ in range(lenght)]
    array_let = [random.choice(string.ascii_uppercase) for _ in range(lenght)]

def print_head(title):
    print('\n\n------------------------------------')
    print(title)
    print('------------------------------------\n')

def print_results(name,lenght,statements,time):
    print(f"Cantidad de elementos en {name}:",lenght)
    print('Cantidad de sentencias ejecutadas: ', statements)
    print('Cantidad de tiempo utilizado: ', time)
    print()