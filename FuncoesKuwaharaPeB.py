def kuwahara_cantos(y, x, plano, largura, altura):
    if y == 0:
        if x == 0:
            return sum([plano[y, x], plano[y, x + 1], plano[y, x + 2],
                        plano[y + 1, x], plano[y + 1, x + 1], plano[y + 1, x + 2],
                        plano[y + 2, x], plano[y + 2, x + 1], plano[y + 2, x + 2]]) / 9
        elif x == largura - 1:
            return sum([plano[y, x], plano[y, x - 1], plano[y, x - 2],
                        plano[y + 1, x], plano[y + 1, x - 1], plano[y + 1, x - 2],
                        plano[y + 2, x], plano[y + 2, x - 1], plano[y + 2, x - 2]]) / 9

    if y == altura - 1:
        if x == 0:
            return sum([plano[y, x], plano[y, x + 1], plano[y, x + 2],
                        plano[y - 1, x], plano[y - 1, x + 1], plano[y - 1, x + 2],
                        plano[y - 2, x], plano[y - 2, x + 1], plano[y - 2, x + 2]])
        elif x == largura - 1:
            return sum([plano[y, x], plano[y, x - 1], plano[y, x - 2],
                        plano[y - 1, x], plano[y - 1, x - 1], plano[y - 1, x - 2],
                        plano[y - 2, x], plano[y - 2, x - 1], plano[y - 2, x - 2]])


def kuwahara_meioCantos(y, x, plano, largura, altura):
    janela1bgr = []
    janela2bgr = []

    if y == 0:
        if x == 1:

            janela1bgr = [plano[y, x - 1], plano[y, x],
                          plano[y + 1, x - 1], plano[y + 1, x],
                          plano[y + 2, x - 1], plano[y + 2, x]]
            janela2bgr = [plano[y, x], plano[y, x + 1], plano[y, x + 2],
                          plano[y + 1, x], plano[y + 1, x + 1], plano[y + 1, x + 2],
                          plano[y + 2, x], plano[y + 2, x + 1], plano[y + 2, x + 2]]

        elif x == largura - 2:

            janela2bgr = [plano[y, x], plano[y, x - 1], plano[y, x - 2],
                          plano[y + 1, x], plano[y + 1, x - 1], plano[y + 1, x - 2],
                          plano[y + 2, x], plano[y + 2, x - 1], plano[y + 2, x - 2]]
            janela1bgr = [plano[y, x], plano[y, x + 1],
                          plano[y + 1, x], plano[y + 1, x + 1],
                          plano[y + 2, x], plano[y + 2, x + 1]]

    elif y == altura - 1:
        if x == 1:

            janela1bgr = [plano[y, x - 1], plano[y, x],
                          plano[y - 11, x - 1], plano[y - 1, x],
                          plano[y - 2, x - 1], plano[y - 2, x]]
            janela2bgr = [plano[y, x], plano[y, x + 1], plano[y, x + 2],
                          plano[y - 1, x], plano[y - 1, x + 1], plano[y - 1, x + 2],
                          plano[y - 2, x], plano[y - 2, x + 1], plano[y - 2, x + 2]]

        elif x == largura - 2:

            janela2bgr = [plano[y, x], plano[y, x - 1], plano[y, x - 2],
                          plano[y - 1, x], plano[y - 1, x - 1], plano[y - 1, x - 2],
                          plano[y - 2, x], plano[y - 2, x - 1], plano[y - 2, x - 2]]

            janela1bgr = [plano[y, x], plano[y, x + 1],
                          plano[y - 1, x], plano[y - 1, x + 1],
                          plano[y - 2, x], plano[y - 2, x + 1]]

    elif y == 1:
        if x == 0:
            janela1bgr = [plano[y - 1, x], plano[y - 1, x + 1], plano[y - 1, x + 2],
                          plano[y, x], plano[y, x + 1], plano[y, x + 2]]

            janela2bgr = [plano[y, x], plano[y, x + 1], plano[y, x + 2],
                          plano[y + 1, x], plano[y + 1, x + 1], plano[y + 1, x + 2],
                          plano[y + 2, x], plano[y + 2, x + 1], plano[y + 2, x + 2]]
        elif x == largura - 1:
            janela1bgr = [plano[y - 1, x], plano[y - 1, x - 1], plano[y - 1, x - 2],
                          plano[y, x], plano[y, x - 1], plano[y, x - 2]]
            janela2bgr = [plano[y, x], plano[y, x - 1], plano[y, x - 2],
                          plano[y + 1, x], plano[y + 1, x - 1], plano[y + 1, x - 2],
                          plano[y + 2, x], plano[y + 2, x - 1], plano[y + 2, x - 2]]

    elif y == altura - 2:
        if x == 0:
            janela1bgr = [plano[y + 1, x], plano[y + 1, x + 1], plano[y + 1, x + 2],
                          plano[y, x], plano[y, x + 1], plano[y, x + 2]]

            janela2bgr = [plano[y, x], plano[y, x + 1], plano[y, x + 2],
                          plano[y - 1, x], plano[y - 1, x + 1], plano[y - 1, x + 2],
                          plano[y - 2, x], plano[y - 2, x + 1], plano[y - 2, x + 2]]

        elif x == largura - 1:
            janela1bgr = [plano[y + 1, x], plano[y + 1, x - 1], plano[y + 1, x - 2],
                          plano[y, x], plano[y, x - 1], plano[y, x - 2]]

            janela2bgr = [plano[y, x], plano[y, x - 1], plano[y, x - 2],
                          plano[y - 1, x], plano[y - 1, x - 1], plano[y - 1, x - 2],
                          plano[y - 2, x], plano[y - 2, x - 1], plano[y - 2, x - 2]]

    media_janela1 = sum(janela1bgr) / 6
    media_janela2 = sum(janela2bgr) / 9

    soma_dos_quadrados1 = 0
    soma_dos_quadrados2 = 0

    for i in range(6):
        soma_dos_quadrados1 += (media_janela1 - janela1bgr[i]) ** 2

    for j in range(9):
        soma_dos_quadrados2 += (media_janela2 - janela2bgr[j]) ** 2

    variacia_janela1 = soma_dos_quadrados1 / 6
    variacia_janela2 = soma_dos_quadrados2 / 9

    if variacia_janela1 > variacia_janela2:
        return sum(janela2bgr) / 9
    else:
        return sum(janela1bgr) / 6


