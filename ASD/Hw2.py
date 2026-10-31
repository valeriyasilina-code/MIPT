n = int(input())  # количество параметров в формуле
a = [int(i) for i in input().split()]  # параметры

d = int(input())  # количество объектов

docs = []  # числовые признаки каждого объекта
scores = []  # общая оценка документа

for i in range(d):
    doc = [int(j) for j in input().split()]
    docs.append(doc)  # записываем оценки по отдельности, чтобы потом легко пересчитать
    score = sum([a[j] * doc[j] for j in range(n)])
    scores.append(score)  # записываем общий скор для ранжирования

# Создаем список пар (скор, исходный индекс) и сортируем его один раз при старте
items = [(scores[i], i) for i in range(d)]
items.sort(key=lambda x: (-x[0], x[1]))
print(items)

q = int(input())  # количество запросов

ans = []

for i in range(q):
    z = [int(j) for j in input().split()]
    if z[0] == 1:
        k = z[1]
        res = [str(j[1]+1) for j in items[:k]]
        ans.append(" ".join(res))

    elif z[0] == 2:
        i_doc = z[1] - 1
        j = z[2] - 1
        v = z[3]

        old_v = docs[i_doc][j]
        scores[i_doc] = scores[i_doc] - a[j] * old_v + a[j] * v
        docs[i_doc][j] = v


        pos = 0
        for t in range(d):
            if items[t][1] == i_doc:
                pos = t
                break

        item = (scores[i_doc], i_doc)

        new_pos = 0
        while new_pos < len(items) and (
                items[new_pos][0] > item[0] or (items[new_pos][0] == item[0] and items[new_pos][1] < item[1])):
            new_pos += 1

        if pos != new_pos:
            if pos < new_pos:
                items[pos:new_pos] = items[pos + 1:new_pos + 1]
                items[new_pos] = item
            else:

                items[new_pos + 1:pos + 1] = items[new_pos:pos]
                items[new_pos] = item

for line in ans:
    print(line)
