import random

def maxMinSelect(lista):
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
        menorMaior2 = maxMinSelect(lista[meio:])

        menor_final = min(menorMaior1[0], menorMaior2[0])
        maior_final = max(menorMaior1[1], menorMaior2[1])
        return (menor_final, maior_final)
    


listaAleatoria = [random.randint(1, 1000000) for _ in range(1000)]
resultado = maxMinSelect(listaAleatoria)
print(f"Resultado: {resultado}")
print(f"Mínimo para conferência: {min(listaAleatoria)}")
print(f"Máximo para conferência: {max(listaAleatoria)}")
