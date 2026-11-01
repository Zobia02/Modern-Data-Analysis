from sklearn.decomposition import PCA
import scipy as sp
import numpy as np
import matplotlib.pyplot as plt

def load_data():
    data = sp.io.loadmat('dataset1.mat')
    set1 = data['set1a']
    set2 = data['set1b'] @ np.array([[1.4, 0.4], [0.1, 1.4]])
    return set1, set2

if __name__ == '__main__':
    set1, set2 = load_data()
    # Your code here
