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