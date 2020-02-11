from sklearn.model_selection import train_test_split
from data_main import X, y
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.svm import SVC
import pandas as pd
from sklearn.metrics import confusion_matrix,classification_report
from statsmodels.regression.linear_model import OLS




X=X.drop(["Ad Topic Line", "Timestamp"], axis=1) #i'll leave this for later...


column_transformer = ColumnTransformer([("city_trans", OneHotEncoder(), ["City"]),
                                        ("country_transformer", OneHotEncoder(), ["Country"])], remainder="passthrough")




encoded_cities = pd.get_dummies(X["City"], drop_first=True, dtype="int")
encoded_countries = pd.get_dummies(X["Country"], drop_first=True, dtype="int")
X=X.drop(["Country", "City"], axis=1)
X=pd.concat([X, encoded_cities, encoded_countries], axis=1)

def summary_OLS(X, y):
  scaler = StandardScaler().fit(X)
  X=scaler.transform(X)
  ols = OLS(y, X).fit()
  print(ols.summary())

#summary_OLS(X.iloc[:, 0:15], y)
#X = X.drop(["Daily Time Spent on Site", "Daily Internet Usage"], axis=1)
X= X.iloc[:,0:4] #i noticed that the P-Values on the Male column all the others were categorical variables were quite high
def classification():
  X_np=X.to_numpy()
  y_np=y.to_numpy()
  
  X_train, X_test, y_train, y_test = train_test_split(X_np, y_np, test_size=0.3)
  
  scaler = StandardScaler().fit(X_train)
  X_train = scaler.transform(X_train)
  X_test = scaler.transform(X_test)
  #X_sklearnencoding = column_transformer.fit_transform(X).toarray()
  
  classifier = SVC(kernel="linear", gamma="auto").fit(X_train, y_train)
  y_pred=classifier.predict(X_test)
  global cm
  cm = confusion_matrix(y_test, y_pred)
  print(classification_report(y_test, y_pred))
  
classification()

"""
FEATURE SCALING IS STILL NECESSARY, i was having a problem with the feature
scaling because i had a bunch of features with high P-Values
that i detected with the OLS summary!!!
"""