def kuwahara_cantos_internos(y, x, plano, largura, altura):
    janela1BGR = []
    janela2BGR = []
    janela3BGR = []
    janela4BGR = []
    if y == 1:
        if x == 1:
            janela1BGR = [plano[y, x], plano[y, x - 1],
                          plano[y - 1, x], plano[y - 1, x - 1]]
            janela2BGR = [plano[y, x], plano[y, x + 1], plano[y, x + 2],
                          plano[y - 1, x], plano[y - 1, x + 1], plano[y - 1, x + 2]]
            janela3BGR = [plano[y, x], plano[y, x - 1],
                          plano[y + 1, x], plano[y + 1, x - 1],
                          plano[y + 2, x], plano[y + 2, x - 1]]
            janela4BGR = [plano[y, x], plano[y, x + 1], plano[y, x + 2],
                          plano[y + 1, x], plano[y + 1, x + 1], plano[y + 1, x + 2],
                          plano[y + 2, x], plano[y + 2, x + 1], plano[y + 2, x + 2]]

        elif x == largura - 2:
            janela1BGR = [plano[y, x], plano[y, x + 1],
                          plano[y - 1, x], plano[y - 1, x + 1]]
            janela2BGR = [plano[y, x], plano[y, x - 1], plano[y, x - 2],
                          plano[y - 1, x], plano[y - 11, x - 1], plano[y - 1, x - 2]]
            janela3BGR = [plano[y, x], plano[y, x + 1],
                          plano[y + 1, x], plano[y + 1, x + 1],
                          plano[y + 2, x], plano[y + 2, x + 1]]
            janela4BGR = [plano[y, x], plano[y, x - 1], plano[y, x - 2],
                          plano[y + 1, x], plano[y + 1, x - 1], plano[y + 1, x - 2],
                          plano[y + 2, x], plano[y + 2, x - 1], plano[y + 2, x - 2]]

    if y == altura - 2:
        if x == 1:
            janela1BGR = [plano[y, x], plano[y, x - 1],
                          plano[y + 1, x], plano[y + 1, x - 1]]
            janela2BGR = [plano[y, x], plano[y, x + 1], plano[y, x + 2],
                          plano[y + 1, x], plano[y + 1, x + 1], plano[y + 1, x + 2]]
            janela3BGR = [plano[y, x], plano[y, x - 1],
                          plano[y - 1, x], plano[y - 1, x - 1],
                          plano[y - 2, x], plano[y - 2, x - 1]]
            janela4BGR = [plano[y, x], plano[y, x + 1], plano[y, x + 2],
                          plano[y - 1, x], plano[y - 1, x + 1], plano[y - 1, x + 2],
                          plano[y - 2, x], plano[y - 2, x + 1], plano[y - 2, x + 2]]

        elif x == largura - 2:
            janela1BGR = [plano[y, x], plano[y, x + 1],
                          plano[y + 1, x], plano[y + 1, x + 1]]
            janela2BGR = [plano[y, x], plano[y, x - 1], plano[y, x - 2],
                          plano[y + 1, x], plano[y + 1, x - 1], plano[y + 1, x - 2]]
            janela3BGR = [plano[y, x], plano[y, x + 1],
                          plano[y - 1, x], plano[y - 1, x + 1],
                          plano[y - 2, x], plano[y - 2, x + 1]]
            janela4BGR = [plano[y, x], plano[y, x - 1], plano[y, x - 2],
                          plano[y - 1, x], plano[y - 1, x - 1], plano[y - 1, x - 2],
                          plano[y - 2, x], plano[y - 2, x - 1], plano[y - 2, x - 2]]

    media_janela1 = sum(janela1BGR) / 4
    media_janela2 = sum(janela2BGR) / 6
    media_janela3 = sum(janela3BGR) / 6
    media_janela4 = sum(janela4BGR) / 9

    soma_quadrados1 = 0
    soma_quadrados2 = 0
    soma_quadrados3 = 0
    soma_quadrados4 = 0

    for i in range(4):
        soma_quadrados1 += (media_janela1 - janela1BGR[i]) ** 2
    for j in range(6):
        soma_quadrados2 += (media_janela2 - janela2BGR[j]) ** 2
        soma_quadrados3 += (media_janela3 - janela3BGR[j]) ** 2
    for x in range(9):
        soma_quadrados4 += (media_janela4 - janela4BGR[x]) ** 2

    variancia1 = soma_quadrados1 / 4
    variancia2 = soma_quadrados2 / 6
    variancia3 = soma_quadrados3 / 6
    variancia4 = soma_quadrados4 / 9

    l = [variancia1, variancia2, variancia3, variancia4]

    menor = min(l)
    menor_varianciaa = 0
    for i in range(1, 5):
        if l[i - 1] == menor:
            menor_varianciaa = i
            break

    if menor_varianciaa == 1:
        return sum(janela1BGR) / 4
    elif menor_varianciaa == 2:
        return sum(janela2BGR) / 6
    elif menor_varianciaa == 3:
        return sum(janela3BGR) / 6
    elif menor_varianciaa == 4:
        return sum(janela4BGR) / 9


