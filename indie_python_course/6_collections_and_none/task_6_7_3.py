supermarket = {
    "milk": {"quantity": 20, "price": 1.19},
    "biscuits": {"quantity": 32, "price": 1.45},
    "butter": {"quantity": 20, "price": 2.29},
    "cheese": {"quantity": 15, "price": 1.90},
    "bread": {"quantity": 15, "price": 2.59},
    "cookies": {"quantity": 20, "price": 4.99},
    "yogurt": {"quantity": 18, "price": 3.65},
    "apples": {"quantity": 35, "price": 3.15},
    "oranges": {"quantity": 40, "price": 0.99},
    "bananas": {"quantity": 23, "price": 1.29}
}
summa = 0
for _, q in supermarket.items():
    summa += q['quantity'] * q['price']
print(summa)



s_1, s_2 = {}, {}
for i in range(2):
    temp = s_2 if i else s_1
    line = input()
    for w in line:
        temp[w] = temp.get(w, 0) + 1
print('YES' if s_1 == s_2 else 'NO')
