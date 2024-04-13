def make_circle(x, y, radius, *, line_width=1, fill=True):
    #Здесь * выступает разделителем: отделяет обычные аргументы (их можно указывать по имени и позиционно) от строго именованных.
    print(x, y, radius)
    print(line_width, fill)

# x=10, y=20, radius=5,  line_width=1, fill=True
make_circle(10, 20, 5)  

# x=10, y=20, radius=7,  line_width=1, fill=True
make_circle(x=10, y=20, radius=7)

# x=10, y=20, radius=10, line_width=2, fill=False
make_circle(10, 20, radius=10, line_width=2, fill=False)

# x=10, y=20, radius=17, line_width=3, fill=True
make_circle(x=10, y=20, radius=17, line_width=3)

#То есть аргументы x, y и radius могут быть переданы в качестве как позиционных, так и именованных аргументов. При этом аргументы line_width и fill могут быть переданы только как именованные аргументы.

# make_circle(10, 20, 15, 20)
# make_circle(x=10, y=20, 15, True)
# make_circle(10, 20, 10, 2, False)