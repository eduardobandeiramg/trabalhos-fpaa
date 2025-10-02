# Arquivo com as funções de suporte ao código principal

## Função que "anda" para o próximo nó:
def andeParaONo(no: int, listaNos: list, nosVisitados: list, listaCaminhos: list, caminhosPercorridos: list):
    nosVisitados.append(no)
    print(f"Entrando no nó {no}")
    print(f"Nós visitados: {nosVisitados}")
    if set(listaNos) == set(nosVisitados):
        print(f"Problema resolvido! Caminhos percorridos: \n${caminhosPercorridos}")
        return caminhosPercorridos
    else:
        caminhosAPartirDoNodoAtual = [caminho for caminho in listaCaminhos if no in caminho]
        print(f"caminhos a partir do atual: {caminhosAPartirDoNodoAtual}")
        ## Criar condição para acessar penultimo elemento
        caminhosAPartirDoNodoAtualSemPassarPorNodosJaVisitados = [caminho for caminho in caminhosAPartirDoNodoAtual if all(no not in nosVisitados[len(nosVisitados)-2] for no in caminho)]
        print(f"Caminhos possíveis: {caminhosAPartirDoNodoAtualSemPassarPorNodosJaVisitados}")
        for i in range(len(caminhosAPartirDoNodoAtualSemPassarPorNodosJaVisitados)):
            if caminhosPercorridos:
                caminhosPercorridos.pop()
            proximoCaminho = caminhosAPartirDoNodoAtualSemPassarPorNodosJaVisitados.pop()
            print(f"Seguindo caminho {proximoCaminho}")
            caminhosPercorridos.append(proximoCaminho)
            return andeParaONo(proximoCaminho[0] if proximoCaminho[1] == no else proximoCaminho[1], listaNos, nosVisitados,listaCaminhos, caminhosPercorridos)