def draw_rectangle(width, height):
    print('-' * width)
    for i in range(height-2):
        print('|' + ' '*(width-2) + '|')
    if height > 1:
        print('-' * width)
        draw_rectangle(10, 3)