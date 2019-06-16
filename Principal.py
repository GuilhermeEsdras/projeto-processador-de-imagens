print("\033[91m Carregando...\n \033[0m---")

# ===[ Bibliotecas & Funções ]::.
import os
# ===[ Adicionais do Sistema ]::.
import math
import time
from random import randint

# ===[ Tkinter para Interface Gráfica ]::.
from tkinter import *
from tkinter import messagebox as tkmb
from tkinter import filedialog as tkfd
from tkinter import ttk

# ===[ OpenCV e Numpy para as Imagens e Filtros ]::.
import cv2
import numpy as np

# ===[ Matplotlib.pyplot para Gráficos ]::.
from matplotlib import pyplot as plt

# ===[ Funções (Coração) dos Filtros ]::.
import FuncoesHistograma as fh
import FuncoesHistogramaPeB as fhpb
import FuncoesKuwahara as fk
import FuncoesKuwaharaPeB as fkpb
import FuncoesMediana as fm
import FuncoesPSNR as fp
import FuncoesVerificaPeB as fvpb


# ===[ Atalho para Cores e Estilos de Texto ]::.
class TColor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# =========================[ Saudação ]::.
print(TColor.OKBLUE + "Seja Bem Vindo!\n" + TColor.BOLD + " ┕ Navegue pela janela acima." + TColor.ENDC)

# =========================[ Início ]::.
janela = Tk()

