import keras
import pandas as pd
import numpy as np
from keras.models import Sequential
from keras.layers import Conv2D, MaxPooling2D, Activation, Dropout, Flatten, Dense
from keras import regularizers, optimizers
from keras_preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

#tamanho das imagens
img_width, img_height = 306, 306

#path do diretorio contendo as imagens
path = '../../../../Desktop/Selfie-dataset/'

path_Image = '../../../../Desktop/Selfie-dataset/images/'

#array composto com o nome de todos os atributos das selfies
names = ['photo','score','partial_faces','is_female','baby','child','teenager','youth','middle_age','senior','white','black','asian','oval_face','round_face','heart_face','smiling','mouth_open','frowning','wearing_glasses','wearing_sunglasses','wearing_lipstick','tongue_out','duck_face','black_hair','blond_hair','brown_hair','red_hair','curly_hair','straight_hair','braid_hair','showing_cellphone','using_earphone','using_mirror','braces','wearing_hat','harsh_lighting','dim_lighting']
#Lendo o arquivo txt, separando ele por espacos e colocando num dicionario com o nome de cada atributo
data = pd.read_csv(path+'selfie_dataset.txt', header=None, sep = ' ', names= names)

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

test_datagen = ImageDataGenerator(
    rescale= 1. /255
)

#aplicar a extensao da imagem
def append_ext(fn):
    return fn+".jpg"

#substituir o score pelas classes (boa, neutra, ruim)
def apply_class(fn):
    if fn > 4.7:
        return 'boa'
    elif fn > 3.5:
        return 'neutra'
    else:
        return 'ruim'

data['photo'] = data['photo'].apply(append_ext)
data['score'] = data['score'].apply(apply_class)

# separar 70% para treino, e 30% para validar
total = len(data)
number = float(total) * 0.7

train_set = {}
test_set = {}
#carregando matriz transposta para poder jogar no algoritmo de floresta randomica q necessariamente utiliza [n_samples, n_features]

for i in names:
    train_set[i] = data[i][0:int(number)]
    test_set[i] = data[i][int(number):]

#transformando os dicionarios em objetos imutaveis
df_train = pd.DataFrame(train_set)
df_test = pd.DataFrame(test_set)
    
#flow from dataframe
train_generator = train_datagen.flow_from_dataframe(dataframe=df_train , directory=path_Image ,x_col = 'photo', y_col= 'score', class_mode='categorical', target_size=(img_width, img_height), batch_size=32)

test_generator = test_datagen.flow_from_dataframe(dataframe=df_test , directory=path_Image ,x_col = 'photo', y_col= 'score', class_mode='categorical', target_size=(img_width, img_height), batch_size=32)

## Criar o modelo
model = Sequential()
model.add(Conv2D(32, (3, 3), padding='same', input_shape=(306,306,3)))
model.add(Activation('relu'))
model.add(Conv2D(32, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Conv2D(64, (3, 3), padding='same'))
model.add(Activation('relu'))
model.add(Conv2D(64, (3, 3)))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
model.add(Flatten())
model.add(Dense(512))
model.add(Activation('relu'))
model.add(Dropout(0.5))
model.add(Dense(3, activation='softmax'))
model.compile(optimizers.rmsprop(lr=0.0001, decay=1e-6),loss="categorical_crossentropy",metrics=["accuracy"])

model.summary()


#fitting model
STEP_SIZE_TRAIN=train_generator.n // train_generator.batch_size
STEP_SIZE_TEST=test_generator.n // test_generator.batch_size
model.fit_generator(generator=train_generator,
                    steps_per_epoch=STEP_SIZE_TRAIN,
                    validation_data=train_generator,
                    epochs=1
)

#checar valor
model.evaluate_generator(generator=train_generator,
steps=STEP_SIZE_TEST)

#fazer a predicao dos casos teste
test_generator.reset()
pred=model.predict_generator(test_generator,
steps=STEP_SIZE_TEST,
verbose=1)

predicted_class_indices=np.argmax(pred,axis=1)

labels = (test_generator.class_indices)
labels = dict((v,k) for k,v in labels.items())
predictions = [labels[k] for k in predicted_class_indices]

#salvar em um txt
filenames=test_generator.filenames
results=pd.DataFrame({"Filename":filenames,
                      "Predictions":predictions})
results.to_csv("results.csv",index=False)