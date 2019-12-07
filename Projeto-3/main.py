import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from IPython.display import display

#array composto com o nome de todos os atributos das selfies
names = ['photo','score','partial_faces','is_female','baby','child','teenager','youth','middle_age','senior','white','black','asian','oval_face','round_face','heart_face','smiling','mouth_open','frowning','wearing_glasses','wearing_sunglasses','wearing_lipstick','tongue_out','duck_face','black_hair','blond_hair','brown_hair','red_hair','curly_hair','straight_hair','braid_hair','showing_cellphone','using_earphone','using_mirror','braces','wearing_hat','harsh_lighting','dim_lighting']
#Lendo o arquivo txt, separando ele por espacos e colocando num dicionario com o nome de cada atributo
data = pd.read_csv('selfie_dataset.txt', header=None, sep = ' ', names= names)
keys = []
#pegando os atributos das selfies, sem contar o nome da foto nem a sua pontacao
for x in data.keys():
    if x != 'photo' and x != 'score':
        keys.append(x)

xset = []
#carregando matriz transposta para poder jogar no algoritmo de floresta randomica q necessariamente utiliza [n_samples, n_features]
for x in range(0, 46836):
    row = []
    for i in keys:
        row.append(data[i][x])
    xset.append(row)

#Carregando o modulo da floresta randomica com 100 arvores, utilizando bootstrap, setando um estado randomico unico para sempre dar os mesmos valores
#Nao foi utilizado a RandomForestClassifier porque ela nao aceita em seus parametros numeros float, entao foi utilizado a RandomForestRegressor
model = RandomForestRegressor(n_estimators= 100, bootstrap=True, max_features = names.__len__() -2, random_state=1)
#Fazendo o modulo da floresta randomica ser treinado pelos dados que foram dados
model.fit(xset , data['score'].astype(float))

#Criando uma tabela para que esta ordenado por grau de importancia
df = pd.DataFrame({'features': keys, 'importance': model.feature_importances_}).sort_values('importance', ascending= False)

#Mostrar a tabela no terminal
print("DataFrame:")
display(df)

#Criar um arquivo HTML que mostra a tabela no browser
print("Creating an html file with name (importancefeatures.html)")
f = open("importancefeatures.html", "w")
f.write(df.to_html())