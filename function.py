from db_users import avaliacoes
from math import sqrt

def euclidiana(user1,user2):
    dados = {}

    for item in avaliacoes[user1]:
        if item in avaliacoes[user2]:
            dados[item] = 1

    if len(dados) == 0:
        return 0

    soma = sum ([pow(avaliacoes[user1][item] - avaliacoes[user2][item],2)
                    for item in avaliacoes[user1] if item in avaliacoes[user2]
                ])
    return 1/(1+sqrt(soma))

def getSimilares(user): #retorna a similaridade de um usuários com todos os outros usuários
    similaridade = [(euclidiana(user, outro), outro)
                    for outro in avaliacoes if outro != user]
    similaridade.sort()
    similaridade.reverse()
    return similaridade

def getRecomendacoes(user):
    totais = {}
    somasimilaridade = {}

    for outro in avaliacoes: #percorre usuários
        if outro == user:
            continue

        similaridade = euclidiana(user,outro)

        if similaridade <= 0:
            continue

        for item in avaliacoes[outro]: #percorre filmes assistidos pelo usuário
            if item not in avaliacoes[user]: #verifica os filmes que não estão avaliados pelo usuario
                totais.setdefault(item,0)
                totais[item] += avaliacoes[outro][item] * similaridade
                somasimilaridade.setdefault(item,0)
                somasimilaridade[item] += similaridade

    rankings = [(total/somasimilaridade[item],item) for item , total in totais.items()]
    rankings.sort()
    rankings.reverse()
    return rankings
