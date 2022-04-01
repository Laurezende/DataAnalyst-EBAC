# -*- coding: utf-8 -*-
"""2_listas_dicionarios_e_conjuntos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1esU5wxy7c_5UABPzVrV891MT6az-Fj-S

**1.0 Listas**

**1.1 Criando uma lista chamada filmes com o nome dos 10 primeiros filmes mais bem avaliados no
site no IMDB**
"""

filmes = ['Um Sonho de Liberdade', ' O Poderoso Chefão', 'O Poderoso Chefão II', 'Batman: O Cavaleiro das Trevas', '12 Homens e uma Sentença',
          'A Lista de Schindler', 'O Senhor dos Anéis: O Retorno do Rei','Pulp Fiction: Tempo de Violência', 'Três Homens em Conflito',
          'O Senhor dos Anéis: A Sociedade do Anel']
print(filmes)

filme = filmes.pop(1)
print(filmes)

filmes.insert(0, filme)
print(filmes)

"""**2.0 Conjuntos**

**2.1 Simulando a duplicação dos três últimos filmes da lista**
"""

filmes = ['Um Sonho de Liberdade', ' O Poderoso Chefão', 'O Poderoso Chefão II', 'Batman: O Cavaleiro das Trevas', '12 Homens e uma Sentença',
          'A Lista de Schindler', 'O Senhor dos Anéis: O Retorno do Rei','Pulp Fiction: Tempo de Violência', 'Pulp Fiction: Tempo de Violência',
          'Três Homens em Conflito', 'Três Homens em Conflito', 'O Senhor dos Anéis: A Sociedade do Anel', 'O Senhor dos Anéis: A Sociedade do Anel']
print(filmes)
print(len(filmes))

"""**2.2 Utilizando a conversão set e list para remover os valores duplicados**"""

filmes = list(set(filmes))
print(filmes)
print(len(filmes))

"""**3.0 Dicionários**

**3.1 Repetindo os exercícios da parte 1 (listas) porém com os elementos da lista filmes como dicionários**
"""

filmes = [
    {'nome':'Um Sonho de Liberdade', 'ano':1994, 'sinopse':'Dois homens presos se reúnem ao longo de vários anos, encontrando consolo e eventual redenção através de atos de decência comum.'},
    {'nome':'O Poderoso Chefão', 'ano': 1972, 'sinopse':'O patriarca idoso de uma dinastia do crime organizado transfere o controle de seu império clandestino para seu filho relutante.'},
    {'nome':'O Poderoso Chefão II', 'ano':1974, 'sinopse':'Em 1950, Michael Corleone, agora à frente da família, tenta expandir o negócio do crime a Las Vegas, Los Angeles e Cuba. Paralelamente, é revelada a história de Vito Corleone, e de como saiu da Sicília e chegou a Nova Iorque.'},
    {'nome': 'Batman: O Cavaleiro das Trevas', 'ano': 2008, 'sinopse': 'Quando a ameaça conhecida como O Coringa surge de seu passado, causa estragos e caos nas pessoas de Gotham. O Cavaleiro das Trevas deve aceitar um dos maiores testes para combater a injustiça.'},
    {'nome':'12 Homens e uma Sentença', 'ano':1957, 'sinopse': 'Um jurado que se aposenta tenta evitar um erro judicial forçando seus colegas a reconsiderarem as evidências.'},
    {'nome': ' A Lista de Schindler', 'ano': 1993, 'sinopse': 'Depois de testemunhar a perseguição dos judaicos na Polônia ocupada pelos alemães durante a Segunda Guerra Mundial, o industrial Oskar Schindler se começa a preocupar com sua força de trabalho judaica.'},
    {'nome': 'O Senhor dos Anéis: O Retorno do Rei', 'ano': 2003, 'sinopse': 'Gandalf e Aragorn lideram o Mundo dos Homens contra o exército de Sauron para desviar o olhar de Frodo e Sam quando eles se aproximam á Montanha da Perdição com o Um Anel.'},
    {'nome': 'Pulp Fiction: Tempo de Violência', 'ano': 1994, 'sinopse': 'As vidas de dois assassinos da máfia, um boxeador, um gângster e sua esposa, e um par de bandidos se entrelaçam em quatro histórias de violência e redenção.'},
    {'nome': 'Três Homens em Conflito', 'ano': 1966, 'sinopse': 'Um impostor se junta com dois homens para encontrar fortuna num remoto cemitério.'},
    {'nome': 'O Senhor dos Anéis: A Sociedade do Anel', 'ano': 2001, 'sinopse': 'Um manso hobbit do Condado e oito companheiros partem em uma jornada para destruir o poderoso Um Anel e salvar a Terra-media das Trevas.'},
  
]
print(filmes)

filme = filmes.pop(1)
print(filmes)

filmes.insert(0, filme)
print(filmes)