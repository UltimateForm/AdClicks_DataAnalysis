import matplotlib.pyplot as plt
import numpy as np
from data_main import data,timespentonsite, areaIncome, ages, y, maleclickers, femaleclickers, malenotclickers, femalenotclickers
import seaborn as sns

##I REALLY DONT NEED TO BE DOING ALL THIS SINCE THERE ARE EASIER WAYS
##BUT I WANNA FCK WITH PYPLOTLIB

y_numpy = y.to_numpy()
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
  for g in np.unique(y_numpy): #pretty much converts y to set, presumably [0,1]
      i = np.where(y_numpy == g) #Picks indexes from y where value == g (0 or 1) ^
      ax.scatter(scatter_x[i], scatter_y[i], label=legends[g])
  ax.legend()
  plt.xlabel("Age")
  plt.ylabel("Time (seconds)")
  plt.title("Time x Age")
  plt.show()


def chart_areaIncomeVsClickedAd():
  plt.scatter(areaIncome, y_numpy)
  plt.title("Area Income vs Click Ad");
  plt.xlabel("Area Income")
  plt.ylabel("Clicked Ad")
  plt.show()

  
def chart_clickersVsGender():
  plt.bar(["Male", "Female"], [len(maleclickers[0]), len(femaleclickers[0])])
  plt.title("Clickers by gender")
  plt.show()

  
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
    
sns.pairplot(data, hue = 'Clicked on Ad', vars = 
             ['Daily Time Spent on Site', 'Age', 'Area Income', 'Daily Internet Usage'], 
             palette = 'husl')