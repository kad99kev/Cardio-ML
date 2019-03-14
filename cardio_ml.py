import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)


# Importing dataset
dataset = pd.read_csv('cardio_train.csv', sep = ';')


#Modifying the dataset
dataset['years'] = (dataset['age']/360).round().astype(int)

dataset.drop(['id'], axis = 1, inplace = True)

dataset.drop(dataset[(dataset['height'] > dataset['height'].quantile(0.975)) | (dataset['height'] < dataset['height'].quantile(0.025)) ].index,inplace=True)
dataset.drop(dataset[(dataset['weight'] > dataset['weight'].quantile(0.975)) | (dataset['weight'] < dataset['weight'].quantile(0.025)) ].index,inplace=True)

dataset.drop(dataset[(dataset['ap_hi'] > dataset['ap_hi'].quantile( 0.975)) | (dataset['ap_hi'] < dataset['ap_hi'].quantile(0.025))].index,inplace=True)
dataset.drop(dataset[(dataset['ap_lo'] > dataset['ap_lo'].quantile( 0.975)) | (dataset['ap_lo'] < dataset['ap_lo'].quantile(0.025))].index,inplace=True)

X = dataset.drop(['age', 'cardio'], axis = 1)
y = dataset.iloc[:, -2]


#Splitting
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)


#Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)


#Fitting the model
from sklearn.linear_model import LogisticRegression
lr_clf = LogisticRegression(random_state = 0, solver = 'liblinear', multi_class = 'ovr')
lr_clf.fit(X_train, y_train)

def predict(data):
    data = sc_X.transform(data)
    lr_pred = lr_clf.predict_proba(data)[:, 1]
    return(round(lr_pred[0]*100, 4))
