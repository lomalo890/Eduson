'''Напишите функцию find_unique_elements, которая принимает 
на вход список lst и возвращает список уникальных элементов 
этого списка. Используйте встроенные функции. Отсортируйте результат 
по возрастанию.
'''

def find_unique_elements(lst):
    return sorted(list(set(lst)))

'''
Напишите функцию sums_by_quarter, которая принимает список чисел (показаний 
термометра с января по декабрь) и возвращает список сумм значений 
по кварталам. Каждый квартал состоит из трех месяцев, и список должен быть 
разбит на соответствующие кварталам элементы. При этом, каждый квартал должен 
быть представлен одним числом - суммой элементов в этом квартале. 
'''

def sums_by_quarter(lst):
    result = []
    for i in range(0, len(lst) - 1, 3):
        j = i + 1
        k = i + 2
        result.append(lst[i] + lst[j] + lst[k])
    return result


'''
Напишите функцию sorted_unique_list, которая принимает список чисел и возвращает 
список, отсортированный по возрастанию и без повторяющихся элементов. Используйте 
специальную функцию.
'''
def sorted_unique_list(lst):
    return sorted(list(set(lst)))

'''
Напишите функцию count_frequency, которая принимает список имен (строк) и возвращает 
словарь, содержащий количество упоминаний каждого имени в списке. Словарь должен быть 
отсортирован по ключам в алфавитном порядке.
'''

def count_frequency(names):
    return {k: names.count(k) for k in names}


'''
Напишите функцию flatten_nested_list, которая принимает в качестве аргумента 
вложенный список (список списков) и возвращает плоский список, состоящий из всех элементов вложенных списков.
'''

def flatten_nested_list(subber):
    result = []
    for element in subber:
        if isinstance(element, list):
            result = result + element
        else:
            result.append(element)
    return result


'''
Напишите функцию process_commands, которая принимает на вход список 
команд и выполняет их. Каждая команда представляет собой строку, которая 
может быть одной из следующих: * execute: добавляет текущий индекс 
выполнения команды в список результатов; * skip: игнорирует команду и 
переходит к следующей; * stop: прекращает выполнение команд.

Функция process_commands должна возвращать список всех индексов выполнения 
команд.
'''

def process_commands():
    id = 1
    lst = []
    command = ''
    while not 'stop' in command:
        command = input()
        if 'execute' in command:
            lst.append(str(id) + f' {command}')
        elif 'skip' in command:
            continue
    print(lst)

process_commands()







    
