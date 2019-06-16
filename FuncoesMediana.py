def mediana_cantos(posicao_y, posicao_x, imagem, largura, altura):

    lista_niveis = []
    if posicao_y == 0:
        if posicao_x == 0:
            lista_niveis = [imagem[posicao_y, posicao_x], imagem[posicao_y, posicao_x + 1], imagem[posicao_y + 1, posicao_x], imagem[posicao_y + 1, posicao_x + 1]]
        elif posicao_x == largura-1:
            lista_niveis = [imagem[posicao_y, posicao_x - 1], imagem[posicao_y + 1, posicao_x - 1], imagem[posicao_y + 1, posicao_x], imagem[posicao_y, posicao_x]]
    elif posicao_y == altura-1:
        if posicao_x == 0:
            lista_niveis = [imagem[posicao_y, posicao_x], imagem[posicao_y, posicao_x + 1], imagem[posicao_y - 1, posicao_x], imagem[posicao_y - 1, posicao_x + 1]]
        elif posicao_x == largura-1:
            lista_niveis = [imagem[posicao_y, posicao_x - 1], imagem[posicao_y - 1, posicao_x - 1], imagem[posicao_y - 1, posicao_x], imagem[posicao_y, posicao_x]]

    lista_niveis.sort()

    nivel_mediano = (int(lista_niveis[1]) + int(lista_niveis[2])) // 2

    return nivel_mediano


def mediana_arestas(posicao_y, posicao_x, imagem, largura, altura):

    lista_niveis = []
    if posicao_y == 0:
        lista_niveis = [imagem[posicao_y, posicao_x], imagem[posicao_y, posicao_x-1],
                        imagem[posicao_y, posicao_x+1], imagem[posicao_y+1, posicao_x-1]
                        , imagem[posicao_y+1, posicao_x], imagem[posicao_y+1, posicao_x+1]]
    elif posicao_y == altura-1:
        lista_niveis = [imagem[posicao_y, posicao_x], imagem[posicao_y, posicao_x - 1],
                        imagem[posicao_y, posicao_x + 1], imagem[posicao_y - 1, posicao_x - 1]
            , imagem[posicao_y - 1, posicao_x], imagem[posicao_y - 1, posicao_x + 1]]
    elif posicao_x == 0:
        lista_niveis=[imagem[posicao_y, posicao_x], imagem[posicao_y+1, posicao_x],
                        imagem[posicao_y-1, posicao_x], imagem[posicao_y-1, posicao_x+1]
            , imagem[posicao_y, posicao_x+1], imagem[posicao_y+1, posicao_x+1]]
    elif posicao_x == largura-1:
        lista_niveis = [imagem[posicao_y, posicao_x], imagem[posicao_y-1, posicao_x],
                        imagem[posicao_y+1, posicao_x], imagem[posicao_y - 1, posicao_x - 1]
            ,imagem[posicao_y , posicao_x-1], imagem[posicao_y + 1, posicao_x - 1]]

    lista_niveis.sort()

    nivel_mediano = (int(lista_niveis[2]) + int(lista_niveis[3])) // 2

    return nivel_mediano


def mediana_meios(posicao_y, posicao_x, imagem):
    lista_niveis= [imagem[posicao_y, posicao_x], imagem[posicao_y - 1, posicao_x - 1], imagem[posicao_y - 1, posicao_x],
                   imagem[posicao_y - 1, posicao_x + 1], imagem[posicao_y, posicao_x - 1], imagem[posicao_y, posicao_x + 1],
                   imagem[posicao_y + 1, posicao_x - 1], imagem[posicao_y + 1, posicao_x], imagem[posicao_y, posicao_x + 1]]

    lista_niveis.sort()

    nivel_mediano = lista_niveis[4]

    return nivel_mediano
