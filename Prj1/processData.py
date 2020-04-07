import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score

X_file_name = "Animals_with_Attributes2/Features/ResNet101/AwA2-features.txt"
y_file_name = "Animals_with_Attributes2/Features/ResNet101/AwA2-labels.txt"
col_name = ['feature' + str(i) for i in range(2048)]

def divideData(size='full'):
    if size == 'full':
        X_data = pd.read_csv(X_file_name, sep=' ', names=col_name)
        y_data = pd.read_csv(y_file_name, names=['label'])
    else:
        X_data = pd.read_csv(X_file_name, sep=' ', nrows=2000, names=col_name)
        y_data = pd.read_csv(y_file_name, nrows=2000, names=['label'])
    X_train, X_test, y_train, y_test = train_test_split(X_data, y_data, test_size=0.4)
    np.save('X_train', X_train)
    np.save('X_test', X_test)
    np.save('y_train', y_train)
    np.save('y_test', y_test)

def loadDataDivided():
    X_train = np.load('X_train.npy')
    X_test = np.load('X_test.npy')
    y_train = np.load('y_train.npy')
    y_test = np.load('y_test.npy')
    return X_train, X_test, y_train, y_test

def loadData(size='full'):
    if size == 'full':
        X_data = pd.read_csv(X_file_name, sep=' ', names=col_name)
        y_data = pd.read_csv(y_file_name, names=['label'])
    else:
        X_data = pd.read_csv(X_file_name, sep=' ', nrows=2000, names=col_name)
        y_data = pd.read_csv(y_file_name, nrows=2000, names=['label'])
    return X_data, y_data

if __name__ == '__main__':
    divideData('full')

