"""Задача NumPy: экспрессия одного гена в пяти образцах."""
import numpy as np

expression = np.array([12, 18, 9, 25, 16])

# 1. Среднее значение экспрессии
mean = expression.mean()
print("Среднее:", mean)

# 2. Минимум и максимум
print("Минимум:", expression.min())
print("Максимум:", expression.max())

# 3. Индекс образца с максимальной экспрессией (нумерация с 0)
idx = expression.argmax()
print(f"Максимум в образце с индексом {idx} (это {idx + 1}-й образец)")

# 4. Только значения выше среднего — булева маска
above = expression[expression > mean]
print("Выше среднего:", above)

# 5. Сортировка по возрастанию (исходный массив не меняется)
print("Отсортировано:", np.sort(expression))
print("Исходный не изменился:", expression)
