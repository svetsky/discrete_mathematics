'''
Дискретная математика.
Лабораторная работа №4 (часть 2): построение кодов Хаффмана
описание алгоритма Хаффмана (страница 459) https://matematika76.ru/fm/Кормен.pdf
'''
from queue import PriorityQueue

# дерево
class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

# создание C - словарь, в котором ключи - буквы, а значения - частоты соответствующих букв
C = {}
file = open('letter_frequencies.txt')
for line in file:
    C[line[0]] = int(line[3:-1])
file.close()
n = len(C)  # количество различных символов в тексте

# добавляем все элементы словаря C в очередь с приоритетом Q
Q = PriorityQueue()
for key in C:
    char = Node(key, C[key])
    Q.put((C[key], char))

# алгоритм Хаффмана (строим дерево)
for i in range(n-1):
    z = Node()
    char1 = Q.get()
    char2 = Q.get()
    z.left = char1[1]
    z.right = char2[1]
    z.frequency = char1[1].frequency + char1[1].frequency
    Q.put(z.frequency, z)

node = Q.get()











