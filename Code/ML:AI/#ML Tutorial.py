#ML Tutorial

import sklearn 

from sklearn.datasets import load_breast_cancer

#load data

data = load_breast_cancer()

print(data)

#organise data

label_names = data['target_names']

labels = data['target']

feature_names = data['feature_names']

features = data['data']

#look at data

print(label_names)
print(labels[0])
print(feature_names[0])
print(features[0])