def Real(n):
    numeros = '1234567890'
    dot_counter = 0
    for i in n:
        if i == ".":
            dot_counter += 1
    if dot_counter > 1:
        return False
    if n[0] == "-":
        for i in n[1:]:
            if i not in numeros and i != ".":
                return False
        return True
    for i in n:
        if i not in numeros and i != '.':
            return False
    return True
                    
                    
print(Real("-123.3"))