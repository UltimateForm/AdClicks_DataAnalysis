# AdClicks_DataAnalysis
messing around with dataset from https://www.kaggle.com/fayomi/advertising#advertising.csv

[classification report](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.classification_report.html):
|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| 0            | 0.97      | 0.98   | 0.98     | 103     |
| 1            | 0.98      | 0.97   | 0.97     | 97      |
|              |           |        |          |         |
| accuracy     |           |        | 0.97     | 200     |
| macro avg    | 0.98      | 0.97   | 0.97     | 200     |
| weighted avg | 0.98      | 0.97   | 0.97     | 200     |


~~without scaling...which is strange or lucky...~~

~~ah, found it, scaling dilenma: https://stats.stackexchange.com/questions/172795/scaling-for-svm-destroys-my-results~~

although true, in my case it was simply a case of features with high P Values and low coefficients polluting the model, after removing them: feature scaling no longer decreased the scores, it increased them!
