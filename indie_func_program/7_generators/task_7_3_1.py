def grep(pattern: str):
    while True:
        text: str = yield
        if pattern.lower() in text.lower():
            print(text)


search = grep('кору')
next(search)
search.send("Короед любит есть дерево")
search.send("Корутины полезно знать")
search.send("Ненавижу бесконченые циклы")
search.send("Ору с это задачи")
search.send("Какая же эта тема про корутины непонятная")
search.close()
