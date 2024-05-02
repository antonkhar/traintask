import numpy as np
import pandas as pd

# Генерация случайных объемов поставок и потребностей
supplies = np.random.randint(50, 200, size=(100,))
demands = np.random.randint(1, 20, size=(1000,))

# Генерация случайных стоимостей перевозок
costs = np.random.randint(10, 100, size=(100, 1000))

# Создание DataFrame для supplies и demands
df_supplies = pd.DataFrame({'Supplies': supplies})
df_demands = pd.DataFrame(demands, columns=['Demand'])

# Объединение supplies и demands с основным DataFrame
df_data = pd.concat([df_supplies, pd.DataFrame(costs)], axis=1)

# Сохранение данных в виде матрицы в файл Excel
df_data.to_excel("transport.xlsx", index=False)

# Считывание данных из файла Excel
df_data = pd.read_excel("transport.xlsx")

# Преобразование DataFrame в numpy array
costs = df_data.iloc[:, 1:].to_numpy()

# Создание списка для хранения путей
paths = []

# Расчет оптимальных путей
while np.sum(supplies) > 0 and np.sum(demands) > 0:
    # Находим индексы минимального элемента в матрице стоимостей
    min_index = np.unravel_index(np.argmin(costs), costs.shape)
    
    # Определяем объем поставки
    supply = min(supplies[min_index[0]], demands[min_index[1]])
    
    # Добавляем путь в список
    paths.append((min_index[0] + 1, min_index[1] + 1, supply))
    
    # Уменьшаем объемы поставок и потребностей
    supplies[min_index[0]] -= supply
    demands[min_index[1]] -= supply
    
    # Удаляем строку или столбец, в зависимости от того, какой из них полностью обслужен
    if supplies[min_index[0]] == 0:
        costs = np.delete(costs, min_index[0], axis=0)
        supplies = np.delete(supplies, min_index[0])
    else:
        costs = np.delete(costs, min_index[1], axis=1)
        demands = np.delete(demands, min_index[1])

# Создание DataFrame для выходной матрицы
output_matrix = np.zeros((100, 1000))
for path in paths:
    output_matrix[path[0] - 1, path[1] - 1] = path[2]

# Запись выходной матрицы в файл Excel
df_output_matrix = pd.DataFrame(output_matrix)
df_output_matrix.to_excel("transportation_output_matrix.xlsx", index=False, header=False)

# Запись результатов путей перевозок в текстовый файл
with open("transportation_paths.txt", "w") as file:
    for path in paths:
        file.write(f"Со склада {path[0]} везем к покупателям {path[1]} в количестве {path[2]} единиц\n")

# Вывод результатов
print("Пути перевозок записаны в файл transportation_paths.txt")
print("Выходная матрица записана в файл transportation_output_matrix.xlsx")
