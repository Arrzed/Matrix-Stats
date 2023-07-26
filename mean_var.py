import numpy as np

def calculate(x):
    if len(x) != 9:
        raise ValueError('List must contain nine numbers ')
    matrix = np.reshape(x,(3,3))
    mean = list(np.mean(matrix, axis=0)),list(np.mean(matrix, axis=1)),np.mean(matrix)
    var = list(np.var(matrix, axis=0)),list(np.var(matrix, axis=1)),np.var(matrix)
    std_dev = list(np.std(matrix, axis=0)),list(np.std(matrix, axis=1)),np.std(matrix)
    maximum = list(np.max(matrix, axis=0)),list(np.max(matrix, axis=1)),np.max(matrix)
    minimum = list(np.min(matrix, axis=0)),list(np.min(matrix, axis=1)),np.min(matrix)
    add = list(np.sum(matrix, axis=0)),list(np.sum(matrix, axis=1)),np.sum(matrix)
    
    calculations = {'mean': list(mean),
                    'variance': list(var),
                    'standard deviation': list(std_dev),
                    'max': list(maximum),
                    'min': list(minimum),
                    'sum': list(add)}

    return calculations

calculate([2,6,2,8,4,0,1,])
