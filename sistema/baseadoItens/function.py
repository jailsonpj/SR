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

def carregaMovieLens():  #retorna o id do filme e o respectivo nome do filme
    filmes = { }
    for linha in open('u.item',encoding="ISO-8859-1"):#o enconding foi usado para solucionar o erro na abertura do arquivo
        (id,titulo) = linha.split('|') [0:2] #começa a pegar da posição 0 e vai até a segunda quebra
        filmes[id] = titulo
    #print(filmes)
    base = { }
    for linha in open('u.data',encoding="ISO-8859-1"): #carrega os dados do arquivo u.data que contem o numero do user,o id do filme , a nota do filme e o tempo
        (usuario,idfilme,nota,tempo) = linha.split('\t')#\t é tab
        base.setdefault(usuario,{ })
        base[usuario][filmes[idfilme]] = float(nota)

    return base

def calculaItensSimilares(base):
    result = {}
    for item in base:
        notas = getSimilares(base,item)
        result[item] = notas
    return result

def getRecomendacoesItens(baseUsuario,similaridadeItens,usuario):
    notasUsuario = baseUsuario[usuario] #recebe a base de dados dos usuários
    notas={}
    totalSimilaridade={}

    for (item,nota) in notasUsuario.items():#percorre a base de daods e pega cada item e nota
        for (similaridade,item2) in similaridadeItens[item]: #percorre em um for e verifica a similaridade do item ja com a funcao de similaridade rodada e guarda a similaridade e o item
            if item2 in notasUsuario:
                continue #faz com que o item não faça o calculo dele mesmo

            notas.setdefault(item2,0)#inicia um item com um valor
            notas[item2] += similaridade * nota #na posição do item ele faz o calculo da similaridade com a nota da base de dados
            totalSimilaridade.setdefault(item2,0) #soma as notas
            totalSimilaridade[item2] += similaridade

    rankings=[(score/totalSimilaridade[item],item) for item,score in notas.items()]
    rankings.sort()
    rankings.reverse()
    return rankings
