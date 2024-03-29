# -*- coding: utf-8 -*-
"""1_variaveis_e_tipos_de_dados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-dx9fMFtKsabe_q_rVRH2-ym_ietlOMs

**1.0 Números**

**1.1 Preenchendo células de código com os valores de (A), (B) e (C) na tabela de
ticket médio abaixo**

| Dia   | Valor Total Vendas | Qtd Total Vendas | Ticket Médio |
|-------|--------------------|------------------|--------------|
| 19/01 | (A)                | 3                | 320.52       |
| 20/01 | 834.47             | (B)              | 119.21       |
| 23/01 | 15378.12           | 5                | (C)          |
"""

#(A)
Qtd_Total_Vendas_19 = 3
Ticket_Medio_19 = 320.52

Valor_Total_Vendas_19 = Qtd_Total_Vendas_19 * Ticket_Medio_19
print(Valor_Total_Vendas_19)

#(B)
Valor_Total_Vendas_20 = 834.47
Ticket_Medio_20 = 119.21

Qtd_Total_Vendas_20 = Valor_Total_Vendas_20 / Ticket_Medio_20
print(Qtd_Total_Vendas_20)

#(C)
Valor_Total_Vendas_23 = 15378.12
Qtd_Total_Vendas_23 = 5

Ticket_Medio_23 = Valor_Total_Vendas_23 / Qtd_Total_Vendas_23
print(Ticket_Medio_23)

"""**2.0 Strings**

**2.1 Aplicando três métodos distintos na string abaixo**
"""

cancao = 'Roda mundo, roda gigante, roda moinho, roda pião.'

cancao.casefold()

cancao.upper()

cancao.title()

"""**2.2 Extraindo da string abaixo o valor da taxa selic na variável selic e o valor do ano na
variavel ano**
"""

noticia = 'Selic vai a 2,75% e supera expectativas; é a primeira alta em 6 anos.'

#Selic
posicao_percentual = noticia.find('%')
selic = noticia[posicao_percentual-4:posicao_percentual]
print(posicao_percentual)
print(selic)

#Ano
posicao_ano = noticia.find('ano')
ano = noticia[posicao_ano -2: posicao_ano]
print(posicao_ano)
print(ano)

"""**3.0 Booleanos**

**3.1 Utilizando a tabela da verdade para responder: Qual o valor da variável x?**

| **A**    | **B**    | **A OR B** | **A AND B** | **NOT A** |
|----------|----------|------------|-------------|-----------|
| **TRUE** | **TRUE** | **TRUE**   | **TRUE**    | FALSE     |
| **TRUE** | FALSE    | **TRUE**   | FALSE       | FALSE     |
| FALSE    | FALSE    | FALSE      | FALSE       | **TRUE**  |
| FALSE    | **TRUE** | **TRUE**   | FALSE       | **TRUE**  |
"""

a = False
b = True

x = not a & b

print(False & True)
print(not False)

x = not False
print(x)