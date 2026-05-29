Mission Control AI
Projeto desenvolvido em Python para simular o monitoramento de uma missão espacial, analisando o estado de diferentes sistemas da nave ao longo de vários ciclos.

Sobre o projeto
O sistema trabalha com uma base de dados contendo informações de cada ciclo da missão. A cada ciclo, são avaliados cinco parâmetros principais:

Temperatura interna

Comunicação com a base

Bateria

Oxigênio

Estabilidade operacional

Com base nesses dados, o programa identifica possíveis riscos, gera alertas e classifica o estado geral da missão.

Funcionalidades
Leitura e organização dos dados da missão

Análise de cada ciclo individualmente

Classificação de risco (estável, atenção ou crítico)

Geração de alertas por sistema

Cálculo de pontuação de risco por ciclo

Análise de tendência da missão (melhora ou piora)

Identificação da área mais afetada

Relatório final no terminal

Estrutura do projeto
mission-control-ai
 │
 <br>
 ├── README.md
 <br>
 └── mission_control.py
 <br>
Como executar
Ter o Python instalado

Rodar o arquivo principal:

python mission_control.py

Informações da missão
Nome da missão: Alpha Saturno

Equipe: 101

Ciclos analisados: 6

Observação
O projeto foi feito como exercício de lógica de programação, focando em estruturas condicionais, repetição, funções e manipulação de dados.
