# Caminho Hamiltoniano
O caminho hamiltoniano é um problema conhecido da computação e descrito pelo enunciado clássico do 'caixeiro viajante'.  
Trata-se da tentativa de se determinar aquele caminho no qual passa-se por todos os nós de um grafo apenas uma vez, voltando ao nó de partida.  
Existem diveras abordagens possíveis para se resolver esse problema, tais quais: força bruta, backtracking, ...

## O algoritmo implementado
Para entender o algoritmo, a melhor maneira é pensar sobre a ideia central dele.   
O algoritmo basicamente implementa a lógica de um escoteiro perdido na floresta e que precisa chegar à saída. Para isso, ele anda com um caderninho onde anota cada ponto de referência que já passou e sempre toma uma entre 3 opções de decisão quando chega em cada um desses pontos. Essas opções são:
1. Se percorreu todos os pontos de referência, quer dizer que chegou ao fim. Neste caso, o problema foi resolvido e encerrado. Se não chegou ao fim, então:   
    1.1. Se possui opções de trajeto, seguir para uma delas, riscar das opções do local, seguir o caminho e registrá-lo na trilha percorrida.
    1.2. Se não possui mais opções no ponto de referência que está, voltar pelo caminho que veio e cortá-lo do mapa da trilha.   
Ao seguir esses passos, o escoteiro eventualmente encontrará a saída desejada.

## Como executar o código
1. Clone o repositório
2. Abra o projeto na sua IDE de preferência
3. Crie um ambiente virtual python, executando o seguinte comando no terminal:   
```
python3 -m venv .venv
```
4. Ative o ambiente virtual executando o seguinte comando no terminal:
    No Windows:
    ```
    .\.venv\Scripts\Activate.ps1
    ```
    No Mac ou Linux:
    ```
    source .venv/bin/activate
    ```
5. Instale as dependências:   
```
pip install -r requirements.txt
```
6. Navegue até a pasta que contém o código:   
```
cd 3_caminho_hamiltoniano/code
```
7. Abra o arquivo 'main.py' e execute o código clicando no botão de executar da IDE ou executando o comando    
```
python main.py
```
8. Para interromper o ambiente virtual, execute o comando:
```
deactivate
```