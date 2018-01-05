from db_users import avaliacoes,euclidiana


ava =  avaliacoes ['Ana']['Star Trek']
ava1 = avaliacoes ['Marcos']['Star Trek']

print(ava)  #imprime a nota de avaliação do filme Star Trek , avaliado por Ana
print(ava1) #imprime a nota de avaliação do filme Star Trek , avaliado por Marcos
print('################')
print ('Todos os filmes da ana com suas notas de avalição: ')
print(avaliacoes['Ana']) #imprime todos os filmes avaliados por Ana

print('##############')
print(euclidiana('Leonardo','Ana'))
print(euclidiana('Claudia','Ana'))