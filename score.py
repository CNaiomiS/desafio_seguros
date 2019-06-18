import pickle
from sklearn.neural_network import MLPClassifier

def load_model(self): #cargar el modelo guardado
	filename = 'arn.sav'
	neural_network = pickle.load(open(filename, 'rb'))
	return neural_network

def transform(x):
	#dependiendo del formato del x entregado, será necesario transformarlo al formato de entrada de la red neuronal
	return x
	
def calculate_score(x): #entregar un score para los datos x de un cliente
	x = transform(x)
	neural_network = load_model()
	return neural_network.predict_proba(x)[0][0] #se entrega solo la probabilidad de que sea malo, pues representa la probabilidad de riesgo


