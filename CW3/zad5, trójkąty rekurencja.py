def draw_triangle(level):
    if level == 0:
        return
    draw_triangle(level - 1)
    print('*' * level)

level1 = int(input("ilu poziomowy ma byc trójkąt? "))
draw_triangle(level1)
