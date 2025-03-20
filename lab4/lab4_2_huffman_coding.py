'''
Дискретная математика.
Лабораторная работа №4 (часть 2): построение кодов Хаффмана
описание алгоритма Хаффмана (страница 459) https://matematika76.ru/fm/Кормен.pdf
'''
from queue import PriorityQueue
import itertools

# Дерево
class Node:
    def __init__(self, symbol=None, frequency=None):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.frequency < other.frequency

'''
# создание C - словарь, в котором ключи - буквы, а значения - частоты соответствующих букв
C = {}
file = open('letter_frequencies.txt')
for line in file:
    char, frequency = line.split()
    C[char] = int(frequency)
file.close()
'''
C = {'A': 10, 'B': 5, 'C': 7, 'D': 1, 'E': 6}
n = len(C)  # количество различных символов в тексте

# Добавляем все элементы словаря C в очередь с приоритетом Q
Q = PriorityQueue()
unique_id = itertools.count() 
for key, freq in C.items():
    char = Node(key, freq)
    Q.put((freq, next(unique_id), char))  

# Алгоритм Хаффмана (строим дерево)
for i in range(n - 1):
    # Берём два узла с наименьшей частотой
    freq1, _, char1 = Q.get()
    freq2, _, char2 = Q.get()

    # Создаём новый узел z
    z = Node(frequency=freq1 + freq2)
    z.left = char1
    z.right = char2
    Q.put((z.frequency, next(unique_id), z)) 

# корень дерева
root = Q.get()[2]

# Функция для генерации кодов Хаффмана
def generate_huffman_codes(node, code="", code_dict=None):
    if code_dict is None:
        code_dict = {}
    if node.symbol:
        code_dict[node.symbol] = code
    else:
        generate_huffman_codes(node.left, code + "0", code_dict)
        generate_huffman_codes(node.right, code + "1", code_dict)
    return code_dict


huffman_codes = generate_huffman_codes(root)
print("Коды Хаффмана:")
for symbol, code in huffman_codes.items():
    print(f"Символ: {symbol}, Код: {code}")











