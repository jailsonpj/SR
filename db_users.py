
from math import sqrt



avaliacoes = {'Ana': #chave ana tem , chave filme e um valor nota para o determinado filme
                {'Freddy x Jason': 2.5,
                    'O Ultimato Bourne': 3.5,
                    'Star Trek': 3.0,
                    'Exterminador do Futuro': 3.5,
                    'Norbit': 2.5,
                    'Star Wars': 3.0},

            'Marcos':
                {'Freddy x Jason': 3.0,
                    'O Ultimato Bourne': 3.5,
                    'Star Trek': 1.5,
                    'Exterminador do Futuro': 5.0,
                    'Star Wars': 3.0,
                    'Norbit': 3.5},

            'Pedro':
                {'Freddy x Jason': 2.5,
                    'O Ultimato Bourne': 3.0,
                    'Exterminador do Futuro': 3.5,
                    'Star Wars': 4.0},

            'Claudia':
                {'O Ultimato Bourne': 3.5,
                    'Star Trek': 3.0,
                    'Star Wars': 4.5,
                    'Exterminador do Futuro': 4.0,
                    'Norbit': 2.5},

            'Adriano':
                {'Freddy x Jason': 3.0,
                    'O Ultimato Bourne': 4.0,
                    'Star Trek': 2.0,
                    'Exterminador do Futuro': 3.0,
                    'Star Wars': 3.0,
                    'Norbit': 2.0},

            'Janaina':
                {'Freddy x Jason': 3.0,
                    'O Ultimato Bourne': 4.0,
                    'Star Wars': 3.0,
                    'Exterminador do Futuro': 5.0,
                    'Norbit': 3.5},

            'Leonardo':
                {'O Ultimato Bourne':4.5,
                    'Norbit':1.0,
                    'Exterminador do Futuro':4.0}
}


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
