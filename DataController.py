import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
from imblearn.under_sampling import RandomUnderSampler

def SampleizeData(self):
    cardFraud = pd.read_csv("creditcard.csv")

    rus = RandomUnderSampler()
    
    X = cardFraud.drop("fraud",axis=1)
    y = cardFraud['fraud']
    
    for column in X.columns:
        X[column] = (X[column] - X[column].mean())/X[column].std()
    
    X_res, y_res = rus.fit_resample(X,y) # type: ignore
    
    return pd.concat([pd.DataFrame(X_res, columns=X.columns), pd.DataFrame(y_res, columns=['fraud'])], axis=1)

