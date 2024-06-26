# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |                |              |
#         |         позиционные или       |
#         |         по ключу               - только по ключевому слову
#         |
#          -- только по позиции

def make_circle(pos1, /, *, kwd1, **kwargs):
    # Теперь для вызова функции make_circle() нам нужно передать значения всех аргументов только позиционно. Такой разделитель можно использовать только один раз в определении функции. Его нельзя применять в функциях с неограниченным количеством позиционных аргументов после *args !!!
    print(pos1)
    print(kwd1)
    print(kwargs)


make_circle(2, kwd1=4, name=3, m=5)
