# Mission Control AI é um projeto desenvolvido em Python que simula o monitoramento em tempo real de uma missão espacial. O sistema analisa a telemetria de diferentes sistemas críticos da espaçonave ao longo de múltiplos ciclos de operação, prevendo riscos e emitindo alertas de segurança. 

Projeto 
O sistema processa uma base de dados simulada contendo informações de cada ciclo da missão espacial. A cada atualização, o programa avalia cinco parâmetros fundamentais:
 Temperatura interna (Monitoramento térmico) 
Comunicação com a base (Integridade do sinal) Bateria (Níveis de energia) Oxigênio (Suporte à vida)
 Estabilidade operacional (Sistemas mecânicos e de navegação)
Com base nesses indicadores, a IA calcula o nível de risco atual, gera alertas preventivos/críticos e classifica o status geral da missão. 


 Funcionalidades 
-Leitura Estruturada: Organização e processamento dos dados de telemetria <br>
- Análise Individual: Avaliação detalhada ciclo por ciclo. <br>
-Classificação de Risco: Identificação automática dos estados Estável, Atenção ou Crítico. <br>
-Alertas por Sistema: Mensagens customizadas para cada tipo de falha detectada. -Cálculo de Pontuação: Score de risco dinâmico para quantificar a gravidade dos problemas. <br>
-Análise de Tendência: Diagnóstico comparativo para saber se a missão está melhorando ou piorando. <br>
-Mapeamento de Danos: Identificação exata da área mais afetada ao longo do percurso. <br>
-Relatório Final: Dashboard completo impresso diretamente no terminal <br>

---

 Estrutura do Projeto<br>
 
 mission-control-ai/ <br>
├── README.md <br>
└── mission_control.py <br> 




Como Executar 
Pré-requisitos -  Certifique-se de ter o Python 3.x instalado em sua máquina.
 1. **Clone ou baixe** os arquivos deste repositório.
2. **Abra o terminal** ou prompt de comando na pasta do projeto.
3. **Execute o arquivo** principal com o comando:
   ```bash
   python mission_control.py
   ```

Dados da Missão Avaliada 
Nome da Missão: Alpha Saturno <br>
Equipe de Controle: 101 <br>
6 Ciclos Analisados<br>

---

Observação Tecnológica 

Este projeto foi desenvolvido exclusivamente como um exercício prático de lógica de programação. O objetivo principal foi consolidar conhecimentos em estruturas condicionais avançadas (if/elif/else), loops de repetição (while/for), modularização com funções, escopo de variáveis e manipulação de coleções de dados nativas do Python.

