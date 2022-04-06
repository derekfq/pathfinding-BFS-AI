# Pathfinding BFS AI
![GitHub Repository Size](https://img.shields.io/github/repo-size/h-ssiqueira/pathfinding-BFS-AI?label=Repository%20Size&style=for-the-badge)

![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![MAC](https://img.shields.io/badge/MAC-000000?style=for-the-badge&logo=macos&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

![VSCode](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

## Descrição

Este projeto consiste em um sistema de navegação automática de um robô utilizando o algoritmo de busca em largura.

A região de busca é determinada por um arquivo de entrada (.csv), contendo as posições de partida, de destino e um mapa 42x42.

A movimentação da busca é realizada somente na vertical e horizontal, seguindo o padrão norte, leste, sul e oeste (N->L->S->O), assim como na figura abaixo, em que a cor verde representa o ponto de partida, a cor lilás representa o destino, as células amarelas representam as posições por onde o algoritmo percorreu, as em bege representam as células presentes na fila, sendo elas as próximas a serem executadas.

![FuncionamentoDoAlgoritmo](imgs/algoritmo.jpg)

## Mapas

Tipo | Cor | Valor (CSV) | Custo
:---: | :---: | :---: | :---:
Sólido e plano | Verde | 1 | 1
Montanhoso | Marrom | 2 | 5
Pântano | Azul | 3 | 10
Fogo | Vermelho | 4 | 15

### Mapa 1
![Exemplo1](/imgs/mapa1.jpg)

### Mapa 2
![Exemplo2](/imgs/mapa2.JPG)

### Mapa 3
![Exemplo3](/imgs/mapa3.JPG)

### Mapa 4
![Exemplo4](/imgs/mapa4.JPG)

## Resultados

Para calcular o custo total, o programa realiza a soma de custos de toda a trajetória, ou seja, o custo do início, os custos pertencentes à trajetória do caminho encontrado pelo algoritmo e também o custo da posição final.

## Exemplo de execução
![funcionamento](imgs/funcionamento.png)

Com custo 12. 