# Algoritmo de seleção simultânea do maior e menor elementos
Como o próprio nome sugere, esse algoritmo tem como objetivo buscar o menor e o maior valor de uma lista de números. Ele se caracteriza como um algoritmo clássico de divisão e conquista, onde a lista é subdividida em listas menores até que se chegue ao ponto de ser necessário apenas uma comparação simples de valores (**linha 4 e linha 9**). Esse ponto acontece quando a lista analisada tem tamanho 1 ou 2.   
Trata-se de um algoritmo recursivo, onde a parada ocorre quando a lista tem tamanho 1 ou 2 (**linhas 6, 8 ou 10**). Quando essa condição não é verdadeira, é feita uma chamada sobre a partição esquerda (**linha 13**) e então direita (**linha 14**) da lista. Quando os valores provenientes da comparação simples são retornados para a chamada acima na pilha (**linha 18**), é então avaliado esses valores para o lado direito (**linha 14**). Então, avalia-se o menor e maior valor também por comparação simples entre os dois valores obtidos como mínimos e os dois valores obtidos como máximos (**linhas 16 e 17**). O resultado é retornado para a chamada acima até que a última comparação seja entre as tuplas de mínimo/máximo da partição esquerda e direita da lista original. Então, faz-se a comparação dos mínimos e máximos (**linhas 16 e 17**), retornando o resultado final.

## Análise da complexidade assintótica pelo método de contagem de operações
### Comparações em cada etapa do algoritmo
* 1ª etapa do algoritmo: lista tem tamanho 1 ou 2.   
Nesta etapa é feita **uma comparação** para se determinar e então retornar a **tupla do valor mínimo e máximo**, nesta ordem.
* 2ª etapa do algoritmo: lista tem tamanho maior que 2.  
Nesta etapa chama-se a função sobre a parte esquerda da lista. Caso essa parte entre na 1ª parte do algoritmo e retorne a tupla de mínimo e máximo, o valor é armazenado e então chama-se a função para a parte direita. De forma análoga, o valor da tupla de mínimo e máximo também é armazenada caso a chamada entre na mesma condição. Então, é feita a comparação para se determinar o **menor valor dentre os dois valores mínimos** e o **maior valor dentre os dois valores máximos**. Ou seja, na segunda parte são feitas **duas comparações**.    
Resumidamente, é feita **1 comparação na primeira parte do algoritmo** e **2 comparações na segunda parte do algoritmo**.

### Total de comparações para n elementos
As comparações para os casos em que se cai na primeira etapa do algoritmo acontecem um número igual a n/2 vezes. 
Para os casos que caem na segunda parte do algoritmo, as 2 comparações realizadas acontecem um número de vezes que vai aumentando a cada chamada, dobrando a cada divisão. Essas 2 comparações serão chamadas 1 vez ao início, então 2 vezes, depois 4, depois 8, depois 16 e assim sucessivamente. Observa-se um padrão de somatório onde sempre soma-se o dobro do valor anterior, começando do 1. 
Assim, tem-se a seguinte função:

$\sum_{i=0}^{{\log_{2} n} - 1} i^2$    

A função acima descreve o número de partições maiores que 2 que o algoritmo irá avaliar. Cada uma dessas partições realiza duas comparações. Então, multiplica-se esse valor por 2 e depois soma-se ao número de partições menores ou iguais a 2 do algoritmo (n/2). Ao final tem-se a seguinte função:

$2 comparações \times(\sum_{i=0}^{{\log_{2} n} - 1} i^2) + \frac{n}{2} comparações$    

Entende-se, portanto, que trata-se de uma função de complexidade igual a O(n).

## Análise da complexidade assintótica pela aplicação do teorema mestre
O teorema mestre é dado pela fórmula:    
$T(n) = a \times T \dot (\frac{n}{b}) + f(n)$

O teorema define a ordem de complexidade de um algoritmo recursivo avaliando qual das duas funções domina:    
f(n) ou $n^{\log_{b} a}$    
Caso sejam equivalentes, a solução será igual a $n^{\log_{b} a} \times x$, sendo x um fator logarítmico.    

Considerando a recorrência do MaxMinSelect como sendo:    
$T(n) = 2 \dot T (\frac{n}{b}) + O(2)$     
1. Os valores de a, b e f(n) são, respectivamente:
    * 2
    * 2
    * O(1)
2. $\log_{b} a = \log_{2} 2 = 1$
3. Como $O(n^{\log_{b} a}) = O(n)$ domina assintoticamente $O(1)$, este algoritmo se encaixa no *caso 1*
4. A solução assintótica da fórmula é dada por: $T(n) = \Theta(n)$

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
cd 2_max_min_select/code
```
7. Abra o arquivo 'main.py' e execute o código clicando no botão de executar da IDE ou executando o comando    
```
python main.py
```
8. Para interromper o ambiente virtual, execute o comando:
```
deactivate
```