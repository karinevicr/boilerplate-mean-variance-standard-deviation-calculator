import numpy as np

# Função calculate que recebe uma lista de 9 números e retorna um dicionário 
# contendo a média, variância, desvio padrão, máximo, mínimo e soma dos 
# elementos da lista.

def calculate(list_input):
    if len(list_input) != 9:
        raise ValueError("List must contain nine numbers.")
    
#Armazena a lista no array de 3x3
    array = np.array(list_input).reshape(3, 3)
    
# Faz o calculo da média, variância, desvio padrão, 
# máximo, mínimo e soma dos elementos do main.py.
    calculations = {
        'mean': [np.mean(array, axis=0).tolist(), np.mean(array, axis=1).tolist(), np.mean(array).tolist()],
        'variance': [np.var(array, axis=0).tolist(), np.var(array, axis=1).tolist(), np.var(array).tolist()],
        'standard deviation': [np.std(array, axis=0).tolist(), np.std(array, axis=1).tolist(), np.std(array).tolist()],
        'max': [np.max(array, axis=0).tolist(), np.max(array, axis=1).tolist(), np.max(array).tolist()],
        'min': [np.min(array, axis=0).tolist(), np.min(array, axis=1).tolist(), np.min(array).tolist()],
        'sum': [np.sum(array, axis=0).tolist(), np.sum(array, axis=1).tolist(), np.sum(array).tolist()]
    }
    
    return calculations
