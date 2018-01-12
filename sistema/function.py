#from db_users import *
from math import sqrt

def euclidiana(base,user1,user2): #faz o calculo de aproximidade dos usuários
    dados = {}

    for item in base[user1]:
        if item in base[user2]:
            dados[item] = 1

    if len(dados) == 0:
        return 0

    soma = sum ([pow(base[user1][item] - base[user2][item],2)
                    for item in base[user1] if item in base[user2]
                ])
    return 1/(1+sqrt(soma))

def getSimilares(base,user): #retorna a similaridade de um usuários com todos os outros usuários
    similaridade = [(euclidiana(base,user, outro), outro)
                    for outro in base if outro != user]
    similaridade.sort()
    similaridade.reverse()
    return similaridade[0:30] #retorna os 30 primeiros

def getRecomendacoes(base,user):
    totais = {}
    somasimilaridade = {}

    for outro in base: #percorre usuários
        if outro == user:
            continue

        similaridade = euclidiana(base,user,outro)

        if similaridade <= 0:
            continue

        for item in base[outro]: #percorre filmes assistidos pelo usuário
            if item not in base[user]: #verifica os filmes que não estão avaliados pelo usuario
                totais.setdefault(item,0)
                totais[item] += base[outro][item] * similaridade
                somasimilaridade.setdefault(item,0)
                somasimilaridade[item] += similaridade

    rankings = [(total/somasimilaridade[item],item) for item , total in totais.items()]
    rankings.sort()
    rankings.reverse()
    return rankings[0:30]#retorna os 30 primeiros  registros

def carregaMovieLens():  #retorna o id do filme e o respectivo nome do filme
    filmes = { }
    for linha in open('u.item',encoding="ISO-8859-1"):#o enconding foi usado para solucionar o erro na abertura do arquivo
        (id,titulo) = linha.split('|') [0:2] #começa a pegar da posição 0 e vai até a segunda qebra
        filmes[id] = titulo
    #print(filmes)
    base = { }
    for linha in open('u.data',encoding="ISO-8859-1"): #carrega os dados do arquivo u.data que contem o numero do user,o id do filme , a nota do filme e o tempo
        (usuario,idfilme,nota,tempo) = linha.split('\t')#\t é tab
        base.setdefault(usuario,{ })
        base[usuario][filmes[idfilme]] = float(nota)

    return base
