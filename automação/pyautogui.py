# importação de bibliotecas

import pyautogui

pyautogui.PAUSE = 0.5 # pausa do pyautogui para o sistema responder

import pandas

import time


# acessando o site da empresa

pyautogui.press("win")

pyautogui.write("chrome")

pyautogui.press("enter")

time.sleep(2)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")

# login / senha para acessar o site da empresa

time.sleep(2)

pyautogui.click(x=638, y=467)

pyautogui.write("usuário123@gmail.com")

pyautogui.press("tab")

pyautogui.write("usuario123")

pyautogui.press("tab")

pyautogui.press("enter")


# acessando área para o cadastramento do produto

# usando pandas para fazer a vereficação dos produtos

tabela_dados = pandas.read_csv("automação/produtos.csv")

pyautogui.click(x=677, y=324)


for linha in tabela_dados.index: # index == acessar todos os itens da tabela

    # codigo do produto

    codigo_cadastrado = tabela_dados.loc[linha, "codigo"]

    pyautogui.write(codigo_cadastrado)

    pyautogui.press("tab")


    # marca do produto

    marca_cadastrada = tabela_dados.loc[linha, "marca"]

    pyautogui.write(marca_cadastrada)

    pyautogui.press("tab")


    # tipo do produto

    tipo_cadastrado = tabela_dados.loc[linha, "tipo"]

    pyautogui.write(tipo_cadastrado)

    pyautogui.press("tab")


    # categoria do produto

    categoria_cadastrada = tabela_dados.loc[linha, "categoria"]

    pyautogui.write(f'{categoria_cadastrada}')

    pyautogui.press("tab")


    # preço unitario do produto

    unitario_cadastrado = tabela_dados.loc[linha, "preco_unitario"]

    pyautogui.write(f'{unitario_cadastrado}')

    pyautogui.press("tab")


    # custo do produto

    custos_cadastrado = tabela_dados.loc[linha, "custo"]

    pyautogui.write(f'{custos_cadastrado}')

    pyautogui.press("tab")


    # obs do produto

    obs_cadastrado = tabela_dados.loc[linha, "obs"]

    if(obs_cadastrado == "NaN"):

        pyautogui.press("tab")

        pyautogui.press("enter")

    else:

        pyautogui.write(f'{obs_cadastrado}')

        pyautogui.press("tab")

        pyautogui.press("enter")


    # finalização da entrega do produto

    pyautogui.scroll(5000)

    pyautogui.click(x=677, y=324)