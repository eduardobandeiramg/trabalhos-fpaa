# Arquivo com as funções de suporte ao código principal


## Função que verifica se todos os nós já foram percorridos (problema resolvido):
def percorreuTodosOsNos(listaNos, caminhosPercorridos):
    nosPercorridos = set().union(*map(set, caminhosPercorridos))
    return set(listaNos) <= set(nosPercorridos)

## Função que "anda" para o próximo nó:
def andeParaONo(no: int, listaCaminhos: list, listaNos: list, caminhosPercorridos: list):
    if percorreuTodosOsNos(listaNos, caminhosPercorridos):
        print(f"Problema resolvido! Caminhos percorridos: \n${caminhosPercorridos}")
        return caminhosPercorridos
    else:
        caminhosPossiveis = [caminho for caminho in listaCaminhos if no in caminho]
        if not caminhosPossiveis:
            caminhosPercorridos.pop()
            return
        else:
            proximoCaminho = caminhosPossiveis.pop()
            caminhosPercorridos.append(proximoCaminho)
            andeParaONo(proximoCaminho[0] if proximoCaminho[1] == no else proximoCaminho[1])