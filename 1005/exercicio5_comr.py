def nmr_string(string):
    if len(string) == 0:
        return 0
    else:
        return 1 + nmr_string(string[1:])
    
print(nmr_string("Rennan"))