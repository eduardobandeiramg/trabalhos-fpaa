# Flood Fill
Como o próprio nome sugere, o algoritmo Flood Fill busca analisar as áreas que seriam "inundadas" caso se jogasse um líquido dentro das partes "livres" do labirinto, neste caso representadas pelos algarismos "0" da matriz. As barreiras ou muros são representadas pelo algarismo "1".

## Funcionamento do algoritmo
O algoritmo funciona da seguinte forma:
1. A matriz é percorrida, buscando pela primeira área livre, representada pelo algarismo "0".
2. Quando essa área é encontrada, inicia-se, a partir dela, uma busca recursiva por todos os pontos adjacentes dentro da área delimitada pelos limites da matriz e pelos pontos cujos algarismos é igual a "1". Uma vez que todas as opções são exauridas, significa que a "piscina" existente desde o primeiro ponto foi completamente alagada.
3. Então, continua-se percorrendo a matriz, até o final, buscando por pontos dentro de outras "piscinas", que ainda não foram descobertas.
4. Ao final, é retornada uma lista de listas, cada uma representando uma "piscina" diferente.
5. O algoritmo principal recebe a lista de piscinas e, então, substitui os valores dos elementos de cada uma delas
6. Por fim, é gerada uma imagem com colorações diferentes para cada algarismo.

## Como executar o código