# =========================[ Parâmetros/Medidas da janela ]::.
janela.title("Processador de Imagens")
janela.iconbitmap(r'favicon.ico')
janela.resizable(0, 0)
largura_janela = 300
altura_janela = 325
x = (janela.winfo_screenwidth() // 2) - (largura_janela // 2)
y = (janela.winfo_screenheight() // 2) - (altura_janela // 2)
janela.geometry("{}x{}+{}+{}".format(largura_janela, altura_janela, x, y))

# =========================[ Barra de Menu ]::.
menubar = Menu(janela)
janela.config(menu=menubar)

# =========================[ Menu Arquivo, Caminhos (Paths) e Dados das Imagens ]::.
caminho_1 = None  # Caminho (path) da imagem 1.
caminho_2 = None  # Caminho (path) da imagem 2.
local_imagem_1 = None  # Local onde a imagem 1 está salva.
local_imagem_2 = None  # Local onde a imagem 2 está salva.
pixels_imagem_1 = 0  # Quantidade de Pixels total da imagem 1.
pixels_imagem_2 = 0  # Quantidade de Pixels total da imagem 2.
nome_da_imagem_1 = None  # Nome do arquivo da imagem 1.
nome_da_imagem_2 = None  # Nome do arquivo da imagem 2.
ext_da_imagem_1 = None  # Extensão ou formato da imagem 1.
ext_da_imagem_2 = None  # Extensão ou formato da imagem 2.
cont_img1 = 0  # Informa se a é a primeira vez que a imagem 1 está sendo selecionada.
cont_img2 = 0  # Informa se a é a primeira vez que a imagem 2 está sendo selecionada.
preto_e_branco1 = False  # Valor booleano que informa se a imagem 1 é preto-e-branco (monocromática) ou colorida.
preto_e_branco2 = False  # Valor booleano que informa se a imagem 2 é preto-e-branco (monocromática) ou colorida.


def AbrirImagem1():  # Função executada ao clicar no botão "Abrir Imagem 1" no menu.
    global caminho_1, local_imagem_1, pixels_imagem_1, nome_da_imagem_1, ext_da_imagem_1, cont_img1, preto_e_branco1

    preto_e_branco1 = False

    get_caminho_1 = tkfd.askopenfilename(initialdir="C:/Users/~/Documents",
                                         filetypes=(("Imagem", "*.jpg *.png"), ("All Files", "*.*")),
                                         title="Selecione a Imagem 1")

    if len(get_caminho_1) > 0:  # Certifica-se de que o usuário selecionou uma imagem sem fechar a janela antes.


        caminho_1 = get_caminho_1
        local_imagem_1 = os.path.dirname(os.path.realpath(caminho_1))
        nome_da_imagem_1 = os.path.splitext(os.path.basename(caminho_1))[0]
        ext_da_imagem_1 = os.path.splitext(os.path.basename(caminho_1))[1]
        cont_img1 += 1

        try:

            # ======= [ Verifica se a imagem é preto-e-branco (monocromática) ou colorida.
            img1 = cv2.imread(caminho_1)

            altura, largura = img1.shape[0], img1.shape[1]

            pixels_imagem_1 = altura * largura

            conta_vezes_True = 0

            for i in range(500):
                bb = fvpb.eh_pEb(img1[randint(0, altura - 1), randint(0, largura - 1)])

                if bb:
                    conta_vezes_True += 1

            if conta_vezes_True == 500:
                preto_e_branco1 = True

            # =======

            if cont_img1 == 1:  # Verifica se é a primeira vez que o usuário seleciona a Imagem 1.
                if preto_e_branco1:
                    print("---\nImagem 1 carregada!")
                    print(" ├ Nome: {}".format(nome_da_imagem_1))
                    print(" ├ Local: {}".format(local_imagem_1))
                    print(" ├ Extensão/formato: {}".format(ext_da_imagem_1))
                    print(" ├ Possui: {} pixels de largura por {} pixels de altura.".format(largura, altura))
                    print(" ┕ É preto-e-branco (ou monocromática).")

                elif not preto_e_branco1:
                    print("---\nImagem 1 carregada!")
                    print(" ├ Nome: {}".format(nome_da_imagem_1))
                    print(" ├ Local: {}".format(local_imagem_1))
                    print(" ├ Extensão/formato: {}".format(ext_da_imagem_1))
                    print(" ├ Possui: {} pixels de largura por {} pixels de altura.".format(largura, altura))
                    print(" ┕ É colorida.")

            else:
                if preto_e_branco1:
                    print("---\nNova Imagem 1 carregada!")
                    print(" ├ Nome: {}".format(nome_da_imagem_1))
                    print(" ├ Local: {}".format(local_imagem_1))
                    print(" ├ Extensão/formato: {}".format(ext_da_imagem_1))
                    print(" ├ Possui: {} pixels de largura por {} pixels de altura.".format(largura, altura))
                    print(" ┕ É preto-e-branco (ou monocromática).")

                elif not preto_e_branco1:
                    print("---\nNova Imagem 1 carregada!")
                    print(" ├ Nome: {}".format(nome_da_imagem_1))
                    print(" ├ Local: {}".format(local_imagem_1))
                    print(" ├ Extensão/formato: {}".format(ext_da_imagem_1))
                    print(" ├ Possui: {} pixels de largura por {} pixels de altura.".format(largura, altura))
                    print(" ┕ É colorida.")

            # Verifica se a imagem 2 já foi carregada e define a mensagem do StatusBar.
            if caminho_2 is None:
                statusBar['text'] = "Imagem 1 selecionada..."
            else:
                statusBar['text'] = "Imagens 1 e 2 selecionadas."

        except AttributeError:
            tkmb.showinfo("Erro ao abrir arquivo!", "Você selecionou um arquivo estranho. "
                                                    "As funções podem não funcionar corretamente.\n"
                                                    "Selecione apenas imagens .jpg ou .png.")

    else:
        print("---\nNenhuma imagem selecionada.")


def AbrirImagem2():  # Função executada ao clicar no botão "Abrir Imagem 2" no menu.
    global caminho_2, local_imagem_2, pixels_imagem_2, nome_da_imagem_2, ext_da_imagem_2, cont_img2, preto_e_branco2

    get_caminho_2 = tkfd.askopenfilename(initialdir="C:/Users/~/Documents",
                                         filetypes=(("Imagem", "*.jpg *.png"), ("All Files", "*.*")),
                                         title="Selecione a Imagem 2")

    if len(get_caminho_2) > 0:  # Certifica-se de que o usuário selecionou uma imagem sem fechar a janela antes.

        caminho_2 = get_caminho_2
        local_imagem_2 = os.path.dirname(os.path.realpath(caminho_2))
        nome_da_imagem_2 = os.path.splitext(os.path.basename(caminho_2))[0]
        ext_da_imagem_2 = os.path.splitext(os.path.basename(caminho_2))[1]
        cont_img2 += 1

        try:

            # ======= [ Verifica se a imagem é preto-e-branco (monocromática) ou colorida.
            img2 = cv2.imread(caminho_2)

            altura, largura = img2.shape[0], img2.shape[1]

            pixels_imagem_2 = altura * largura

            conta_vezes_True = 0

            for i in range(500):
                bb = fvpb.eh_pEb(img2[randint(0, altura - 1), randint(0, largura - 1)])

                if bb:
                    conta_vezes_True += 1

            if conta_vezes_True == 500:
                preto_e_branco2 = True

            # =======

            if cont_img2 == 1:  # Verifica se é a primeira vez que o usuário seleciona a Imagem 2.
                if preto_e_branco2:
                    print("---\nImagem 2 carregada!")
                    print(" ├ Nome: {}".format(nome_da_imagem_2))
                    print(" ├ Local: {}".format(local_imagem_2))
                    print(" ├ Extensão/formato: {}".format(ext_da_imagem_2))
                    print(" ├ Possui: {} pixels de largura por {} pixels de altura.".format(largura, altura))
                    print(" ┕ É preto-e-branco (ou monocromática).")

                elif not preto_e_branco2:
                    print("---\nImagem 2 carregada!")
                    print(" ├ Nome: {}".format(nome_da_imagem_2))
                    print(" ├ Local: {}".format(local_imagem_2))
                    print(" ├ Extensão/formato: {}".format(ext_da_imagem_2))
                    print(" ├ Possui: {} pixels de largura por {} pixels de altura.".format(largura, altura))
                    print(" ┕ É colorida.")

            else:
                if preto_e_branco2:
                    print("---\nNova Imagem 2 carregada!")
                    print(" ├ Nome: {}".format(nome_da_imagem_2))
                    print(" ├ Local: {}".format(local_imagem_2))
                    print(" ├ Extensão/formato: {}".format(ext_da_imagem_2))
                    print(" ├ Possui: {} pixels de largura por {} pixels de altura.".format(largura, altura))
                    print(" ┕ É preto-e-branco (ou monocromática).")

                elif not preto_e_branco2:
                    print("---\nNova Imagem 2 carregada!")
                    print(" ├ Nome: {}".format(nome_da_imagem_2))
                    print(" ├ Local: {}".format(local_imagem_2))
                    print(" ├ Extensão/formato: {}".format(ext_da_imagem_2))
                    print(" ├ Possui: {} pixels de largura por {} pixels de altura.".format(largura, altura))
                    print(" ┕ É colorida.")

            # Verifica se a imagem 1 já foi carregada.
            if caminho_1 is None:
                statusBar['text'] = "Apenas Imagem 2 selecionada!"
            else:
                statusBar['text'] = "Imagens 1 e 2 selecionadas."

        except AttributeError:
            tkmb.showinfo("Erro ao abrir arquivo!", "Você selecionou um arquivo estranho. "
                                                    "As funções podem não funcionar corretamente.\n"
                                                    "Selecione apenas imagens .jpg ou .png.")

    else:
        print("---\nNenhuma imagem selecionada.")


def Sair():  # Função executada ao clicar em um dos botões "Sair".
    statusBar['text'] = "Até logo... :)"
    janela.after(1000, lambda: janela.destroy())


fileMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Arquivo", menu=fileMenu)
fileMenu.add_command(label="Abrir Imagem 1", command=AbrirImagem1)
fileMenu.add_command(label="Abrir Imagem 2", command=AbrirImagem2)
fileMenu.add_separator()
fileMenu.add_command(label="Sair", command=Sair)


# =========================[ Menu Ajuda ]::.
def Ajuda():  # Função executada ao clicar no botão "Exibir Ajuda" no menu.
    popup = tkfd.Tk()
    popup.wm_title("Ajuda...")
    popup.iconbitmap(r'favicon.ico')

    label = ttk.Label(popup, text="-----\nDescrição:\n-----\n"

                                  "Para usar alguma das funções deste processador certifique-se de selecionar pelo"
                                  " menos a primeira imagem.\n"

                                  "Clique em:\n -> Arquivo\n -> Abrir Imagem 1\n -> Selecione a Imagem\n"
                                  "Repita o processo clicando em -> Abrir Imagem 2 para poder calcular o PSNR entre as"
                                  " duas.\n"
                                  "---\n"

                                  "Filtro da Mediana: Filtro da mediana é uma transformação usada para suavizar ruído"
                                  " do tipo impulsivo em imagens digitais.\n"
                                  "-\n"
                                  
                                  "Filtro Kuwahara: É um filtro de suavização não linear que age sobre as imagens, "
                                  "sem comprometer sua nitidez e as posições das bordas.\n"
                                  "-\n"
                                  
                                  "Gráfico do Histograma: Um histograma é um gráfico de frequência que tem por"
                                  " objetivo ilustrar como a quantidade de cores da imagem está distribuída. \n"
                                  "-\n"
                                  
                                  "Cálculo do PSNR: Relação Sinal-Ruído de Pico")
    label.pack()

    botao_sair_ajuda = ttk.Button(popup, text="Ok", command=popup.destroy)
    botao_sair_ajuda.pack(side="bottom")

    popup.mainloop()


def Sobre():  # Função executada ao clicar no botão "Sobre este Projeto" no menu.
    tkmb.showinfo("Sobre...", "Este Processador de Imagens é um Projeto de Algoritmos e Programação"
                              " do Primeiro Semestre do Curso de Engenharia de Computação do IFPB/CG.\n"
                              "Feito pelos alunos:\n"
                              "© João Edinaldo\n"
                              "© Guilherme Esdras\n"
                              "Com a orientação do Professor:\n"
                              "© Henrique Cunha")


helpMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Ajuda", menu=helpMenu)
helpMenu.add_command(label="Exibir Ajuda", command=Ajuda)
helpMenu.add_separator()
helpMenu.add_command(label="Sobre este Projeto", command=Sobre)

# =========================[ Tela Principal ]::.
titulo = Label(janela, text="Seja Bem Vindo!", font="Helvetica 18 bold italic")
titulo.pack(side="top", fill="x", pady=10)

texto = Label(janela, text="Após selecionar sua imagem,\n navegue pelos botões abaixo:")
texto.pack(side="top", fill="x", pady=10)


# =========================[ Ver Imagem 1 ]::.
def VerImagem1():  # Função executada ao clicar no botão "Ver Imagem 1".
    if caminho_1 is None:
        tkmb.showinfo("Sem imagem!", "Certifique-se de que pelo menos a Imagem 1 foi devidamente selecionada.")

    else:

        try:
            imagem_1 = cv2.imread(caminho_1)
            cv2.imshow('Imagem 1 Original', imagem_1)
            cv2.waitKey(1)

        except cv2.error:
            tkmb.showinfo("Erro ao abrir arquivo!", "Você selecionou um arquivo estranho. \n"
                                                    "Selecione apenas imagens .jpg ou .png.")


# =========================[ Filtro da Mediana ]::.
def Mediana():  # Função executada ao clicar no botão "Aplicar Filtro da Mediana".
    global nome_da_imagem_1, local_imagem_1

    if caminho_1 is None:
        tkmb.showinfo("Sem imagem!", "Certifique-se de que pelo menos a Imagem 1 foi devidamente selecionada.")

    else:

        try:

            roedera = cv2.imread(caminho_1)

            num_canais = roedera.shape
            altura, largura = roedera.shape[0], roedera.shape[1]
            lista_niveis = []
            b = roedera[:, :, 0]
            g = roedera[:, :, 1]
            r = roedera[:, :, 2]

            for l in range(altura):
                for c in range(largura):
                    cor = roedera[l, c]

                    if l == 0:
                        if c == 0:
                            roedera[l, c, 0] = fm.mediana_cantos(l, c, b, largura, altura)
                            roedera[l, c, 1] = fm.mediana_cantos(l, c, g, largura, altura)
                            roedera[l, c, 2] = fm.mediana_cantos(l, c, r, largura, altura)
                        elif c == largura - 1:
                            roedera[l, c, 0] = fm.mediana_cantos(l, c, b, largura, altura)
                            roedera[l, c, 1] = fm.mediana_cantos(l, c, g, largura, altura)
                            roedera[l, c, 2] = fm.mediana_cantos(l, c, r, largura, altura)
                        else:
                            roedera[l, c, 0] = fm.mediana_arestas(l, c, b, largura, altura)
                            roedera[l, c, 1] = fm.mediana_arestas(l, c, g, largura, altura)
                            roedera[l, c, 2] = fm.mediana_arestas(l, c, r, largura, altura)

                    elif l == altura - 1:
                        if c == 0:
                            roedera[l, c, 0] = fm.mediana_cantos(l, c, b, largura, altura)
                            roedera[l, c, 1] = fm.mediana_cantos(l, c, g, largura, altura)
                            roedera[l, c, 2] = fm.mediana_cantos(l, c, r, largura, altura)
                        elif c == largura - 1:
                            roedera[l, c, 0] = fm.mediana_cantos(l, c, b, largura, altura)
                            roedera[l, c, 1] = fm.mediana_cantos(l, c, g, largura, altura)
                            roedera[l, c, 2] = fm.mediana_cantos(l, c, r, largura, altura)
                        else:
                            roedera[l, c, 0] = fm.mediana_arestas(l, c, b, largura, altura)
                            roedera[l, c, 1] = fm.mediana_arestas(l, c, g, largura, altura)
                            roedera[l, c, 2] = fm.mediana_arestas(l, c, r, largura, altura)

                    elif c == 0 and l != 0 and l != altura:
                        roedera[l, c, 0] = fm.mediana_arestas(l, c, b, largura, altura)
                        roedera[l, c, 1] = fm.mediana_arestas(l, c, g, largura, altura)
                        roedera[l, c, 2] = fm.mediana_arestas(l, c, r, largura, altura)

                    elif c == largura - 1 and l != 0 and l != altura:
                        roedera[l, c, 0] = fm.mediana_arestas(l, c, b, largura, altura)
                        roedera[l, c, 1] = fm.mediana_arestas(l, c, g, largura, altura)
                        roedera[l, c, 2] = fm.mediana_arestas(l, c, r, largura, altura)

                    else:
                        roedera[l, c, 0] = fm.mediana_meios(l, c, b)
                        roedera[l, c, 1] = fm.mediana_meios(l, c, g)
                        roedera[l, c, 2] = fm.mediana_meios(l, c, r)

            print("---\nFiltro da Mediana aplicado na Imagem 1.")

            cv2.imshow("{} com Filtro da Mediana".format(nome_da_imagem_1), roedera)
            cv2.waitKey(1)

            salvar = tkmb.askyesno("Salvar imagem com Filtro da Mediana", "Você deseja salvar esta modificação?")
            if salvar:
                cv2.imwrite(os.path.join(local_imagem_1, '{} com filtro da Mediana.jpg'.format(nome_da_imagem_1)), roedera)
                print("---\nNova Imagem 1 salva em: {}".format(local_imagem_1))
                print(" Com o nome: {} com Filtro da Mediana.jpg".format(nome_da_imagem_1))

        except AttributeError:
            tkmb.showinfo("Erro ao abrir arquivo!", "Você selecionou um arquivo estranho.\n"
                                                    "Selecione apenas imagens .jpg ou .png.")


# =========================[ Filtro Kuwahara ]::.
def Kuwahara():  # Função executada ao clicar no botão "Aplicar Filtro Kuwahara".
    global nome_da_imagem_1, local_imagem_1, pixels_imagem_1

    if caminho_1 is None:  # Verifica se o usuário já selecionou uma Imagem 1.
        tkmb.showinfo("Sem imagem!", "Certifique-se de que pelo menos a Imagem 1 foi devidamente selecionada.")

    else:

        try:

            if preto_e_branco1:  # Verifica se a Imagem 1 é preto-e-branco (ou monocromática).

                imagem = cv2.imread(caminho_1)

                gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)

                altura, largura = imagem.shape[0], imagem.shape[1]

                cont = 0

                for l in range(altura):
                    for c in range(largura):
                        if l == 0 or l == altura - 1:
                            if c == 0 or c == largura - 1:
                                imagem[l, c] = fkpb.kuwahara_cantos(l, c, gray, largura, altura)
                                cont += 1
                                print("Aplicando filtro. Aguarde... [{:.0f}%]".format((cont * 100) / pixels_imagem_1))

                            elif c == 1 or c == largura - 2:
                                imagem[l, c] = fkpb.kuwahara_meioCantos(l, c, gray, largura, altura)
                                cont += 1
                                print("Aplicando filtro. Aguarde... [{:.0f}%]".format((cont * 100) / pixels_imagem_1))

                            else:
                                imagem[l, c] = fkpb.kuwahara_arestas_pEb(l, c, gray, largura, altura)
                                cont += 1
                                print("Aplicando filtro. Aguarde... [{:.0f}%]".format((cont * 100) / pixels_imagem_1))

                        if c == 0 and (l != 0 and l != altura - 1):
                            if l == 1 or l == altura - 2:
                                imagem[l, c, 0] = fkpb.kuwahara_meioCantos(l, c, gray, largura, altura)
                                cont += 1
                                print("Aplicando filtro. Aguarde... [{:.0f}%]".format((cont * 100) / pixels_imagem_1))

                            else:
                                imagem[l, c] = fkpb.kuwahara_arestas_pEb(l, c, gray, largura, altura)
                                cont += 1
                                print("Aplicando filtro. Aguarde... [{:.0f}%]".format((cont * 100) / pixels_imagem_1))

                        elif c == largura - 1 and (l != 0 and l != altura - 1):
                            if l == 1 or l == altura - 2:
                                imagem[l, c] = fkpb.kuwahara_meioCantos(l, c, gray, largura, altura)
                                cont += 1
                                print("Aplicando filtro. Aguarde... [{:.0f}%]".format((cont * 100) / pixels_imagem_1))

                            else:
                                menor_variancia = fkpb.kuwahara_arestas_pEb(l, c, gray, largura, altura)
                                cont += 1
                                print("Aplicando filtro. Aguarde... [{:.0f}%]".format((cont * 100) / pixels_imagem_1))

                        if l == 1:
                            if c == 1 or c == largura - 2:
                                imagem[l, c] = fkpb.kuwahara_cantos_internos(l, c, gray, largura, altura)
                                cont += 1
                                print("Aplicando filtro. Aguarde... [{:.0f}%]".format((cont * 100) / pixels_imagem_1))

                            elif c != 0 and c != largura - 1 and c != 1 and c != largura - 2:
                                imagem[l, c] = fkpb.kuwahara_arestaS_internas(l, c, gray, largura, altura)
                                cont += 1
                                print("Aplicando filtro. Aguarde... [{:.0f}%]".format((cont * 100) / pixels_imagem_1))

                        elif l == altura - 2:
                            if c == 1 or c == largura - 2:
                                imagem[l, c] = fkpb.kuwahara_cantos_internos(l, c, gray, largura, altura)
                                cont += 1
                                print("Aplicando filtro. Aguarde... [{:.0f}%]".format((cont * 100) / pixels_imagem_1))

                            elif c != 0 and c != largura - 1 and c != 1 and c != largura - 2:
                                imagem[l, c] = fkpb.kuwahara_arestaS_internas(l, c, gray, largura, altura)
                                cont += 1
                                print("Aplicando filtro. Aguarde... [{:.0f}%]".format((cont * 100) / pixels_imagem_1))

                        if c == 1:
                            if l != 0 and l != 1 and l != altura - 2 and l != altura - 1:
                                imagem[l, c] = fkpb.kuwahara_arestaS_internas(l, c, gray, largura, altura)
                                cont += 1
                                print("Aplicando filtro. Aguarde... [{:.0f}%]".format((cont * 100) / pixels_imagem_1))

                        if c == largura - 2:
                            if l != 0 and l != 1 and l != altura - 2 and l != altura - 1:
                                imagem[l, c] = fkpb.kuwahara_arestaS_internas(l, c, gray, largura, altura)
                                cont += 1
                                print("Aplicando filtro. Aguarde... [{:.0f}%]".format((cont * 100) / pixels_imagem_1))

                        if l != 0 and l != 1 and l != altura - 2 and l != altura - 1:
                            if c != 0 and c != 1 and c != largura - 2 and c != largura - 1:
                                imagem[l, c] = fkpb.define_janela_menor_variancia_meios(l, c, gray)
                                cont += 1
                                print("Aplicando filtro. Aguarde... [{:.0f}%]".format((cont * 100) / pixels_imagem_1))

                print("---\nFiltro Kuwahara aplicado na Imagem 1.")
                cv2.imshow("{} com Filtro Kuwahara".format(nome_da_imagem_1), imagem)

                salvar = tkmb.askyesno("Salvar imagem com Filtro Kuwahara", "Você deseja salvar esta modificação?")
                if salvar:
                    cv2.imwrite(os.path.join(local_imagem_1, '{} com Filtro Kuwahara.jpg'.format(nome_da_imagem_1)),
                                imagem)
                    print("---\nNova Imagem 1 salva em: {}".format(local_imagem_1))
                    print(" Com o nome: {} com Filtro Kuwahara.jpg".format(nome_da_imagem_1))

                '''
                # Fail!!!
                # Esse método faz travar a imagem exibida.
                
                while True:
                    salvar = input("---\nVocê deseja salvar este resultado como uma nova imagem? [S/N]").upper()[0]
    
                    if salvar in 'SN':
                        if salvar == 'S':
                            cv2.imwrite(os.path.join(local_imagem_1, '{} com Filtro Kuwahara.jpg'.format(nome_da_imagem_1)),
                                        imagem)
                            print("---\nUma Nova Imagem 1 foi salva com Filtro Kuwahara aplicado.")
                            break
                        else:
                            print("---\nOk")
                            break
                    else:
                        print("Por favor, responda apenas com Sim ou Não!")
                '''

            else:

                imagem = cv2.imread(caminho_1)

                hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)

                altura, largura = imagem.shape[0], imagem.shape[1]

                value = hsv[:, :, 2]
                b = imagem[:, :, 0]
                g = imagem[:, :, 1]
                r = imagem[:, :, 2]

                cont = 0

                for l in range(altura):
                    for c in range(largura):
                        if l == 0 or l == altura - 1:
                            if c == 0 or c == largura - 1:
                                imagem[l, c, 0] = fk.kuwahara_cantos(l, c, b, largura, altura)
                                imagem[l, c, 1] = fk.kuwahara_cantos(l, c, g, largura, altura)
                                imagem[l, c, 2] = fk.kuwahara_cantos(l, c, r, largura, altura)

                            elif c == 1 or c == largura - 2:
                                imagem[l, c, 0] = fk.kuwahara_meioCantos(l, c, value, b, largura, altura)
                                imagem[l, c, 1] = fk.kuwahara_meioCantos(l, c, value, g, largura, altura)
                                imagem[l, c, 2] = fk.kuwahara_meioCantos(l, c, value, r, largura, altura)

                            else:
                                menor_variancia = fk.define_janela_arestas(l, c, value, largura, altura)

                                if l == 0:
                                    if menor_variancia == 1:
                                        imagem[l, c, 0] = sum([b[l, c], b[l, c - 1], b[l, c - 2],
                                                               b[l + 1, c], b[l + 1, c - 1], b[l + 1, c - 2]]) / 6
                                        imagem[l, c, 1] = sum([g[l, c], g[l, c - 1], g[l, c - 2],
                                                               g[l + 1, c], g[l + 1, c - 1], g[l + 1, c - 2]]) / 6
                                        imagem[l, c, 2] = sum([r[l, c], r[l, c - 1], r[l, c - 2],
                                                               r[l + 1, c], r[l + 1, c - 1], r[l + 1, c - 2]]) / 6
                                    elif menor_variancia == 2:
                                        imagem[l, c, 0] = sum([b[l, c], b[l, c - 1], b[l, c - 2],
                                                               b[l + 1, c], b[l + 1, c - 1], b[l + 1, c - 2]]) / 6
                                        imagem[l, c, 1] = sum([g[l, c], g[l, c - 1], g[l, c - 2],
                                                               g[l + 1, c], g[l + 1, c - 1], g[l + 1, c - 2]]) / 6
                                        imagem[l, c, 2] = sum([r[l, c], r[l, c - 1], r[l, c - 2],
                                                               r[l + 1, c], r[l + 1, c - 1], r[l + 1, c - 2]]) / 6

                                elif l == altura - 1:
                                    if menor_variancia == 1:
                                        imagem[l, c, 0] = sum([b[l, c], b[l, c - 1], b[l, c - 2],
                                                               b[l - 1, c], b[l - 1, c - 1], b[l - 1, c - 2]]) / 6
                                        imagem[l, c, 1] = sum([g[l, c], g[l, c - 1], g[l, c - 2],
                                                               g[l - 1, c], g[l - 1, c - 1], g[l - 1, c - 2]]) / 6
                                        imagem[l, c, 2] = sum([r[l, c], r[l, c - 1], r[l, c - 2],
                                                               r[l - 1, c], r[l - 1, c - 1], r[l - 1, c - 2]]) / 6
                                    elif menor_variancia == 2:
                                        imagem[l, c, 0] = sum([b[l, c], b[l, c + 1], b[l, c + 2],
                                                               b[l - 1, c], b[l - 1, c + 1], b[l - 1, c + 2]]) / 6
                                        imagem[l, c, 1] = sum([g[l, c], g[l, c + 1], g[l, c + 2],
                                                               g[l - 1, c], g[l - 1, c + 1], g[l - 1, c + 2]]) / 6
                                        imagem[l, c, 2] = sum([r[l, c], r[l, c + 1], r[l, c + 2],
                                                               r[l - 1, c], r[l - 1, c + 1], r[l - 1, c + 2]]) / 6

                        if c == 0 and (l != 0 and l != altura - 1):
                            if l == 1 or l == altura - 2:
                                imagem[l, c, 0] = fk.kuwahara_meioCantos(l, c, value, b, largura, altura)
                                imagem[l, c, 1] = fk.kuwahara_meioCantos(l, c, value, g, largura, altura)
                                imagem[l, c, 2] = fk.kuwahara_meioCantos(l, c, value, r, largura, altura)

                            else:
                                menor_variancia = fk.define_janela_arestas(l, c, value, largura, altura)

                                if menor_variancia == 1:
                                    imagem[l, c, 0] = sum([b[l, c], b[l, c + 1],
                                                           b[l - 1, c], b[l - 1, c + 1],
                                                           b[l - 2, c], b[l - 2, c + 1]]) / 6
                                    imagem[l, c, 1] = sum([g[l, c], g[l, c + 1],
                                                           g[l - 1, c], g[l - 1, c + 1],
                                                           g[l - 2, c], g[l - 2, c + 1]]) / 6
                                    imagem[l, c, 2] = sum([r[l, c], r[l, c + 1],
                                                           r[l - 1, c], r[l - 1, c + 1],
                                                           r[l - 2, c], r[l - 2, c + 1]]) / 6

                                elif menor_variancia == 2:
                                    imagem[l, c, 0] = sum([b[l, c], b[l, c + 1],
                                                           b[l + 1, c], b[l - 1, c + 1],
                                                           b[l + 2, c], b[l - 2, c + 1]]) / 6
                                    imagem[l, c, 1] = sum([g[l, c], g[l, c + 1],
                                                           g[l + 1, c], g[l - 1, c + 1],
                                                           g[l + 2, c], g[l - 2, c + 1]]) / 6
                                    imagem[l, c, 2] = sum([r[l, c], r[l, c + 1],
                                                           r[l + 1, c], r[l - 1, c + 1],
                                                           r[l + 2, c], r[l - 2, c + 1]]) / 6

                        elif c == largura - 1 and (l != 0 and l != altura - 1):
                            if l == 1 or l == altura - 2:
                                imagem[l, c, 0] = fk.kuwahara_meioCantos(l, c, value, b, largura, altura)
                                imagem[l, c, 1] = fk.kuwahara_meioCantos(l, c, value, g, largura, altura)
                                imagem[l, c, 2] = fk.kuwahara_meioCantos(l, c, value, r, largura, altura)

                            else:
                                menor_variancia = fk.define_janela_arestas(l, c, value, largura, altura)

                                if menor_variancia == 1:
                                    imagem[l, c, 0] = sum([b[l, c], b[l, c - 1],
                                                           b[l - 1, c], b[l - 1, c - 1],
                                                           b[l - 2, c], b[l - 2, c - 1]]) / 6
                                    imagem[l, c, 1] = sum([g[l, c], g[l, c - 1],
                                                           g[l - 1, c], g[l - 1, c - 1],
                                                           g[l - 2, c], g[l - 2, c - 1]]) / 6
                                    imagem[l, c, 2] = sum([r[l, c], r[l, c - 1],
                                                           r[l - 1, c], r[l - 1, c - 1],
                                                           r[l - 2, c], r[l - 2, c - 1]]) / 6

                                elif menor_variancia == 2:
                                    imagem[l, c, 0] = sum([b[l, c], b[l, c - 1],
                                                           b[l + 1, c], b[l - +1, c - 1],
                                                           b[l + 2, c], b[l + 2, c - 1]]) / 6
                                    imagem[l, c, 1] = sum([g[l, c], g[l, c - 1],
                                                           g[l + 1, c], g[l + 1, c - 1],
                                                           g[l + 2, c], g[l + 2, c - 1]]) / 6
                                    imagem[l, c, 2] = sum([r[l, c], r[l, c - 1],
                                                           r[l + 1, c], r[l + 1, c - 1],
                                                           r[l + 2, c], r[l + 2, c - 1]]) / 6

                        if l == 1:
                            if c == 1 or c == largura - 2:
                                imagem[l, c, 0] = fk.kuwahara_cantos_internos(l, c, value, b, largura, altura)
                                imagem[l, c, 1] = fk.kuwahara_cantos_internos(l, c, value, g, largura, altura)
                                imagem[l, c, 2] = fk.kuwahara_cantos_internos(l, c, value, r, largura, altura)

                            elif c != 0 and c != largura - 1 and c != 1 and c != altura - 2:
                                menor_variancia = fk.kuwahara_arestaS_internas(l, c, value, largura, altura)

                                if menor_variancia == 1:
                                    imagem[l, c, 0] = sum([b[l - 1, c - 2], b[l - 1, c - 1], b[l - 1, c],
                                                           b[l, c - 2], b[l, c - 1], b[l, c]]) / 6
                                    imagem[l, c, 1] = sum([g[l - 1, c - 2], g[l - 1, c - 1], g[l - 1, c],
                                                           g[l, c - 2], g[l, c - 1], g[l, c]]) / 6
                                    imagem[l, c, 2] = sum([r[l - 1, c - 2], r[l - 1, c - 1], r[l - 1, c],
                                                           r[l, c - 2], r[l, c - 1], r[l, c]]) / 6

                                elif menor_variancia == 2:
                                    imagem[l, c, 0] = sum([b[l - 1, c], b[l - 1, c + 1], b[l - 1, c + 2],
                                                           b[l, c], b[l, c + 1], b[l, c + 2]]) / 6
                                    imagem[l, c, 1] = sum([g[l - 1, c], g[l - 1, c + 1], g[l - 1, c + 2],
                                                           g[l, c], g[l, c + 1], g[l, c + 2]]) / 6
                                    imagem[l, c, 2] = sum([r[l - 1, c], r[l - 1, c + 1], r[l - 1, c + 2],
                                                           r[l, c], r[l, c + 1], r[l, c + 2]]) / 6

                                elif menor_variancia == 3:
                                    imagem[l, c, 0] = sum([b[l, c - 2], b[l, c - 1], b[l, c],
                                                           b[l + 1, c - 2], b[l + 1, c - 1], b[l + 1, c],
                                                           b[l + 2, c - 2], b[l + 2, c - 1], b[l + 2, c]]) / 9
                                    imagem[l, c, 1] = sum([g[l, c - 2], g[l, c - 1], g[l, c],
                                                           g[l + 1, c - 2], g[l + 1, c - 1], g[l + 1, c],
                                                           g[l + 2, c - 2], g[l + 2, c - 1], g[l + 2, c]]) / 9
                                    imagem[l, c, 2] = sum([r[l, c - 2], r[l, c - 1], r[l, c],
                                                           r[l + 1, c - 2], r[l + 1, c - 1], r[l + 1, c],
                                                           r[l + 2, c - 2], r[l + 2, c - 1], r[l + 2, c]]) / 9

                                elif menor_variancia == 4:
                                    imagem[l, c, 0] = sum([b[l, c], b[l, c + 1], b[l, c + 2],
                                                           b[l + 1, c], b[l + 1, c + 1], b[l + 1, c + 2],
                                                           b[l + 2, c], b[l + 2, c + 1], b[l + 2, c + 2]]) / 9
                                    imagem[l, c, 1] = sum([g[l, c], g[l, c + 1], g[l, c + 2],
                                                           g[l + 1, c], g[l + 1, c + 1], g[l + 1, c + 2],
                                                           g[l + 2, c], g[l + 2, c + 1], g[l + 2, c + 2]]) / 9
                                    imagem[l, c, 2] = sum([r[l, c], r[l, c + 1], r[l, c + 2],
                                                           r[l + 1, c], r[l + 1, c + 1], r[l + 1, c + 2],
                                                           r[l + 2, c], r[l + 2, c + 1], r[l + 2, c + 2]]) / 9

                        elif l == altura - 2:
                            if c == 1 or c == largura - 2:
                                imagem[l, c, 0] = fk.kuwahara_cantos_internos(l, c, value, b, largura, altura)
                                imagem[l, c, 1] = fk.kuwahara_cantos_internos(l, c, value, g, largura, altura)
                                imagem[l, c, 2] = fk.kuwahara_cantos_internos(l, c, value, r, largura, altura)

                            elif c != 0 and c != largura - 1 and c != 1 and c != altura - 2:
                                menor_variancia = fk.kuwahara_arestaS_internas(l, c, value, largura, altura)

                                if menor_variancia == 1:
                                    imagem[l, c, 0] = sum([b[l + 1, c - 2], b[l + 1, c - 1], b[l + 1, c],
                                                           b[l, c - 2], b[l, c - 1], b[l, c]]) / 6
                                    imagem[l, c, 1] = sum([g[l + 1, c - 2], g[l + 1, c - 1], g[l + 1, c],
                                                           g[l, c - 2], g[l, c - 1], g[l, c]]) / 6
                                    imagem[l, c, 2] = sum([r[l + 1, c - 2], r[l + 1, c - 1], r[l + 1, c],
                                                           r[l, c - 2], r[l, c - 1], r[l, c]]) / 6

                                elif menor_variancia == 2:
                                    imagem[l, c, 0] = sum([b[l + 1, c], b[l + 1, c + 1], b[l + 1, c + 2],
                                                           b[l, c], b[l, c + 1], b[l, c + 2]]) / 6
                                    imagem[l, c, 1] = sum([g[l + 1, c], g[l + 1, c + 1], g[l + 1, c + 2],
                                                           g[l, c], g[l, c + 1], g[l, c + 2]]) / 6
                                    imagem[l, c, 2] = sum([r[l + 1, c], r[l + 1, c + 1], r[l + 1, c + 2],
                                                           r[l, c], r[l, c + 1], r[l, c + 2]]) / 6

                                elif menor_variancia == 3:
                                    imagem[l, c, 0] = sum([b[l, c - 2], b[l, c - 1], b[l, c],
                                                           b[l - 1, c - 2], b[l - 1, c - 1], b[l - 1, c],
                                                           b[l - 2, c - 2], b[l - 2, c - 1], b[l - 2, c]]) / 9
                                    imagem[l, c, 1] = sum([g[l, c - 2], g[l, c - 1], g[l, c],
                                                           g[l - 1, c - 2], g[l - 1, c - 1], g[l - 1, c],
                                                           g[l - 2, c - 2], g[l - 2, c - 1], g[l - 2, c]]) / 9
                                    imagem[l, c, 2] = sum([r[l, c - 2], r[l, c - 1], r[l, c],
                                                           r[l - 1, c - 2], r[l - 1, c - 1], r[l - 1, c],
                                                           r[l - 2, c - 2], r[l - 2, c - 1], r[l - 2, c]]) / 9

                                elif menor_variancia == 4:
                                    imagem[l, c, 0] = sum([b[l, c], b[l, c + 1], b[l, c + 2],
                                                           b[l - 1, c], b[l - 1, c + 1], b[l - 1, c + 2],
                                                           b[l - 2, c], b[l - 2, c + 1], b[l - 2, c + 2]]) / 9
                                    imagem[l, c, 1] = sum([g[l, c], g[l, c + 1], g[l, c + 2],
                                                           g[l - 1, c], g[l - 1, c + 1], g[l - 1, c + 2],
                                                           g[l - 2, c], g[l - 2, c + 1], g[l - 2, c + 2]]) / 9
                                    imagem[l, c, 2] = sum([r[l, c], r[l, c + 1], r[l, c + 2],
                                                           r[l - 1, c], r[l - 1, c + 1], r[l - 1, c + 2],
                                                           r[l - 2, c], r[l - 2, c + 1], r[l - 2, c + 2]]) / 9

                        if c == 1:
                            if l != 0 and l != 1 and l != altura - 2 and l != altura - 1:
                                menor_variancia = fk.kuwahara_arestaS_internas(l, c, value, largura, altura)

                                if menor_variancia == 1:
                                    imagem[l, c, 0] = sum([b[l - 2, c - 1], b[l - 2, c],
                                                           b[l - 1, c - 1], b[l - 1, c],
                                                           b[l, c - 1], b[l, c]]) / 6
                                    imagem[l, c, 1] = sum([g[l - 2, c - 1], g[l - 2, c],
                                                           g[l - 1, c - 1], g[l - 1, c],
                                                           g[l, c - 1], g[l, c]]) / 6
                                    imagem[l, c, 2] = sum([r[l - 2, c - 1], r[l - 2, c],
                                                           r[l - 1, c - 1], r[l - 1, c],
                                                           r[l, c - 1], r[l, c]]) / 6

                                elif menor_variancia == 2:
                                    imagem[l, c, 0] = sum([b[l, c - 1], b[l, c],
                                                           b[l + 1, c - 1], b[l + 1, c],
                                                           b[l + 2, c - 1], b[l + 2, c]]) / 6
                                    imagem[l, c, 1] = sum([g[l, c - 1], g[l, c],
                                                           g[l + 1, c - 1], g[l + 1, c],
                                                           g[l + 2, c - 1], g[l + 2, c]]) / 6
                                    imagem[l, c, 2] = sum([r[l, c - 1], r[l, c],
                                                           r[l + 1, c - 1], r[l + 1, c],
                                                           r[l + 2, c - 1], r[l + 2, c]]) / 6

                                elif menor_variancia == 3:
                                    imagem[l, c, 0] = sum([b[l - 2, c], b[l - 2, c + 1], b[l - 2, c + 2],
                                                           b[l - 1, c], b[l - 1, c + 1], b[l - 1, c + 2],
                                                           b[l, c], b[l, c + 1], b[l, c + 2]]) / 9
                                    imagem[l, c, 1] = sum([g[l - 2, c], g[l - 2, c + 1], g[l - 2, c + 2],
                                                           g[l - 1, c], g[l - 1, c + 1], g[l - 1, c + 2],
                                                           g[l, c], g[l, c + 1], g[l, c + 2]]) / 9
                                    imagem[l, c, 2] = sum([r[l - 2, c], r[l - 2, c + 1], r[l - 2, c + 2],
                                                           r[l - 1, c], r[l - 1, c + 1], r[l - 1, c + 2],
                                                           r[l, c], r[l, c + 1], r[l, c + 2]]) / 9

                                elif menor_variancia == 4:
                                    imagem[l, c, 0] = sum([b[l, c], b[l, c + 1], b[l, c + 2],
                                                           b[l + 1, c], b[l + 1, c + 1], b[l + 1, c + 2],
                                                           b[l + 2, c], b[l + 2, c + 1], b[l + 2, c + 2]]) / 9
                                    imagem[l, c, 1] = sum([g[l, c], g[l, c + 1], g[l, c + 2],
                                                           g[l + 1, c], g[l + 1, c + 1], g[l + 1, c + 2],
                                                           g[l + 2, c], g[l + 2, c + 1], g[l + 2, c + 2]]) / 9
                                    imagem[l, c, 2] = sum([r[l, c], r[l, c + 1], r[l, c + 2],
                                                           r[l + 1, c], r[l + 1, c + 1], r[l + 1, c + 2],
                                                           r[l + 2, c], r[l + 2, c + 1], r[l + 2, c + 2]]) / 9

                        if c == largura - 2:
                            if l != 0 and l != 1 and l != altura - 2 and l != altura - 1:
                                menor_variancia = fk.kuwahara_arestaS_internas(l, c, value, largura, altura)

                                if menor_variancia == 1:
                                    imagem[l, c, 0] = sum([b[l - 2, c + 1], b[l - 2, c],
                                                           b[l - 1, c + 1], b[l - 1, c],
                                                           b[l, c + 1], b[l, c]]) / 6
                                    imagem[l, c, 1] = sum([g[l - 2, c + 1], g[l - 2, c],
                                                           g[l - 1, c + 1], g[l - 1, c],
                                                           g[l, c + 1], g[l, c]]) / 6
                                    imagem[l, c, 2] = sum([r[l - 2, c + 1], r[l - 2, c],
                                                           r[l - 1, c + 1], r[l - 1, c],
                                                           r[l, c + 1], r[l, c]]) / 6

                                elif menor_variancia == 2:
                                    imagem[l, c, 0] = sum([b[l, c + 1], b[l, c],
                                                           b[l + 1, c + 1], b[l + 1, c],
                                                           b[l + 2, c + 1], b[l + 2, c]]) / 6
                                    imagem[l, c, 1] = sum([g[l, c + 1], g[l, c],
                                                           g[l + 1, c + 1], g[l + 1, c],
                                                           g[l + 2, c + 1], g[l + 2, c]]) / 6
                                    imagem[l, c, 2] = sum([r[l, c + 1], r[l, c],
                                                           r[l + 1, c + 1], r[l + 1, c],
                                                           r[l + 2, c + 1], r[l + 2, c]]) / 6

                                elif menor_variancia == 3:
                                    imagem[l, c, 0] = sum([b[l - 2, c], b[l - 2, c - 1], b[l - 2, c - 2],
                                                           b[l - 1, c], b[l - 1, c - 1], b[l - 1, c - 2],
                                                           b[l, c], b[l, c - 1], b[l, c - 2]]) / 9
                                    imagem[l, c, 1] = sum([g[l - 2, c], g[l - 2, c - 1], g[l - 2, c - 2],
                                                           g[l - 1, c], g[l - 1, c - 1], g[l - 1, c - 2],
                                                           g[l, c], g[l, c - 1], g[l, c - 2]]) / 9
                                    imagem[l, c, 2] = sum([r[l - 2, c], r[l - 2, c - 1], r[l - 2, c - 2],
                                                           r[l - 1, c], r[l - 1, c - 1], r[l - 1, c - 2],
                                                           r[l, c], r[l, c - 1], r[l, c - 2]]) / 9

                                elif menor_variancia == 4:
                                    imagem[l, c, 0] = sum([b[l, c], b[l, c - 1], b[l, c - 2],
                                                           b[l + 1, c], b[l + 1, c - 1], b[l + 1, c - 2],
                                                           b[l + 2, c], b[l + 2, c - 1], b[l + 2, c - 2]]) / 9
                                    imagem[l, c, 1] = sum([g[l, c], g[l, c - 1], g[l, c - 2],
                                                           g[l + 1, c], g[l + 1, c - 1], g[l + 1, c - 2],
                                                           g[l + 2, c], g[l + 2, c - 1], g[l + 2, c - 2]]) / 9
                                    imagem[l, c, 2] = sum([r[l, c], r[l, c - 1], r[l, c - 2],
                                                           r[l + 1, c], r[l + 1, c - 1], r[l + 1, c - 2],
                                                           r[l + 2, c], r[l + 2, c - 1], r[l + 2, c - 2]]) / 9

                        if l != 0 and l != 1 and l != altura - 2 and l != altura - 1:
                            if c != 0 and c != 1 and c != largura - 2 and c != largura - 1:
                                menor_variancia = fk.define_janela_menor_variancia_meios(l, c, value)

                                if menor_variancia == 1:
                                    imagem[l, c, 0] = sum([b[l - 2, c - 2], b[l - 2, c - 1], b[l - 2, c],
                                                           b[l - 1, c - 2], b[l - 1, c - 1], b[l - 1, c],
                                                           b[l, c - 2], b[l, c - 1], b[l, c]]) / 9
                                    imagem[l, c, 1] = sum([g[l - 2, c - 2], g[l - 2, c - 1], g[l - 2, c],
                                                           g[l - 1, c - 2], g[l - 1, c - 1], g[l - 1, c],
                                                           g[l, c - 2], g[l, c - 1], g[l, c]]) / 9
                                    imagem[l, c, 2] = sum([r[l - 2, c - 2], r[l - 2, c - 1], r[l - 2, c],
                                                           r[l - 1, c - 2], r[l - 1, c - 1], r[l - 1, c],
                                                           r[l, c - 2], r[l, c - 1], r[l, c]]) / 9

                                elif menor_variancia == 2:
                                    imagem[l, c, 0] = sum([b[l - 2, c], b[l - 2, c + 1], b[l - 2, c + 2],
                                                           b[l - 1, c], b[l - 1, c + 1], b[l - 1, c + 2],
                                                           b[l, c], b[l, c + 1], b[l, c + 2]]) / 9
                                    imagem[l, c, 1] = sum([g[l - 2, c], g[l - 2, c + 1], g[l - 2, c + 2],
                                                           g[l - 1, c], g[l - 1, c + 1], g[l - 1, c + 2],
                                                           g[l, c], g[l, c + 1], g[l, c + 2]]) / 9
                                    imagem[l, c, 2] = sum([r[l - 2, c], r[l - 2, c + 1], r[l - 2, c + 2],
                                                           r[l - 1, c], r[l - 1, c + 1], r[l - 1, c + 2],
                                                           r[l, c], r[l, c + 1], r[l, c + 2]]) / 9

                                elif menor_variancia == 3:
                                    imagem[l, c, 0] = sum([b[l, c - 2], b[l, c - 1], b[l, c],
                                                           b[l + 1, c - 2], b[l + 1, c - 1], b[l + 1, c],
                                                           b[l + 2, c - 2], b[l + 2, c - 1], b[l + 2, c]]) / 9
                                    imagem[l, c, 1] = sum([g[l, c - 2], g[l, c - 1], g[l, c],
                                                           g[l + 1, c - 2], g[l + 1, c - 1], g[l + 1, c],
                                                           g[l + 2, c - 2], g[l + 2, c - 1], g[l + 2, c]]) / 9
                                    imagem[l, c, 2] = sum([r[l, c - 2], r[l, c - 1], r[l, c],
                                                           r[l + 1, c - 2], r[l + 1, c - 1], r[l + 1, c],
                                                           r[l + 2, c - 2], r[l + 2, c - 1], r[l + 2, c]]) / 9

                                elif menor_variancia == 4:
                                    imagem[l, c, 0] = sum([b[l, c], b[l, c + 1], b[l, c + 2],
                                                           b[l + 1, c], b[l + 1, c + 1], b[l + 1, c + 2],
                                                           b[l + 2, c], b[l + 2, c + 1], b[l + 2, c + 2]]) / 9
                                    imagem[l, c, 1] = sum([g[l, c], g[l, c + 1], g[l, c + 2],
                                                           g[l + 1, c], g[l + 1, c + 1], g[l + 1, c + 2],
                                                           g[l + 2, c], g[l + 2, c + 1], g[l + 2, c + 2]]) / 9
                                    imagem[l, c, 2] = sum([r[l, c], r[l, c + 1], r[l, c + 2],
                                                           r[l + 1, c], r[l + 1, c + 1], r[l + 1, c + 2],
                                                           r[l + 2, c], r[l + 2, c + 1], r[l + 2, c + 2]]) / 9

                        cont += 1

                        print("Aplicando filtro. Aguarde... [{:.0f}%]".format((cont*100) / pixels_imagem_1))

                print("---\nFiltro Kuwahara aplicado na Imagem 1.")
                cv2.imshow("{} com Filtro Kuwahara".format(nome_da_imagem_1), imagem)

                salvar = tkmb.askyesno("Salvar imagem com Filtro Kuwahara", "Você deseja salvar esta modificação?")
                if salvar:
                    cv2.imwrite(os.path.join(local_imagem_1, '{} com Filtro Kuwahara.jpg'.format(nome_da_imagem_1)),
                                imagem)
                    print("---\nNova Imagem 1 salva em: {}".format(local_imagem_1))
                    print(" Com o nome: {} com Filtro Kuwahara.jpg".format(nome_da_imagem_1))

        except AttributeError:
            tkmb.showinfo("Erro ao abrir arquivo!", "Você selecionou um arquivo estranho. \n"
                                                    "Selecione apenas imagens .jpg ou .png.")


