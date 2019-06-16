def separa_niveis_por_listas(lista_de_cores=[], lista_separada=[]):
    pos = 0
    for i, v in enumerate(lista_de_cores):
        if i == 0:
            lista_separada.append([])
            lista_separada[pos].append(v)
        else:
            if lista_de_cores[i] == lista_de_cores[i - 1]:
                lista_separada[pos].append(v)
            else:
                if lista_de_cores[i] != lista_de_cores[i - 1]:
                    lista_separada.append([])
                    pos += 1
                    lista_separada[pos].append(lista_de_cores[i])
    return lista_separada


def gera_termosY(lista_de_niveis_separados =[], lista_com_niveis_contados=[]):

    pos = 0
    for i in range(256):
        if lista_de_niveis_separados[pos][0] == i:
            lista_com_niveis_contados.append(len(lista_de_niveis_separados[pos]))
            pos += 1
        else:
            lista_com_niveis_contados.append(0)

    return lista_com_niveis_contados


def gera_termos_x(lista_de_niveis_que_fazem_parte_da_imagem=[]):
    for i in range(256):
        lista_de_niveis_que_fazem_parte_da_imagem.append(i)

    return lista_de_niveis_que_fazem_parte_da_imagem
