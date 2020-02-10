import pandas as pds
import matplotlib.pyplot as plt
import numpy as np

data = pds.read_csv("Dataset.csv")
data_numpy = data.to_numpy()
X=data.drop(["Clicked on Ad"], axis=1)
y=data["Clicked on Ad"]
timespentonsite = data["Daily Time Spent on Site"].to_numpy()
ages = data["Age"].to_numpy() 
areaIncome = data["Area Income"]
gender = data["Male"].to_numpy()
males = np.where(gender==1)
females = np.where(gender==0)
clickers = data_numpy[np.where(y==1)]
notclickers = data_numpy[np.where(y==0)]
maleclickers = np.where(clickers[:,6]==1)
femaleclickers = np.where(clickers[:,6]==0)
malenotclickers = np.where(notclickers[:,6]==1)
femalenotclickers = np.where(notclickers[:,6]==0)