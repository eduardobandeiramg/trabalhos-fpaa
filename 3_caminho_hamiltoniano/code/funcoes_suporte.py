# Arquivo com as funções de suporte ao código principal
import networkx

## Função que "anda" para o próximo nó:
def andeParaONo(no: int, listaNos: list, nosVisitados: list, listaCaminhos: list, caminhosPercorridos: list):
    print(f"Entrando no nó {no}")
    nosVisitados.append(no)
    if set(listaNos) == set(nosVisitados):
        return nosVisitados
    else:
        caminhosAPartirDoNodoAtual = [caminho for caminho in listaCaminhos if no in caminho]
        if len(nosVisitados) == 1:
            caminhosAPartirDoNodoAtualSemPassarPorNodosJaVisitados = caminhosAPartirDoNodoAtual
        else:
            nosARetirar = nosVisitados[0:len(nosVisitados)-1]
            caminhosAPartirDoNodoAtualSemPassarPorNodosJaVisitados = [caminho for caminho in caminhosAPartirDoNodoAtual if all(nodo not in nosARetirar for nodo in caminho)]
        if caminhosAPartirDoNodoAtualSemPassarPorNodosJaVisitados:
            for i in range(len(caminhosAPartirDoNodoAtualSemPassarPorNodosJaVisitados)):
                proximoCaminho = caminhosAPartirDoNodoAtualSemPassarPorNodosJaVisitados.pop()
                caminhosPercorridos.append(proximoCaminho)
                resultado = andeParaONo(proximoCaminho[0] if proximoCaminho[1] == no else proximoCaminho[1], listaNos, nosVisitados,listaCaminhos, caminhosPercorridos)
                if set(listaNos) <= set(resultado):
                    return resultado
            nosVisitados.pop()
            return nosVisitados
        else:
            nosVisitados.pop()
            return nosVisitados
        
# Implementação da função "caminho hamiltoniano", que vai isolar os nós do grafo, iniciar o percurso por cada um deles chamando o metodo de caminhar e, caso não haja solução, anunciar

def caminhoHamiltoniano(grafo: networkx.classes.graph.Graph):
    listaDeNos = list(grafo.nodes)
    listaDeCaminhos = list(grafo.edges)
    listaDeNosVisitados = []
    listaDeCaminhosPercorridos = []
    for no in listaDeNos:
        nosVisitados = andeParaONo(no, listaDeNos, listaDeNosVisitados, listaDeCaminhos, listaDeCaminhosPercorridos)
        if listaDeNos <= nosVisitados:
            print(f"Problema resolvido! Caminho hamiltoniano: {nosVisitados}")
            return
    print("Não existe um caminho hamiltoniano para esse grafo!")