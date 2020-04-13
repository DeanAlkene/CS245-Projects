import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
from sklearn.svm import SVC

def runSVM(X_train, X_test, y_train, y_test, C, kernel):
    model = SVC(C=C, kernel=kernel, gamma=0.001, verbose=False)
    model.fit(X_train, y_train)
    score = model.score(X_test, y_test)
    return score

def getBestParam(kernel):
    if kernel == 'rbf':
        C = 5.0
    elif kernel == 'linear':
        C = 0.002
    else:
        C = None
    return  C
