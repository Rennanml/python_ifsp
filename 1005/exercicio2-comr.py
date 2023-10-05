def potencia(x, y):
    if y == 1:
        return x
    else:
        return x * potencia(x , y - 1)
    
print(potencia(2, 3))