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

    # Переопределяем метод сравнения для работы с PriorityQueue
    def __lt__(self, other):
        return self.frequency < other.frequency

# создание C - словарь, в котором ключи - буквы, а значения - частоты соответствующих букв
file = open('letter_frequencies.txt')
lst = []
for line in file:
    lst.append(line)
file.close()
C = {}
i = 0
while i < len(lst):
    if len(lst[i])>2:
        char, frequency = lst[i].split(': ')
        C[char] = int(frequency)
    else:
        C['\n'] = int(lst[i+1].replace(': ', ''))
        i += 1
    i += 1
print(C)
'''
C = {'A': 10, 'B': 5, 'C': 7, 'D': 1, 'E': 6}
'''
n = len(C)  # количество различных символов в тексте

# Добавляем все элементы словаря C в очередь с приоритетом Q
Q = PriorityQueue()
unique_id = itertools.count()  # Уникальный идентификатор для узлов
for key, freq in C.items():
    char = Node(key, freq)
    Q.put((freq, next(unique_id), char))  # Добавляем уникальный идентификатор

# Алгоритм Хаффмана (строим дерево)
for i in range(n - 1):
    # Берём два узла с наименьшей частотой
    freq1, _, char1 = Q.get()
    freq2, _, char2 = Q.get()

    # Создаём новый узел z
    z = Node(frequency=freq1 + freq2)
    z.left = char1
    z.right = char2
    Q.put((z.frequency, next(unique_id), z))  # Добавляем уникальный идентификатор

# Получаем корень дерева
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


# Генерация кодов Хаффмана
huffman_codes = generate_huffman_codes(root)

# Вывод кодов Хаффмана
print("Коды Хаффмана:")
for symbol, code in huffman_codes.items():
    print(f"Символ: {symbol}, Код: {code}")

# Кодируем текст
missed_chars = set()
text = open('text.txt')
encoded = open('encoded_text.txt', 'w')
for line in text:
    for char in line:
        if char not in huffman_codes:
            missed_chars.add(char)
            continue
        encoded.write(huffman_codes[char])
encoded.close()
text.close()

if missed_chars:
    print('Прорущенные символы:', missed_chars)









