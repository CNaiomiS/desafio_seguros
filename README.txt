Se entren� un clasificador que recibe como entrada los datos de un cliente y entrega una probabilidad que determinamos como el score de riesgo.
El clasificador fue entrenado y evaluado con la data entregada, la cual fue dividida en conjuntos de entrenamiento y testing para los fines correspondientes.
Se iter� el entrenamiento con el fin de minimizar el ratio de falsos positivos.

El clasificador sobre el conjunto de testing presenta un ratio de falsos positivos de 0.4, un recall de 0.78 y una precisi�n de 0.8.

Los c�digos adjuntos corresponden a:
neural_network_gen.ipynb : Notebook que contiene el detalle del preprocesamiento de la data, entrenamiento y evaluaci�n del clasificador.

score.py : C�digo en python con la funci�n calculate_score(x) que recibe los datos (x) de un cliente y entrega el score de riesgo.
* En este c�digo tambi�n queda por editar la funci�n transform(x) que seg�n cual sea el formato de entrada de x, ser� necesario transformarlo de acuerdo al formato de la entrada de la red neuronal. Se deja por editar por ser una prueba de concepto.