def kuwahara_arestas_pEb(y, x, plano_BGR, largura, altura):
    janela1 = []
    janela2 = []

    if y == 0:
        janela1 = [plano_BGR[y, x], plano_BGR[y, x - 1], plano_BGR[y, x - 2],
                   plano_BGR[y + 1, x], plano_BGR[y + 1, x - 1], plano_BGR[y + 1, x - 2]]

        janela2 = [plano_BGR[y, x], plano_BGR[y, x + 1], plano_BGR[y, x + 2],
                   plano_BGR[y + 1, x], plano_BGR[y + 1, x + 1], plano_BGR[y + 1, x + 2]]
    elif y == altura - 1:
        janela1 = [plano_BGR[y, x], plano_BGR[y, x - 1], plano_BGR[y, x - 2],
                   plano_BGR[y - 1, x], plano_BGR[y - 1, x - 1], plano_BGR[y - 1, x - 2]]
        janela2 = [plano_BGR[y, x], plano_BGR[y, x + 1], plano_BGR[y, x + 2],
                   plano_BGR[y - 1, x], plano_BGR[y - 1, x + 1], plano_BGR[y - 1, x + 2]]
    elif x == 0:
        janela1 = [plano_BGR[y, x], plano_BGR[y, x + 1],
                   plano_BGR[y - 1, x], plano_BGR[y - 1, x + 1],
                   plano_BGR[y - 2, x], plano_BGR[y - 2, x + 1]]

        janela2 = [plano_BGR[y, x], plano_BGR[y, x + 1],
                   plano_BGR[y + 1, x], plano_BGR[y + 1, x + 1],
                   plano_BGR[y + 2, x], plano_BGR[y + 2, x + 1]]

    elif x == largura - 1:
        janela1 = [plano_BGR[y, x], plano_BGR[y, x - 1],
                   plano_BGR[y - 1, x], plano_BGR[y - 1, x - 1],
                   plano_BGR[y - 2, x], plano_BGR[y - 2, x - 1]]

        janela2 = [plano_BGR[y, x], plano_BGR[y, x - 1],
                   plano_BGR[y + 1, x], plano_BGR[y + 1, x - 1],
                   plano_BGR[y + 2, x], plano_BGR[y + 2, x - 1]]

    media_janela1 = sum(janela1) / 6
    media_janela2 = sum(janela2) / 6

    soma_dos_quadrados1 = 0
    soma_dos_quadrados2 = 0
    for i in range(6):
        soma_dos_quadrados1 += (media_janela1 - janela1[i]) ** 2
        soma_dos_quadrados2 += (media_janela2 - janela2[i]) ** 2
    variancia1 = soma_dos_quadrados1 / 6
    variancia2 = soma_dos_quadrados2 / 6

    if variancia1 > variancia2:
        return media_janela2
    else:
        return media_janela1


