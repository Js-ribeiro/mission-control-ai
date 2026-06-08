

dados_missao = [
    [24, 92, 88, 96, 90],  
    [27, 80, 72, 94, 85],  
    [31, 65, 58, 91, 70],  
    [36, 42, 38, 87, 55],  
    [39, 28, 19, 78, 35],  
    [34, 55, 32, 82, 50]   
]

areas_monitoradas = [
    "Temperatura",
    "Comunicação",
    "Bateria",
    "Oxigênio",
    "Estabilidade"
]


temperatura = [coluna[0] for coluna in dados_missao]
comunicacao = [coluna[1] for coluna in dados_missao]
bateria = [coluna[2] for coluna in dados_missao]
oxigenio = [coluna[3] for coluna in dados_missao]
estabilidade = [coluna[4] for coluna in dados_missao]

aux = 0
ciclos = {}
ciclo1 = ()


def funcao():

    global aux, ciclo1

    ciclo1 = (
        temperatura[aux],
        comunicacao[aux],
        bateria[aux],
        oxigenio[aux],
        estabilidade[aux]
    )

    return ciclo1


valor_de_validacao = 6


def validacao():

    global aux, valor_de_validacao

    while valor_de_validacao > 0:

        dados_va = funcao()

        nome_do_ciclo = f"ciclo{aux + 1}"

        ciclos[nome_do_ciclo] = dados_va

        aux += 1

        valor_de_validacao -= 1


validacao()


temperatura_c1, comunicacao_c1, bateria_c1, oxigenio_c1, estabilidade_c1 = ciclos["ciclo1"]
temperatura_c2, comunicacao_c2, bateria_c2, oxigenio_c2, estabilidade_c2 = ciclos["ciclo2"]
temperatura_c3, comunicacao_c3, bateria_c3, oxigenio_c3, estabilidade_c3 = ciclos["ciclo3"]
temperatura_c4, comunicacao_c4, bateria_c4, oxigenio_c4, estabilidade_c4 = ciclos["ciclo4"]
temperatura_c5, comunicacao_c5, bateria_c5, oxigenio_c5, estabilidade_c5 = ciclos["ciclo5"]
temperatura_c6, comunicacao_c6, bateria_c6, oxigenio_c6, estabilidade_c6 = ciclos["ciclo6"]

ciclo_atual = 0
temperatura_at = 0
comunicacao_at = 0
bateria_at = 0
oxigenio_at = 0
estabilidade_at = 0

contabilidade_do_ciclo = 0
contabilidade_do_temp = 0
contabilidade_do_comu = 0
contabilidade_do_bate = 0
contabilidade_do_oxi = 0
contabilidade_do_esta = 0

ultima_lista = []

letras_alerta = []
letras_criticas = []


def media():

    media_temperatura = sum(temperatura) / descart
    media_comunicacao = sum(comunicacao) / descart
    media_bateria = sum(bateria) / descart
    media_oxigenio = sum(oxigenio) / descart
    media_estabilidade = sum(estabilidade) / descart

    print(f"Média temperatura: {media_temperatura:.2f}°C ")
    print(f"Média comunicacao: {media_comunicacao:.2f}%")
    print(f"Média bateria: {media_bateria:.2f}%")
    print(f"Média oxigenio: {media_oxigenio}%")
    print(f"Média estabilidade: {media_estabilidade:.2f}%")


def introducao():

    print("Missao : Alpha saturno")
    print("Equipe: 101")
    print(f"Quantidade de ciclos analisados {descart}")


maior = []
critic = ""
listaa = []
valor_T = []
valor_C = []
valor_b = []
valor_o = []
valor_e = []
checagem = []

temporario = ciclo_atual
conta = ciclo_atual
critico = ""
alerta = ""

descart = 6

print(50 * "==")
print("Missao AI Controle")
print(50 * "==")

introducao()

print()
print()


