import re
from numpy import concatenate
from random import randrange
'''Este script foi desenvolvido para extrair os tweets já rotulados
   pelos membros do grupo.
   Parte da extração e pré-processamento para treinamento de um Naïve Bayes.
'''

def extract_labeled(data,file):
	'''Esta função realiza a extração retornando a lista de documentos
	rotulado do total de exemplos no documento passado.'''
	new_list=[]
	c_1 = 0
	c_0 = 0
	for tweet in data:
	    words = re.findall(r"\t[0-1]",tweet)
	    if len(words)>0:
	        new_list.append(tweet)
	        if tweet.endswith('\t1'):
	        	c_1 += 1
	        elif tweet.endswith('\t0'):
	        	c_0 += 1
	        #Para debugar
	        #else:
	        #	print(tweet[-20:])

	print(f'\nQuantidade de exemplos rotulados:', len(new_list))
	print(f'Documento: {file}')
	print(f'Quantidade contra (0) - {c_0} e a favor (1) - {c_1}.')
	return new_list

arquivos = ['twitter_lava_joa.data','twitter_vaza_joa.data',
'twitter_lava_Pedro.data','twitter_vaza_Pedro.data','twitter_lava_du.data','twitter_vaza_du.data']

#Concatenando todos os documentos e removendo duplicatas
t1 = []
for i in arquivos:
	data_file = i
	with open(data_file,"r",encoding="utf8") as f_open:
	    keys = f_open.read().splitlines()

	t1.append(extract_labeled(keys,i))

final_list = list(set(concatenate(t1)))

no_dup = extract_labeled(final_list,'soma_de_todos')

def train_test_split(data, split=0.70):
    train = list()
    train_size = split * len(data)
    dataset_copy = list(data)
    while len(train) < train_size:
        index = randrange(len(dataset_copy))
        train.append(dataset_copy.pop(index))
    return train, dataset_copy

train, teste = train_test_split(no_dup)

print(len(train),len(teste))

#Treino
with open('corpus_treino_70.txt', 'w',encoding="utf-8") as f:
    for item in train:
        f.write("%s\n" % item)
    f.close()

#Teste
with open('corpus_teste_30.txt', 'w',encoding="utf-8") as f:
    for item in teste:
        f.write("%s\n" % item)
    f.close()