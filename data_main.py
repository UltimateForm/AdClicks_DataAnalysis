import pandas as pds
import matplotlib.pyplot as plt
import numpy as np

data = pds.read_csv("Dataset.csv")
y=data.iloc[:, 9].to_numpy()
timespentonsite = data.iloc[:, 0].to_numpy()
ages = data.iloc[:, 1].to_numpy() 

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
  areaIncome = data.iloc[:, 2]
  plt.scatter(areaIncome, y)
  plt.title("Area Income vs Click Ad");
  plt.xlabel("Area Income")
  plt.ylabel("Clicked Ad")
  plt.show()