def kuwahara_arestaS_internas(y, x, plano_brilho, largura, altura):
    janela1 = []
    janela2 = []
    janela3 = []
    janela4 = []
    if y == 1:

        janela1 = [plano_brilho[y - 1, x - 2], plano_brilho[y - 1, x - 1], plano_brilho[y - 1, x],
                   plano_brilho[y, x - 2], plano_brilho[y, x - 1], plano_brilho[y, x]]
        janela2 = [plano_brilho[y - 1, x], plano_brilho[y - 1, x + 1], plano_brilho[y - 1, x + 2],
                   plano_brilho[y, x], plano_brilho[y, x + 1], plano_brilho[y, x + 2]]
        janela3 = [plano_brilho[y, x - 2], plano_brilho[y, x - 1], plano_brilho[y, x],
                   plano_brilho[y + 1, x - 2], plano_brilho[y + 1, x - 1], plano_brilho[y + 1, x],
                   plano_brilho[y + 2, x - 2], plano_brilho[y + 2, x - 1], plano_brilho[y + 2, x]]
        janela4 = [plano_brilho[y, x], plano_brilho[y, x + 1], plano_brilho[y, x + 2],
                   plano_brilho[y + 1, x], plano_brilho[y + 1, x + 1], plano_brilho[y + 1, x + 2],
                   plano_brilho[y + 2, x], plano_brilho[y + 2, x + 1], plano_brilho[y + 2, x + 2]]

    elif y == altura - 2:

        janela1 = [plano_brilho[y + 1, x - 2], plano_brilho[y + 1, x - 1], plano_brilho[y + 1, x],
                   plano_brilho[y, x - 2], plano_brilho[y, x - 1], plano_brilho[y, x]]
        janela2 = [plano_brilho[y + 1, x], plano_brilho[y + 1, x + 1], plano_brilho[y + 1, x + 2],
                   plano_brilho[y, x], plano_brilho[y, x + 1], plano_brilho[y, x + 2]]
        janela3 = [plano_brilho[y, x - 2], plano_brilho[y, x - 1], plano_brilho[y, x],
                   plano_brilho[y - 1, x - 2], plano_brilho[y - 1, x - 1], plano_brilho[y - 1, x],
                   plano_brilho[y - 2, x - 2], plano_brilho[y - 2, x - 1], plano_brilho[y - 2, x]]
        janela4 = [plano_brilho[y, x], plano_brilho[y, x + 1], plano_brilho[y, x + 2],
                   plano_brilho[y - 1, x], plano_brilho[y - 1, x + 1], plano_brilho[y - 1, x + 2],
                   plano_brilho[y - 2, x], plano_brilho[y - 2, x + 1], plano_brilho[y - 2, x + 2]]

    elif x == 1:

        janela1 = [plano_brilho[y - 2, x - 1], plano_brilho[y - 2, x],
                   plano_brilho[y - 1, x - 1], plano_brilho[y - 1, x],
                   plano_brilho[y, x - 1], plano_brilho[y, x]]
        janela2 = [plano_brilho[y, x - 1], plano_brilho[y, x],
                   plano_brilho[y + 1, x - 1], plano_brilho[y + 1, x],
                   plano_brilho[y + 2, x - 1], plano_brilho[y + 2, x]]
        janela3 = [plano_brilho[y - 2, x], plano_brilho[y - 2, x + 1], plano_brilho[y - 2, x + 2],
                   plano_brilho[y - 1, x], plano_brilho[y - 1, x + 1], plano_brilho[y - 1, x + 2],
                   plano_brilho[y, x], plano_brilho[y, x + 1], plano_brilho[y, x + 2]]
        janela4 = [plano_brilho[y, x], plano_brilho[y, x + 1], plano_brilho[y, x + 2],
                   plano_brilho[y + 1, x], plano_brilho[y + 1, x + 1], plano_brilho[y + 1, x + 2],
                   plano_brilho[y + 2, x], plano_brilho[y + 2, x + 1], plano_brilho[y + 2, x + 2]]

    elif x == largura - 2:
        janela1 = [plano_brilho[y - 2, x + 1], plano_brilho[y - 2, x],
                   plano_brilho[y - 1, x + 1], plano_brilho[y - 1, x],
                   plano_brilho[y, x + 1], plano_brilho[y, x]]
        janela2 = [plano_brilho[y, x + 1], plano_brilho[y, x],
                   plano_brilho[y + 1, x + 1], plano_brilho[y + 1, x],
                   plano_brilho[y + 2, x + 1], plano_brilho[y + 2, x]]
        janela3 = [plano_brilho[y - 2, x], plano_brilho[y - 2, x - 1], plano_brilho[y - 2, x - 2],
                   plano_brilho[y - 1, x], plano_brilho[y - 1, x - 1], plano_brilho[y - 1, x - 2],
                   plano_brilho[y, x], plano_brilho[y, x - 1], plano_brilho[y, x - 2]]
        janela4 = [plano_brilho[y, x], plano_brilho[y, x - 1], plano_brilho[y, x - 2],
                   plano_brilho[y + 1, x], plano_brilho[y + 1, x - 1], plano_brilho[y + 1, x - 2],
                   plano_brilho[y + 2, x], plano_brilho[y + 2, x - 1], plano_brilho[y + 2, x - 2]]

    mediajanela1 = sum(janela1) / 6
    mediajanela2 = sum(janela2) / 6
    mediajanela3 = sum(janela3) / 9
    mediajanela4 = sum(janela4) / 9

    soma_quadrados1 = 0
    soma_quadrados2 = 0
    soma_quadrados3 = 0
    soma_quadrados4 = 0

    for i in range(6):
        soma_quadrados1 += (mediajanela1 - janela1[i]) ** 2
        soma_quadrados2 += (mediajanela2 - janela2[i]) ** 2
    for j in range(9):
        soma_quadrados3 += (mediajanela3 - janela3[j]) ** 2
        soma_quadrados4 += (mediajanela4 - janela4[j]) ** 2

    lista_variancias = [soma_quadrados1 / 6, soma_quadrados2 / 6, soma_quadrados3 / 9, soma_quadrados4 / 9]
    menor = min(lista_variancias)
    janela_menor_variancia = 0
    for i in range(1, 5):
        if lista_variancias[i - 1] == menor:
            janela_menor_variancia = i
            break

    if janela_menor_variancia == 1:
        return mediajanela1
    elif janela_menor_variancia == 2:
        return mediajanela2
    elif janela_menor_variancia == 3:
        return mediajanela3
    elif janela_menor_variancia == 4:
        return mediajanela4