# =========================[ Histograma ]::.
def Histograma():  # Função executada ao clicar no botão "Ver Histograma".

    if caminho_1 is None:  # Verifica se o usuário já selecionou uma Imagem 1.
        tkmb.showinfo("Sem imagem!", "Certifique-se de que pelo menos a Imagem 1 foi devidamente selecionada.")

    else:

        try:

            if preto_e_branco1:  # Verifica se a Imagem 1 é preto-e-branco (ou monocromática).

                imagem2 = cv2.imread(caminho_1)
                imagem = cv2.cvtColor(imagem2, cv2.COLOR_BGR2GRAY)

                altura, largura = imagem.shape[0], imagem.shape[1]
                lista_niveis = []

                for l in range(altura):
                    for c in range(largura):
                        lista_niveis.append(imagem[l, c])

                lista_niveis.sort()
                lista_niveis.append(256)
                lista_niveis_separados = []
                fhpb.separa_niveis_por_listas(lista_niveis, lista_niveis_separados)

                fig = plt.figure()

                # Gerando as coordenadas para o gráfico do plano azul
                termos_x = []
                termos_y = []

                fhpb.gera_termosY(lista_niveis_separados, termos_y)
                fhpb.gera_termos_x(termos_x)

                plano_blue = fig.add_subplot(1, 1, 1)
                plano_blue.bar(termos_x, termos_y, align='center', color="#777777")

                print("---\nExibindo Histograma!")

                plt.show()

            else:

                imagem = cv2.imread(caminho_1)

                altura, largura = imagem.shape[0], imagem.shape[1]
                b = []
                g = []
                r = []
                for l in range(altura):
                    for c in range(largura):
                        cor = imagem[l, c]
                        b.append(cor[0])
                        g.append(cor[1])
                        r.append(cor[2])

                b.sort()
                b.append(256)
                lista_niveis_b = []
                fh.separa_niveis_por_listas(b, lista_niveis_b)

                g.sort()
                g.append(256)
                lista_niveis_g = []
                fh.separa_niveis_por_listas(g, lista_niveis_g)

                r.sort()
                r.append(256)
                lista_niveis_r = []
                fh.separa_niveis_por_listas(r, lista_niveis_r)

                fig = plt.figure()

                # Gerando as coordenadas para o gráfico do plano azul
                termos_x_b = []
                termos_y_b = []

                fh.gera_termosY(lista_niveis_b, termos_y_b)
                fh.gera_termos_x(termos_x_b)

                plano_blue = fig.add_subplot(2, 2, 1)
                plano_blue.bar(termos_x_b, termos_y_b, align='center', color="#0000FF")

                # Gerando as coordenadas para o gráfico do plano verde
                termos_x_g = []
                termos_y_g = []

                fh.gera_termosY(lista_niveis_g, termos_y_g)
                fh.gera_termos_x(termos_x_g)

                cont = 240

                plano_green = fig.add_subplot(2, 2, 2)
                plano_green.bar(termos_x_g, termos_y_g, align='center', color="#32CD32")

                # Gerando as coordenadas para o gráfico do plano vermelho
                termos_x_r = []
                termos_y_r = []

                fh.gera_termosY(lista_niveis_r, termos_y_r)
                fh.gera_termos_x(termos_x_r)

                plano_red = fig.add_subplot(2, 1, 2)
                plano_red.bar(termos_x_g, termos_y_g, align='center', color="#FF0000")

                print("---\nExibindo Histograma!")

                plt.show()

        except AttributeError:
            tkmb.showinfo("Erro ao abrir arquivo!", "Você selecionou um arquivo estranho. \n"
                                                    "Selecione apenas imagens .jpg ou .png.")


