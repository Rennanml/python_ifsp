import os
def quantidade_linhas():
    contador = 0
    texto = "aoidsjapsdjaspdjaspdjapskdjasdkjasdkjaaoidsjapsdjaspdjaspdjapskdjasdkjasdkjaaoidsjapsdjaspdjaspdjapskdjasdkjasdkjaaoidsjapsdjaspdjaspdjapskdjasdkjasdkjaaoidsjapsdjaspdjaspdjapskdjasdkjasdkjaaoidsjapsdjaspdjaspdjapskdjasdkjasdkjaaoidsjapsdjaspdjaspdjapskdjasdkjasdkjaaoidsjapsdjaspdjaspdjapskdjasdk\njasdkjaaoidsjapsdjaspdjaspdjapskdjasdkjasdkjaaoidsjapsdjaspdjaspdjapskdjasdkjasdkjaaoidsjapsdjaspdjaspdjapskdjasdkjasdkja das das3er"
    if len(texto):
        ref_arq = open("./1113/exercicio1.txt", 'w')
        for char in texto:
            if char == "\n":
                contador += 1
        ref_arq.write(f"{contador}")
        ref_arq.close()
quantidade_linhas()

def ler_arquivo():
    ref_arq = open("./1113/exercicio1.txt")
    resultado = ref_arq.readline()
    return f"Nesse texto há {resultado} linha(s)."

print(ler_arquivo())