import pandas as pds
import matplotlib.pyplot as plt
import numpy as np

data = pds.read_csv("Dataset.csv")
data_np = data.to_numpy()
y=data.iloc[:, 9].to_numpy()
timespentonsite = data.iloc[:, 0].to_numpy()
ages = data.iloc[:, 1].to_numpy() 
areaIncome = data.iloc[:, 2] 
gender = data.iloc[:, 6].to_numpy()
males = np.where(gender==1)
females = np.where(gender==0)
clickers = data_np[np.where(y==1)]
notclickers = data_np[np.where(y==0)]

def chart_allTimeSpentOnSite():
  length = np.arange(len(timespentonsite))
  plt.bar(length, timespentonsite )
  plt.title("Time Spend on Website (seconds)")
  plt.show()

def chart_timeSpentVsAge():
  fig, ax = plt.subplots()
  scatter_x = ages
  scatter_y = timespentonsite
  legends={0:"Did not click ad",1:"Clicked Ad"}
  for g in np.unique(y): #pretty much converts y to set, presumably [0,1]
      i = np.where(y == g) #Picks indexes from y where value == g (0 or 1) ^
      ax.scatter(scatter_x[i], scatter_y[i], label=legends[g])
  ax.legend()
  plt.xlabel("Age")
  plt.ylabel("Time (seconds)")
  plt.title("Time x Age")
  plt.show()


def chart_areaIncomeVsClickedAd():
  plt.scatter(areaIncome, y)
  plt.title("Area Income vs Click Ad");
  plt.xlabel("Area Income")
  plt.ylabel("Clicked Ad")
  plt.show()


maleclickers = np.where(clickers[:,6]==1)
femaleclickers = np.where(clickers[:,6]==0)
  
def chart_clickersVsGender():
  plt.bar(["Male", "Female"], [len(maleclickers[0]), len(femaleclickers[0])])
  plt.title("Clickers by gender")
  plt.show()

malenotclickers = np.where(notclickers[:,6]==1)
femalenotclickers = np.where(notclickers[:,6]==0)
  
def chart_notClickersVsGender():
  plt.bar(["Male", "Female"], [len(malenotclickers[0]), len(femalenotclickers[0])])
  plt.title("Not clickers by gender")
  plt.show()

def chart_clickersVsGenders():
    fg,ax = plt.subplots()
    indexes = np.arange(2)
    barwidth = 0.3
    opacity= 0.8
    clickersbars = plt.bar(indexes,
                           [len(maleclickers[0]), len(femaleclickers[0])], 
                           alpha=opacity, 
                           width=barwidth, 
                           label="Did Click Ad")
    notclickersbars = plt.bar(indexes+barwidth,
                           [len(malenotclickers[0]), len(femalenotclickers[0])], 
                           alpha=opacity, 
                           width=barwidth, 
                           label="Did not click Ad")
    plt.title("Genders vs Clicked Ad")
    plt.legend()
    plt.xticks(indexes+barwidth/2, ["Male", "Female"])
    plt.tight_layout()
    plt.show()