def classificacao_de_ciclos():

    global ciclo_atual
    global temperatura_at
    global comunicacao_at
    global bateria_at
    global oxigenio_at
    global estabilidade_at
    global variavel
    global contabilidade_do_temp
    global contabilidade_do_comu
    global contabilidade_do_bate
    global contabilidade_do_oxi
    global contabilidade_do_esta
    global estado
    global temporario
    global contabilidade_do_ciclo
    global conta
    global checagem
    global letras_alerta
    global letras_criticas
    global descart
    global critic

    descart = 0

    while descart < 6:

        lista = []

        ciclo_atual = f"ciclo{descart + 1}"

        print(f"\033[1m" + (ciclo_atual.upper()) + "\033[0m")

        temperatura_at = f"temperatura_c{descart + 1}"

        temperatura_at = eval(temperatura_at)

       

        if temperatura_at < 18:

            contabilidade_do_ciclo += 1
            estado = ("Temperatura elevada")
            variavel = ("ATENÇÃO")

        elif temperatura_at > 18 and temperatura_at < 31:

            estado = ("Temperatura estável")
            variavel = ("Normal")

        elif temperatura_at > 30 and temperatura_at < 36:

            contabilidade_do_ciclo += 1
            estado = ("Temperatura elevada")
            variavel = ("ATENÇÃO")

        else:

            estado = ("Risco de superaquecimento")
            contabilidade_do_ciclo += 2
            variavel = ("CRÍTICO")
            critic = variavel

        bloco = "a"

        contabilidade_do_temp = contabilidade_do_ciclo

        print(f"{temperatura_at}°C | {variavel} | {estado}")

        def simples():

            if variavel == "CRÍTICO":

                letras_criticas.append(bloco)

            elif variavel == "ATENÇÃO":

                letras_alerta.append(bloco)

        valor_T.append([contabilidade_do_temp])

        simples()

        print()


        comunicacao_at = f"comunicacao_c{descart + 1}"

        comunicacao_at = eval(comunicacao_at)

        if comunicacao_at < 30:

            contabilidade_do_ciclo += 2
            estado = ("Comunicação com a base em nível crítico")
            variavel = ("CRÍTICO")
            critic = variavel

        elif comunicacao_at > 29 and comunicacao_at < 60:

            contabilidade_do_ciclo += 1
            estado = ("Comunicação instável")
            variavel = ("ATENÇÃO")

        else:

            estado = ("Comunicação Normal")
            variavel = ("Normal ")

        contabilidade_do_comu = contabilidade_do_ciclo - contabilidade_do_temp

        print(f"{comunicacao_at} % | {variavel} | {estado}")

        valor_C.append([contabilidade_do_comu])

        bloco = "b"

        simples()

        print()

        bateria_at = f"bateria_c{descart + 1}"

        bateria_at = eval(bateria_at)

        if bateria_at < 20:

            contabilidade_do_ciclo += 2
            estado = ("Bateria em nível crítico")
            variavel = ("CRÍTICO")
            critic = variavel

        elif bateria_at > 19 and bateria_at < 50:

            contabilidade_do_ciclo += 1
            estado = (" Bateria abaixo do recomendado")
            variavel = ("ATENÇÃO")

        else:

            estado = ("Energia estável")
            variavel = ("Normal ")

        contabilidade_do_bate = (
            contabilidade_do_ciclo -
            (contabilidade_do_temp + contabilidade_do_comu)
        )

        print(f"{bateria_at} % | {variavel} | {estado}")

        valor_b.append([contabilidade_do_bate])

        bloco = "c"

        simples()


        print()

        oxigenio_at = f"oxigenio_c{descart + 1}"

        oxigenio_at = eval(oxigenio_at)

        if oxigenio_at < 80:

            contabilidade_do_ciclo += 2
            estado = ("Oxigênio em nível crítico")
            variavel = ("CRÍTICO")
            critic = variavel

        elif oxigenio_at > 79 and oxigenio_at < 90:

            contabilidade_do_ciclo += 1
            estado = (" Oxigênio abaixo do ideal")
            variavel = ("ATENÇÃO")

        else:

            estado = ("Oxigênio adequado")
            variavel = ("Normal ")

        contabilidade_do_oxi = (
            contabilidade_do_ciclo -
            (
                contabilidade_do_temp +
                contabilidade_do_comu +
                contabilidade_do_bate
            )
        )

        print(f"{oxigenio_at} % | {variavel} | {estado}")

        bloco = "d"

        simples()

        valor_o.append([contabilidade_do_oxi])


        print()

        estabilidade_at = f"estabilidade_c{descart + 1}"

        estabilidade_at = eval(estabilidade_at)

        if estabilidade_at < 40:

            contabilidade_do_ciclo += 2
            estado = ("Estabilidade operacional crítica")
            variavel = ("CRÍTICO")
            critic = variavel

        elif estabilidade_at > 39 and estabilidade_at < 70:

            contabilidade_do_ciclo += 1
            estado = (" Estabilidade operacional reduzida")
            variavel = ("ATENÇÃO")

        else:

            estado = ("Estabilidade operacional adequada")
            variavel = ("Normal ")

        contabilidade_do_esta = (
            contabilidade_do_ciclo -
            (
                contabilidade_do_temp +
                contabilidade_do_comu +
                contabilidade_do_bate +
                contabilidade_do_oxi
            )
        )

        print(f"{estabilidade_at} % | {variavel} | {estado}")

        bloco = "e"

        simples()

        valor_e.append([contabilidade_do_esta])

        print(f"Pontucao do ciclo {contabilidade_do_ciclo}")

        conta = contabilidade_do_ciclo

        if conta >= 3 and conta <= 5:

            print("MISSÃO EM ATENÇÃO")

            if descart == 0 or descart == 5:

                ultima_lista.append("Atencao")

        elif conta >= 6 and conta <= 10:

            print("MISSÃO CRÍTICA")

            if descart == 0 or descart == 5:

                ultima_lista.append("critico")

        elif conta >= 0 and conta <= 2:

            print("MISSÃO ESTÁVEL")

            if descart == 0 or descart == 5:

                ultima_lista.append("estavel")

        checagem.append([ciclo_atual, conta])

        maior.append({
            "valor": temporario,
            "volta": descart
        })

        if descart == 0:

            temporario = contabilidade_do_ciclo

        print()

        if contabilidade_do_ciclo == temporario:

            print("Tendencia: A missão permaneceu estável em relação ao ciclo anterior")

        elif contabilidade_do_ciclo > temporario:

            print("Tendencia: A missão apresentou tendência de piora em relação ao ciclo anterior")

        elif contabilidade_do_ciclo < temporario:

            print("Tendencia: A missão apresentou tendência de melhora em relação ao ciclo anterior")

        temporario = contabilidade_do_ciclo

        contabilidade_do_ciclo = 0

        MENSAGENS_Alerta = {

            "a": "Temperaturas  diferentes do recomendado , melhor averiguar o problema ",
            "b": "Conexão com problemas , ler protocolo de solucao .",
            "c": "Bateria atingindo niveis suspeitos , melhor preparar a powerbank  .",
            "d": "Oxigênio em  de alerta , ativar processo de monitoramnento constante .",
            "e": "Estabilidade com defeito , risco de possivel colapso "
        }

        MENSAGENS_CRITICAS = {

            "a": "Altas temperaturas identificadas, recomendamos a solução do problema.",
            "b": "Conexão com a comunicação com o risco de cair.",
            "c": "Bateria atingindo niveis criticos .",
            "d": "Oxigênio em nível crítico , priorizar a vida humana .",
            "e": "Estabilidade em declínio , risco iminente de falha "
        }

        if not letras_criticas and not letras_alerta:

            print("Missão em monitoramento, nada de risco reportado.")

        else:

            if letras_criticas:

                for letra in letras_criticas:

                    mensagem = MENSAGENS_CRITICAS.get(
                        letra,
                        f"Sistema {letra} em estado crítico."
                    )

                    print(mensagem)

            if letras_alerta:

                for letra in letras_alerta:

                    mensagem = MENSAGENS_Alerta.get(
                        letra,
                        f"Sistema {letra} em estado crítico."
                    )

                    print(mensagem)

        letras_alerta = []
        letras_criticas = []

        if critic == "CRÍTICO":

            listaa.append(1)

        print(50 * "==")

        print()

        critic = ""

        descart += 1


