from sklearn.model_selection import train_test_split
from data_main import X, y
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.svm import SVC
import pandas as pd
from sklearn.metrics import confusion_matrix,classification_report

X=X.drop(["Ad Topic Line", "Timestamp"], axis=1) #i'll leave this for later...
column_transformer = ColumnTransformer([("city_trans", OneHotEncoder(), ["City"]),
                                        ("country_transformer", OneHotEncoder(), ["Country"])], remainder="passthrough")

encoded_cities = pd.get_dummies(X["City"], drop_first=True, dtype="int")
encoded_countries = pd.get_dummies(X["Country"], drop_first=True, dtype="int")
X=X.drop(["Country", "City"], axis=1)
X=pd.concat([X, encoded_cities, encoded_countries], axis=1)
X=X.to_numpy()
y=y.to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

"""scaler = StandardScaler().fit(X_train)
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)"""
#X_sklearnencoding = column_transformer.fit_transform(X).toarray()

classifier = SVC(kernel="linear", gamma="auto").fit(X_train, y_train)
y_pred=classifier.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(classification_report(y_test, y_pred))