import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score, recall_score, precision_score, f1_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.datasets import make_classification

dataset_url = "https://raw.githubusercontent.com/Nauvaldi/Dataset/main/credit_score.csv"
dataset = pd.read_csv(dataset_url)


data = dataset.drop(columns=['kpr_aktif', 'rata_rata_overdue'])

#Pre processing dengan get dummies panda
data_kpr = dataset[['kpr_aktif']]
data_rata = dataset[['rata_rata_overdue']]
kpr = pd.get_dummies(data_kpr)
rata_rata = pd.get_dummies(data_rata)

dataOlah = pd.concat([kpr,rata_rata],axis=1)

dataHasil = pd.concat([data,dataOlah], axis=1)


"""Normalisasi Data"""

datakelas = dataHasil['risk_rating']
data = dataHasil.drop(columns=['kode_kontrak','risk_rating'])


# scale features
scaler = MinMaxScaler()
model =scaler.fit(data)
scaled_data=model.transform(data)
# print scaled features
print(scaled_data)

namakolom = data.columns.values
dataMinMax = pd.DataFrame(scaled_data, columns=namakolom)
label = ['Unnamed: 0']
dataMinMax= dataMinMax.drop(columns = label)

dataMinMax

# Z Score atau StandardScaler
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
model = (scaler.fit(data))
data_mean = (scaler.mean_)
scale_data = (scaler.transform(data))
print(scale_data)

dataZScale = pd.DataFrame(scale_data, columns=data.columns.values)
dataZScale

datakelas = dataHasil['risk_rating']
data = pd.concat([datakelas,dataMinMax],axis=1)
data