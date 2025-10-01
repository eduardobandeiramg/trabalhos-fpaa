# Caminho Hamiltoniano
O caminho hamiltoniano é um problema conhecido da computação e descrito pelo enunciado clássico do 'caixeiro viajante'.  
Trata-se da tentativa de se determinar aquele caminho no qual passa-se por todos os nós de um grafo apenas uma vez, voltando ao nó de partida.  
Existem diveras abordagens possíveis para se resolver esse problema, tais quais: força bruta, backtracking, ...



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