def define_janela_menor_variancia_meios(y, x, planoBGR):
    janela1 = [planoBGR[y - 2, x - 2], planoBGR[y - 2, x - 1], planoBGR[y - 2, x],
               planoBGR[y - 1, x - 2], planoBGR[y - 1, x - 1], planoBGR[y - 1, x],
               planoBGR[y, x - 2], planoBGR[y, x - 1], planoBGR[y, x]]

    janela2 = [planoBGR[y - 2, x], planoBGR[y - 2, x + 1], planoBGR[y - 2, x + 2],
               planoBGR[y - 1, x], planoBGR[y - 1, x + 1], planoBGR[y - 1, x + 2],
               planoBGR[y, x], planoBGR[y, x + 1], planoBGR[y, x + 2]]

    janela3 = [planoBGR[y, x - 2], planoBGR[y, x - 1], planoBGR[y, x],
               planoBGR[y + 1, x - 2], planoBGR[y + 1, x - 1], planoBGR[y + 1, x],
               planoBGR[y + 2, x - 2], planoBGR[y + 2, x - 1], planoBGR[y + 2, x]]

    janela4 = [planoBGR[y, x], planoBGR[y, x + 1], planoBGR[y, x + 2],
               planoBGR[y + 1, x], planoBGR[y + 1, x + 1], planoBGR[y + 1, x + 2],
               planoBGR[y + 2, x], planoBGR[y + 2, x + 1], planoBGR[y + 2, x + 2]]

    media_janela1 = sum(janela1) / 9
    media_janela2 = sum(janela2) / 9
    media_janela3 = sum(janela3) / 9
    media_janela4 = sum(janela4) / 9

    soma_quadrados1 = 0
    soma_quadrados2 = 0
    soma_quadrados3 = 0
    soma_quadrados4 = 0

    for i in range(9):
        soma_quadrados1 += (media_janela1 - janela1[i]) ** 2
        soma_quadrados2 += (media_janela2 - janela2[i]) ** 2
        soma_quadrados3 += (media_janela3 - janela3[i]) ** 2
        soma_quadrados4 += (media_janela4 - janela4[i]) ** 2

    variancia_janela1 = soma_quadrados1 / 9
    variancia_janela2 = soma_quadrados2 / 9
    variancia_janela3 = soma_quadrados3 / 9
    variancia_janela4 = soma_quadrados4 / 9

    lista_variancia = [variancia_janela1, variancia_janela2, variancia_janela3, variancia_janela4]

    janela_menor_variancia = 0
    menor_variancia = min(lista_variancia)
    for j in range(1, 5):
        if lista_variancia[j - 1] == menor_variancia:
            janela_menor_variancia = j
            break

    if janela_menor_variancia == 1:
        return media_janela1
    elif janela_menor_variancia == 2:
        return media_janela2
    elif janela_menor_variancia == 3:
        return media_janela3
    elif janela_menor_variancia == 4:
        return media_janela4
