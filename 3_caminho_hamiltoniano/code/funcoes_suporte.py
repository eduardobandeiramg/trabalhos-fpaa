# Arquivo com as funções de suporte ao código principal
import networkx

## Função que "anda" para o próximo nó:
def andeParaONo(no: int, listaNos: list, nosVisitados: list, listaCaminhos: list, caminhosPercorridos: list):
    print(f"Entrando no nó {no}")
    nosVisitados.append(no)
    #print(f"Nós visitados: {nosVisitados}")
    if set(listaNos) == set(nosVisitados):
        print(f"Problema resolvido! Caminho dos nós visitados: \n{nosVisitados}")
        return nosVisitados #caminhosPercorridos
    else:
        caminhosAPartirDoNodoAtual = [caminho for caminho in listaCaminhos if no in caminho]
        #print(f"caminhos a partir do atual: {caminhosAPartirDoNodoAtual}")
        ## Criar condição para acessar penultimo elemento
        if len(nosVisitados) == 1:
            caminhosAPartirDoNodoAtualSemPassarPorNodosJaVisitados = caminhosAPartirDoNodoAtual
        else:
            nosARetirar = nosVisitados[0:len(nosVisitados)-1]
            caminhosAPartirDoNodoAtualSemPassarPorNodosJaVisitados = [caminho for caminho in caminhosAPartirDoNodoAtual if all(nodo not in nosARetirar for nodo in caminho)]
        #print(f"Caminhos possíveis: {caminhosAPartirDoNodoAtualSemPassarPorNodosJaVisitados}")
        if caminhosAPartirDoNodoAtualSemPassarPorNodosJaVisitados:
            for i in range(len(caminhosAPartirDoNodoAtualSemPassarPorNodosJaVisitados)):
                proximoCaminho = caminhosAPartirDoNodoAtualSemPassarPorNodosJaVisitados.pop()
                #print(f"Seguindo caminho {proximoCaminho}")
                caminhosPercorridos.append(proximoCaminho)
                andeParaONo(proximoCaminho[0] if proximoCaminho[1] == no else proximoCaminho[1], listaNos, nosVisitados,listaCaminhos, caminhosPercorridos)
            nosVisitados.pop()
            return nosVisitados
        else:
            nosVisitados.pop()
            return nosVisitados
        
# Implementação da função "caminho hamiltoniano", que vai isolar os nós do grafo, iniciar o percurso por cada um deles chamando o metodo de caminhar e, caso não haja solução, anunciar

def caminhoHamiltoniano(grafo: networkx.classes.graph.Graph):
    listaDeNos = list(grafo.nodes)
    listaDeCaminhos = list(grafo.edges)
    print(f"TODOS OS CAMINHOS: {listaDeCaminhos}")
    listaDeNosVisitados = []
    listaDeCaminhosPercorridos = []
    for no in listaDeNos:
        nosVisitados = andeParaONo(no, listaDeNos, listaDeNosVisitados, listaDeCaminhos, listaDeCaminhosPercorridos)
        print(f"CAMINHOS RETORNADOS: {nosVisitados}")
        if listaDeNos <= nosVisitados:
            #print(f"Problema resolvido! \nCaminho percorrido: {nosVisitados}")
            return
    print("Não existe um caminho hamiltoniano para esse grafo!")