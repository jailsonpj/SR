#from db_users import *
from math import sqrt

def euclidiana(base,user1,user2):
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
    return similaridade

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
    return rankings
