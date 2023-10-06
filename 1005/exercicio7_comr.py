def inverter_nmr(nmr):
    if nmr == 0:
        return
    else:
        print(nmr % 10)
        return inverter_nmr(nmr // 10)
    
print(inverter_nmr(123))