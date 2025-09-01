import random

def maxMinSelect(lista):
    listaTuplas = []
    if len(lista) == 2:
        if(lista[0] < lista[1]):
            return (lista[0], lista[1])
        else:
            return (lista[1], lista[0])
    elif len(lista) == 1:
        return (lista[0], lista[0])
    else:
        meio = len(lista)//2
        menorMaior1 = maxMinSelect(lista[0:meio])
        listaTuplas.append(menorMaior1)
        menorMaior2 = maxMinSelect(lista[meio:])
        listaTuplas.append(menorMaior2)

        listaMenores = []
        listaMaiores = []
        for i in listaTuplas:
            listaMenores.append(i[0])
            listaMaiores.append(i[1])
        
        return (maxMinSelect(listaMenores)[0], maxMinSelect(listaMaiores)[1]) 
        
        #return (min(listaMenores), max(listaMaiores))
    


listaAleatoria = [random.randint(1, 1000000) for _ in range(1000)]
resultado = maxMinSelect(listaAleatoria)
print(f"Resultado: {resultado}")
print(f"Mínimo para conferência: {min(listaAleatoria)}")
print(f"Máximo para conferência: {max(listaAleatoria)}")
