# -*- coding: utf-8 -*-
"""trained model for rock mine predection.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1_EDKajgCcjBOe7xqAgV5HCZMjEEAVGfa

# **IMPORTING DEPENDENCIES**

---
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

"""# **LOADING DATAFRAME**

---


"""

dataframe = pd.read_csv("/content/drive/MyDrive/Copy of sonar data.csv",header=None)

dataframe.head()

"""# **checking and removing null value**

---


"""

dataframe.isnull().sum()

dataframe.groupby(60).mean()

"""# **SPLITING DATA AND LABELS**

---


"""

x=dataframe.drop(columns=60,axis=1)
y=dataframe[60]

print(x)

print(y)

"""# **SPLITING TRAIN AND TEST DATA**

---


"""

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.1,stratify=y,random_state=1)

print(x.shape)

print(x_test.shape)

print(x_train.shape)

"""# **LOADING TRAINING MODEL**

---


"""

model = LogisticRegression()

"""# **TRAINING THE MODEL**

---


"""

model.fit(x_train,y_train)

"""# **CALCULATING ACCURACY**

---


"""

# accuracy for train
xtrainpredict = model.predict(x_train)
xtrainaccu = accuracy_score(xtrainpredict,y_train)
print(xtrainaccu)

# accuracy for test
xtestpredict = model.predict(x_test)
xtestaccu = accuracy_score(xtestpredict,y_test)
print(xtestaccu)

"""# **MAKING PREDECTIVE SYSTEM**

---


"""

inputdata = (0.0272,0.0378,0.0488,0.0848,0.1127,0.1103,0.1349,0.2337,0.3113,0.3997,0.3941,0.3309,0.2926,0.1760,0.1739,0.2043,0.2088,0.2678,0.2434,0.1839,0.2802,0.6172,0.8015,0.8313,0.8440,0.8494,0.9168,1.0000,0.7896,0.5371,0.6472,0.6505,0.4959,0.2175,0.0990,0.0434,0.1708,0.1979,0.1880,0.1108,0.1702,0.0585,0.0638,0.1391,0.0638,0.0581,0.0641,0.1044,0.0732,0.0275,0.0146,0.0091,0.0045,0.0043,0.0043,0.0098,0.0054,0.0051,0.0065,0.0103)

# converting the collected data to numpy array
inputdata_np = np.asarray(inputdata)

# as we need only one value to be tested so reshaping it
inputdata_reshape = inputdata_np.reshape(1,-1)

# predecting the input data
predection = model.predict(inputdata_reshape)

# printting the predection
print("Rock") if predection[0] == 'R' else print("Mine")