classificacao_de_ciclos()



print(50 * "==")
print("RELATÓRIO FINAL DA MISSAO ")
print(50 * "==")

introducao()

media()

st = sum(num for sub in valor_T for num in sub)
sc = sum(num for sub in valor_C for num in sub)
sb = sum(num for sub in valor_b for num in sub)
so = sum(num for sub in valor_o for num in sub)
se = sum(num for sub in valor_e for num in sub)

Risco_medio = (st + sc + sb + so + se) / 5

maior_ciclo = max(maior, key=lambda x: x["valor"])

pontucao = {

    "Temperatura interna ": st,
    "comunicacao com a base": sc,
    "Sistema de energia": sb,
    "suporte ao a oxigenio": so,
    "estabiidade operacional": se
}

numero = len(listaa)


def pontuacao():

    print(f"temperatura interna:{st}")
    print(f"comunicacao com a base: {sc}")
    print(f"Sistema de energia :{sb}")
    print(f"suporte ao  oxigenio :{so}")
    print(f"estabilidade operacional :{se}")

    Alta_pontuacao = max(pontucao, key=pontucao.get)

    print(f"Área mais afetada :{Alta_pontuacao} ")


pontuacao()


def ciclos_final():

    print(f"Ciclo com mais critico : {maior_ciclo['volta']}")
    print(f"Maior pontuacao de risco : {maior_ciclo['valor']}")
    print(f"Risco médio  da missao: {Risco_medio}")
    print(f"quantidade de ciclos críticos: {numero}")


ciclos_final()

primeiro_cilco = ultima_lista[0]
segundo_cilco = ultima_lista[1]

if primeiro_cilco == "estavel" and segundo_cilco == "Atencao":

    print("Classificacao da missao: ")

    print()

    print("Missao em atencao ")

    print()

    print("Conclusao")

    print(
        "Atencao tivemos a piora consideravel do andamento da missao , "
        "recomendamos o preparo do plano reserva . "
        "Precisamos que todos os tripulantes estejam de prontidão caso "
        "a situacao venha a piorar ainda mais "
    )

if primeiro_cilco == "estavel" and segundo_cilco == "critico":

    print("Classificacao da missao: ")

    print()

    print("Missao Critica")

    print()

    print("Conclusao")

    print(
        "Missao em estado critico , recomendamos a utilizacao do plano "
        "reserva de forma imediato para preservacao de vidas."
        "Precissamos que todos os tripulantes sigam o protocolo a risca "
        "para que todos consigam sobreviver e realizar suas funcoes "
        "nesse momento "
    )

if (
    (primeiro_cilco == "Atencao" or primeiro_cilco == "critico")
    and segundo_cilco == "estavel"
):

    print("Classificacao da missao: ")

    print()

    print("Missao estabilizada")

    print()

    print("Conclusao")

    print(
        "Missao estabilizada , mesmo assim recomendamos "
        "a verificacao constante da funcoes , podemos prosseguir sem medo , "
        "os sistemas funcioanram como o esperado com as variacoes "
        "permitidas pela aeronava "
    )

print()

print(50 * "==")