# =========================[ Cálculo PSNR ]::.
def PSNR():  # Função executada ao clicar no botão "Calcular PSNR".

    if (caminho_1 is None) or (caminho_2 is None):  # Verifica se o usuário já selecionou ambas as Imagens 1 e 2.
        tkmb.showinfo("Sem imagens!", "Certifique-se de que ambas as Imagens 1 e 2 foram devidamente selecionadas.")

    else:

        try:

            print("---\nCalculando PSNR. Aguarde..."
                  + TColor.WARNING + "(Dependendo do tamanho das imagens isso pode levar algum tempo.)" + TColor.ENDC)

            imagem1 = cv2.imread(caminho_1)
            imagem2 = cv2.imread(caminho_2)

            B1 = imagem1[:, :, 0]
            B2 = imagem2[:, :, 0]
            G1 = imagem1[:, :, 1]
            G2 = imagem2[:, :, 1]
            R1 = imagem1[:, :, 2]
            R2 = imagem2[:, :, 2]

            MAX = 255.0

            altura, largura = imagem1.shape[0], imagem1.shape[1]
            mxn = altura * largura
            acumulador = 0
            acumulador2 = 0
            cont = 0
            for l in range(altura):
                for c in range(largura):
                    dif1 = (int(B1[l, c]) - int(B2[l, c])) ** 2
                    dif2 = (int(G1[l, c]) - int(G2[l, c])) ** 2
                    dif3 = (int(R1[l, c]) - int(R2[l, c])) ** 2
                    acumulador += (dif1 + dif2 + dif3)

            mse = acumulador / mxn / 3

            psnr1 = 20 * math.log10(255.0 / (math.sqrt(mse)))

            print("---\nPSNR Calculado!")

            tkmb.showinfo("PSNR Calculado!",
                          "O Peak Signal-to-Noise Ratio das imagens selecionadas é de aproximadamente: "
                          "{:.4f}dB".format(psnr1))

        except IndexError:
            tkmb.showinfo("Erro ao calcular!", "Você selecionou imagens muito diferentes.\n"
                                               "Tente novamente com imagens parecidas.")

        except ZeroDivisionError:
            tkmb.showinfo("Erro ao calcular!", "Você selecionou imagens exatamente iguais.\n"
                                               "Tente novamente com imagens de qualidades diferentes.")

        except AttributeError:
            tkmb.showinfo("Erro ao abrir arquivo!", "Você selecionou um arquivo estranho. \n"
                                                    "Selecione apenas imagens .jpg ou .png.")


# =========================[ Botões / Opções ]::.
botao_verimg = ttk.Button(text="Ver Imagem 1 Original", command=VerImagem1)
botao_mediana = ttk.Button(text="Aplicar Filtro da Mediana", command=Mediana)
botao_kuwahara = ttk.Button(text="Aplicar Filtro Kuwahara", command=Kuwahara)
botao_histograma = ttk.Button(text="Ver Histograma", command=Histograma)
botao_psnr = ttk.Button(text="Calcular PSNR", command=PSNR)

botao_verimg.pack()
botao_mediana.pack()
botao_kuwahara.pack()
botao_histograma.pack()
botao_psnr.pack()

botao_sair = ttk.Button(text="Sair", command=Sair)
botao_sair.pack()

# =========================[ Barra de Status ]::.
statusBar = Label(janela, text="Nenhuma imagem selecionada.", relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)

# =========================[ Fim do Programa ]::.
janela.mainloop()

print("---\n" + TColor.BOLD + "Você saiu do programa.\n" + TColor.OKBLUE + " ┕ Volte sempre!" + TColor.ENDC)

# =========================[ + de 1100 LINHAS!!! =P ( ~ Fora as centenas de linhas das Funções Externas! XD )]::.
