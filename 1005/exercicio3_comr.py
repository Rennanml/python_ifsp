def div(dividendo, divisor):
    if dividendo < divisor:
        return 0
    else:
        return 1 + div(dividendo - divisor, divisor)
    
print(div(20, 2))