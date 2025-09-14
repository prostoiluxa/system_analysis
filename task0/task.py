import csv
from io import StringIO

def main(csv_string: str) -> list[list[int]]:
    # Преобразуем строку в файлоподобный объект
    csv_file = StringIO(csv_string)
    
    # Читаем данные и собираем вершины
    reader = csv.reader(csv_file)
    vertices = set()
    edges = []
    
    for row in reader:
        if len(row) < 2:
            continue
        v1, v2 = int(row[0]), int(row[1])
        edges.append((v1, v2))
        vertices.add(v1)
        vertices.add(v2)
    
    # Сортируем вершины для consistent ordering
    sorted_vertices = sorted(vertices)
    n = len(sorted_vertices)
    
    # Создаем mapping от вершины к индексу
    vertex_to_index = {v: i for i, v in enumerate(sorted_vertices)}
    
    # Инициализируем матрицу нулями
    matrix = [[0] * n for _ in range(n)]
    
    # Заполняем матрицу смежности
    for v1, v2 in edges:
        i, j = vertex_to_index[v1], vertex_to_index[v2]
        matrix[i][j] = 1
        matrix[j][i] = 1  # граф неориентированный
    
    # Сохраняем матрицу в CSV файл
    with open('adjacency_matrix.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(matrix)
    
    return matrix

def csv_file_to_string(file_path: str) -> str:
    """Читает CSV файл и возвращает его строковое представление"""
    with open(file_path, 'r') as f:
        return f.read()

# Пример использования
if __name__ == '__main__':
    # Пример чтения из файла и преобразования в строку
    csv_content = csv_file_to_string('/Users/ilagorbacev/Documents/edu/1-25/sa/task0/task2.csv')
    
    # Передача строкового представления в main
    result_matrix = main(csv_content)
    
    # Вывод результата для проверки
    print("Матрица смежности:")
    for row in result_matrix:
        print(row)