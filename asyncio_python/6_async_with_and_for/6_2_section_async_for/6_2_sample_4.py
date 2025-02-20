"""
async for в выражениях-генераторах:
    Для асинхронного async for можно использовать короткий синтаксис. Действует только в теле
    асинхронной функции (сопрограммы) async def.
# асинхронное выражение-генератор:
    (i ** 2 async for i in agen()).
# асинхронное список-выражение:
    [i async for i in agen()]
# асинхронное словарь-выражение:
    {i: i ** 2 async for i in agen()} ;
    {k: v async for k, v in adict.items()}
# асинхронное выражение-множество:
    {i async for i in agen()}
Разрешено использование await при использовании короткого синтаксиса для асинхронных и для
синхронных конструкций, если fun()/vfun() - это корутины.
# на примере списка-выражения
    result = [await fun() for fun in funcs]
    result = [await fun() for fun in funcs if await smth]
    result = [await fun() async for fun in funcs]
    result = [await fun() async for fun in funcs if await smth]
# также справедливо для словарей и других конструкций
    {k: await vfun() async for k, vfun in funcs_dict.items()}
В асинхронных коротких конструкциях также можно использовать условия if/else. В условиях тоже
может быть await, если условие - это корутина.
# Асинхронное словарь-выражение с условием:
    {k: await vfun() async for k, vfun in funcs_dict.items() if await conditionfun(k)}
"""