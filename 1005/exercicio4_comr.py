def div(dividendo, divisor):
    if dividendo < divisor:
        return dividendo
    else:
        return div(dividendo - divisor, divisor)
    
print(div(20, 3))