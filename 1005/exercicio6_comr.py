def vertical(string):
    if len(string) == 1:
        print(string)
    else: 
        print(string[:1])
        return "\n" + vertical(string[1:])
print(vertical("rennan"))