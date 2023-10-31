quitanda = {
    "sucos": ("Tampico", "Del-valle", "Prats"),
    "frutas": ("Banana", "uva", "Maçã"),
    "Notebooks": ("acer", "lenovo", "asus", "samsung")
}



quitanda["Higiêne"] = "Papel higiênico", "Pasta dental"



total = ()

# for i in quitanda.values(): ###Printa os conteúdos somados!!
#     total += i
# print(total)

# for j in quitanda.items():  ###Printa as keys + os conteúdos
#     print(j)

ks = list(quitanda.keys())
ks.append("Celulares")
print("lista de frutas", ks)
for k in ks:
    print(k, ": ", quitanda.get(k, "Não tem"))