from db_users import *
from function import *


'''print(euclidiana(avaliacoesUsuario,'Pedro','Janaina'))
print(euclidiana(avaliacoesFilme,'Star Wars','Star Trek'))
print(print(getSimilares(avaliacoesUsuario,'Pedro')))
print(print(getSimilares(avaliacoesFilme,'Star Wars')))
print(getRecomendacoes(avaliacoesUsuario,'Leonardo'))
print(getRecomendacoes(avaliacoesFilme,'Star Wars'))'''
base = carregaMovieLens()
#print(getSimilares(base,'1'))#usuários mais parecidos com o 212
print(getRecomendacoes(base,'1'))
