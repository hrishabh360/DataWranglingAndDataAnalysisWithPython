def add_arrays(x, y):
    z = []
    for x_elm, y_elm in zip(x, y):
        z.append(x_elm + y_elm)
    return z