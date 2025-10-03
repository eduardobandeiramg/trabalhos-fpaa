def karatsuba(numero1, numero2):
    numero1 = str(numero1)
    numero2 = str(numero2)
    if len(numero1) < 4 and len(numero2) < 4:
        return int(numero1) * int(numero2)
    else:
        # Dividindo os números ao meio:
        maiorTamanho = max(len(numero1), len(numero2))
        metade = int(maiorTamanho/2)
        numero1 = int(numero1)
        numero2 = int(numero2)
        a = int(numero1//(10 ** metade))
        b = int(numero1%(10 ** metade))
        ##
        c = int(numero2//(10 ** metade))
        d = int(numero2%(10 ** metade))

        # Passo 1: calculando a x c:
        ac = karatsuba(a,c)

        # Passo 2: calculando b x d:
        bd = karatsuba(b,d)

        # Passo 3: ad + bc:
        adbc = karatsuba(a+b, c+d) - ac - bd

        # Passo 4: obtendo o resultado final
        expoente1 = int(maiorTamanho/2) * 2
        expoente2 = int(maiorTamanho/2)
        resultado = (ac * 10**expoente1) + (adbc * 10**expoente2) + bd
        return resultado





numero1 = input("Digite o primeiro número da multiplicação: ")
numero2 = input("Digite o segundo número da multiplicação: ")

resultado = karatsuba(numero1, numero2)
print(f"Resultado: \n{resultado}")
print(f"Para comparar: \n{int(numero1) * int(numero2)}")
