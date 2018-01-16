from db_itens import *
from function import *

print(getSimilares(avaliacoesFilme,'O Ultimato Bourne'))

itens = calculaItensSimilares(avaliacoesFilme)
print(itens)
