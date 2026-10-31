#время o(n*k) за счет цикла for
#память o(k) два списка по k+1

prices = [3, 2, 6, 5, 0, 3]
k = 2 #количество сделок

#prices =[int(i) for i in input().split()]
#k=int(input())

akc0 = [0] * (k + 1) #тут храним прибыль без акций на руках
akc1 = [-float('inf')] * (k + 1) #тут прибыль с акциями на руках

for price in prices:
    for j in range(k, 0, -1):
        akc0[j] = max(akc0[j], akc1[j] + price)  # либо ничего не делаем, либо продаем акции
        akc1[j] = max(akc1[j], akc0[j - 1] - price) #либо ничего не делаем, либо покупаем акции на деньги, которые были вчера
        print(price, akc0, akc1)
print("Максимальная прибыль:", akc0[k])
