print("""
# to suppress warnings 
from warnings import filterwarnings
filterwarnings('ignore')

import pandas as pd
# display all columns of the dataframe
pd.options.display.max_columns = None

# display all rows of the dataframe
pd.options.display.max_rows = None

# to display the float values upto 6 decimal places     
pd.options.display.float_format = '{:.6f}'.format

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
%matplotlib inline
plt.style.use('ggplot')

import numpy as np
from numpy import mean, std, sqrt

import pickle
import pylab as plb
import seaborn as sns

import sklearn
from sklearn import metrics
import sklearn.metrics as sm
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import mean_squared_error 
from sklearn.metrics import roc_curve
from sklearn.metrics import roc_auc_score
from sklearn.metrics import recall_score
from sklearn import datasets
from sklearn import model_selection
from sklearn.model_selection import train_test_split 
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import make_classification
from sklearn.datasets import make_blobs
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler 
from sklearn import neighbors
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.svm import SVC
from sklearn.ensemble import StackingClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import VotingClassifier 

from scipy.stats import zscore

from imblearn.over_sampling import SMOTE
from imblearn.under_sampling import NearMiss

import os
import statsmodels.api as sm
import admission_prediction as model
from flask import Flask, request
import json

import pydotplus
from IPython.display import Image  

import graphviz
import random

import xgboost as xgb

# import function to perform feature selection
from sklearn.feature_selection import RFE

#----------------------------------------------------------------------------------------------------------------------

### Adaboost
os.chdir("/home/sunil/Desktop/ML/SG-AdvancedML")
dataframe = pandas.read_csv("diabetes.csv")
array = dataframe.values

X = array[:,0:8]
Y = array[:,8]
seed = 7

# AdaBoost Classification

seed = 7
num_trees = 30
kfold = model_selection.KFold(n_splits=10, random_state=seed)
model = AdaBoostClassifier(n_estimators=num_trees, random_state=seed)
results = model_selection.cross_val_score(model, X, Y, cv=kfold)
print(results.mean())


#----------------------------------------------------------------------------------------------------------------------
### BaggedDecisionTrees
X = array[:,0:8]
Y = array[:,8]
seed = 7
kfold = model_selection.KFold(n_splits=10)
cart = DecisionTreeClassifier()
num_trees = 100
model = BaggingClassifier(base_estimator=cart, n_estimators=num_trees, random_state=seed)
results = model_selection.cross_val_score(model, X, Y, cv=kfold)
print(results.mean())


#----------------------------------------------------------------------------------------------------------------------
###admission_prediction

#Load Model
with open('admission.pickle','rb') as file:
    model = pickle.load(file)

#Load Scaler object
with open('scaler.pickle','rb') as file:
    X_scaler = pickle.load(file)
    

#Preprocessing function

def normalize_data(GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research):
    
    #Normalize data - continuos featurs
    num_scaled = X_scaler.transform([[GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA]])
    
    #Concatenate Research 
    num_scaled =  np.append(num_scaled[0],Research)
    
    return num_scaled

normalize_data(337,118,4,4.5,4.5,9.65,1)

#Prediction Function
def predict_admission(GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research):
    
    scaled_data = normalize_data(GRE_Score, TOEFL_Score, University_Rating, SOP, LOR, CGPA, Research)
    prediction = model.predict([scaled_data])
    
    if prediction > 0.5:
        result = 'Admission'
    else:
        result = 'No Admission'
    
    return result

if __name__== '__main__':
    result = predict_admission(337,118,4,4.5,4.5,9.65,1)
    print(result)

#----------------------------------------------------------------------------------------------------------------------

### admission_web_service
#Build a Web Service using Flask
app = Flask(__name__)
@app.route('/predict', methods=['GET','POST']) #www.xyz.com/translate
def admission(): 
    
    try:
        #Get Input fields
        gre_score = float(request.form['gre_score'])  
        toefel_score = float(request.form['toefel_score']) 
        university_rating = float(request.form['university_rating']) 
        sop = float(request.form['sop'])
        lor = float(request.form['lor']) 
        cgpa = float(request.form['cgpa']) 
        research = float(request.form['research'])
    
    except:
        return 'Invalid data sent. Please send data in required format.'
    
    return model.predict_admission(gre_score, toefel_score, university_rating, sop, lor, cgpa, research)

#Start the Service
if __name__ == '__main__':
    #Start http server locally on port 5000
    app.run(host='0.0.0.0')


#----------------------------------------------------------------------------------------------------------------------
### iris classification with KNN

# import some data to play with
iris=datasets.load_iris()
iris.feature_names
iris.target
iris.target_names

linnerud=datasets.load_wine()
linnerud.feature_names

# Store the inputs as a Pandas Dataframe and set the column names
x = pd.DataFrame(iris.data)
x.columns = ['Sepal_Length','Sepal_Width','Petal_Length','Petal_Width']

y = pd.DataFrame(iris.target)
y.columns = ['Targets']

y.shape
x.shape


X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.20) 

 
scaler = StandardScaler()  
scaler.fit(X_train)

X_train = scaler.transform(X_train)  
X_test = scaler.transform(X_test)  

classifier = KNeighborsClassifier(n_neighbors=5)  
classifier.fit(X_train, y_train) 
y_pred = classifier.predict(X_test)  
type(y_pred1)

df_c = pd.concat([y_pred1.reset_index(drop=True), y_test.reset_index(drop=True)], axis=1)

confusion_matrix(y_test, y_pred)
classification_report(y_test, y_pred)
accuracy_score(y_test, y_pred)

y_test_np=np.asarray(y_test)


import warnings
warnings.filterwarnings("ignore")

error = []

# Calculating error for K values between 1 and 40
for i in range(1, 40):  
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    pred_i = knn.predict(X_test)
    iter_acc=accuracy_score(y_test,pred_i)*100
    iter_err=round(float(100.0-(iter_acc.astype(float))),2)
    error.append(iter_err)
    
plt.figure(figsize=(12, 6))  
plt.plot(range(1, 40), error, color='red', linestyle='dashed', marker='o',  
         markerfacecolor='blue', markersize=10)
plt.title('Error Rate K Value')  
plt.xlabel('K Value')  
plt.ylabel('Mean Error') 


classifier1 = KNeighborsClassifier(n_neighbors=2)  
classifier1.fit(X_train, y_train) 
y_pred1 = classifier1.predict(X_test)

print(confusion_matrix(y_test, y_pred1))  
print(classification_report(y_test, y_pred1))  
print(accuracy_score(y_test, y_pred1))



#----------------------------------------------------------------------------------------------------------------------
### bank_marketing_New

#Loading the Dataset
df = pd.read_csv('banking_updated.csv')
df.head()
df.describe().T
df.isnull().sum()

#Feature Engineering
df.drop(['duration','contact','month','day_of_week','default','pdays',],axis=1,inplace=True)
df.replace(['basic.6y','basic.4y', 'basic.9y'], 'basic', inplace=True)

#Visualizing the Data
sns.countplot(x='y', data=df)
sns.countplot(y='job', data=df)
sns.countplot(x='marital', data=df)
df.education.value_counts()
sns.countplot(y='education', data=df)

# Pre Processing
le = preprocessing.LabelEncoder()
df.job = le.fit_transform(df.job)
df.marital = le.fit_transform(df.marital)
df.education = le.fit_transform(df.education)
df.housing = le.fit_transform(df.housing)
df.loan = le.fit_transform(df.loan)
df.poutcome = le.fit_transform(df.poutcome)

X = df.iloc[:,0:14]
X[0:10]

y = df.iloc[:,14]
y[0:10]

#Train and Test split
x_train, x_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2, random_state=0) #80/20 split
min_max_scaler = preprocessing.MinMaxScaler()
X_train_minmax = min_max_scaler.fit_transform(x_train)
X_train_minmax
x_train.shape, y_train.shape
x_test.shape, y_test.shape

#training the model
#Logistics Regression

model=LogisticRegression()
model.fit(x_train, y_train)
prediction=model.predict(x_test)


accuracy_score(y_test, prediction)
confusion_matrix(y_test, prediction)

# We will make use of different classification algorithms to train this data set and will record the accuracy on test set.
parameters = {
    'penalty' : ['l1','l2'], 
    'C'       : np.logspace(-3,3,7),
    'solver'  : ['newton-cg', 'lbfgs', 'liblinear'],
}
clf = GridSearchCV(model,param_grid = parameters, cv=10)
kfold = model_selection.KFold(n_splits=10)
model=LogisticRegression()
results = model_selection.cross_val_score(model, X_train_minmax, y_train, cv=kfold)
results.mean()


x, y = make_blobs(n_samples=50, n_features=2, cluster_std=5.0,
                  centers=[(0,0), (2,2)], shuffle=False, random_state=12)

model.fit(X_train_minmax, y_train)
prediction=model.predict(x_test)

accuracy_score(y_test, prediction)

confusion_matrix(y_test, prediction)



#----------------------------------------------------------------------------------------------------------------------
###bootstraping

# scikit-learn bootstrap
from sklearn.utils import resample
# data sample
data = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]

# prepare bootstrap sample
boot = resample(data, replace=True, n_samples=4, random_state=1)
print('Bootstrap Sample: %s' % boot)

# out of bag observations
oob = [x for x in data if x not in boot]
print('OOB Sample: %s' % oob)

# prepare bootstrap sample
boot = resample(data, replace=True, n_samples=3, random_state=1)
print('Bootstrap Sample: %s' % boot)

# prepare bootstrap sample
boot = resample(data, replace=True, n_samples=6, random_state=1)
print('Bootstrap Sample: %s' % boot)

#----------------------------------------------------------------------------------------------------------------------
### comparison

# compare standalone models for binary classification
#Read the data
data = pd.read_csv("stack.csv")
##segregate X & y
X = data.iloc[:,:25].values
y = data.iloc[:,25].values
print(type(X),X.shape)
print(type(y),y.shape)

# train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X,  y,  test_size = 0.20,  random_state = 42) 

# get a list of models to evaluate
def get_models():
    models = dict()
    models['lr'] = LogisticRegression()
    models['knn'] = KNeighborsClassifier()
    models['cart'] = DecisionTreeClassifier()
    models['bayes'] = GaussianNB()
    return models

# evaluate a given model using cross-validation
def evaluate_model(model, X, y):
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
    return scores

## Comparison among different classifiers
# get the dataset
def get_dataset():
    ##Read the data
    data = pd.read_csv("stack.csv")
    ##segregate X & y
    X = data.iloc[:,:25].values
    y = data.iloc[:,25].values
    return X, y


# get a list of models to evaluate
def get_models():
    models = dict()
    models['lr'] = LogisticRegression()
    models['knn'] = KNeighborsClassifier()
    models['cart'] = DecisionTreeClassifier()
    models['bayes'] = GaussianNB()
    return models
 
# evaluate a given model using cross-validation
def evaluate_model(model, X, y):
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
    return scores
 
# define dataset
X, y = get_dataset()
# get the models to evaluate
models = get_models()
# evaluate the models and store results
results, names = list(), list()
for name, model in models.items():
    scores = evaluate_model(model, X_train, y_train)
    results.append(scores)
    names.append(name)
    print('>%s %.3f (%.3f)' % (name, mean(scores), std(scores)))
# plot model performance for comparison
pyplot.boxplot(results, labels=names, showmeans=True)
pyplot.show()
# get the dataset
# get the dataset
def get_dataset():
    ##Read the data
    data = pd.read_csv("stack.csv")
    ##segregate X & y
    X = data.iloc[:,:25].values
    y = data.iloc[:,25].values
    return X, y


# get a list of models to evaluate
def get_models():
    models = dict()
    models['lr'] = LogisticRegression()
    models['knn'] = KNeighborsClassifier()
    models['cart'] = DecisionTreeClassifier()
    models['bayes'] = GaussianNB()
    return models
 
# evaluate a given model using cross-validation
def evaluate_model(model, X, y):
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
    return scores
 
# define dataset
X, y = get_dataset()
# get the models to evaluate
models = get_models()
# evaluate the models and store results
results, names = list(), list()
for name, model in models.items():
    scores = evaluate_model(model, X_train, y_train)
    results.append(scores)
    names.append(name)
    print('>%s %.3f (%.3f)' % (name, mean(scores), std(scores)))
# plot model performance for comparison
pyplot.boxplot(results, labels=names, showmeans=True)
pyplot.show()

# get a stacking ensemble of models
def get_stacking():
    # define the base models
    level0 = list()
    level0.append(('lr', LogisticRegression()))
    level0.append(('knn', KNeighborsClassifier()))
    level0.append(('cart', DecisionTreeClassifier()))
    level0.append(('bayes', GaussianNB()))
    # define meta learner model
    level1 = LogisticRegression()
    # define the stacking ensemble
    model = StackingClassifier(estimators=level0, final_estimator=level1, cv=5)
    return model

# get a list of models to evaluate
def get_models():
    models = dict()
    models['lr'] = LogisticRegression()
    models['knn'] = KNeighborsClassifier()
    models['cart'] = DecisionTreeClassifier()
    models['bayes'] = GaussianNB()
    models['stacking'] = get_stacking()
    return models

## Compare different classifiers with stacking
 
# get the dataset
def get_dataset():
    ##Read the data
    data = pd.read_csv("stack.csv")
    ##segregate X & y
    X = data.iloc[:,:25].values
    y = data.iloc[:,25].values
    return X, y
 
# get a stacking ensemble of models
def get_stacking():
    # define the base models
    level0 = list()
    level0.append(('lr', LogisticRegression()))
    level0.append(('knn', KNeighborsClassifier()))
    level0.append(('cart', DecisionTreeClassifier()))
    level0.append(('bayes', GaussianNB()))
    # define meta learner model
    level1 = LogisticRegression()
    # define the stacking ensemble
    model = StackingClassifier(estimators=level0, final_estimator=level1, cv=5)
    return model
 
# get a list of models to evaluate
def get_models():
    models = dict()
    models['lr'] = LogisticRegression()
    models['knn'] = KNeighborsClassifier()
    models['cart'] = DecisionTreeClassifier()
    models['bayes'] = GaussianNB()
    models['stacking'] = get_stacking()
    return models
 
# evaluate a give model using cross-validation
def evaluate_model(model, X, y):
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
    return scores

# define dataset
X, y = get_dataset()
# get the models to evaluate
models = get_models()
# evaluate the models and store results
results, names = list(), list()
for name, model in models.items():
    scores = evaluate_model(model, X_train, y_train)
    results.append(scores)
    names.append(name)
    print('>%s %.3f (%.3f)' % (name, mean(scores), std(scores)))
# plot model performance for comparison
pyplot.boxplot(results, labels=names, showmeans=True)
pyplot.show()


#Prediction
# make a prediction with a stacking ensemble


# get the dataset
def get_dataset():
    ##Read the data
    data = pd.read_csv("stack.csv")
    ##segregate X & y
    X = data.iloc[:,:25].values
    y = data.iloc[:,25].values
    return X, y
 
# get a stacking ensemble of models
def get_stacking():
    # define the base models
    level0 = list()
    level0.append(('lr', LogisticRegression()))
    level0.append(('knn', KNeighborsClassifier()))
    level0.append(('cart', DecisionTreeClassifier()))
    level0.append(('bayes', GaussianNB()))
    # define meta learner model
    level1 = LogisticRegression()
    # define the stacking ensemble
    model = StackingClassifier(estimators=level0, final_estimator=level1, cv=5)
    return model
 
# get a list of models to evaluate
def get_models():
    models = dict()
    models['lr'] = LogisticRegression()
    models['knn'] = KNeighborsClassifier()
    models['cart'] = DecisionTreeClassifier()
    models['bayes'] = GaussianNB()
    models['stacking'] = get_stacking()
    return models

def accuracy_model(model):
    model.fit(X_train,y_train)
    yhat = model.predict(X_test)
    score = accuracy_score(y_test, yhat)
    return score

results = []
names = []

## Model test accuracy
for name, model in models.items():
    scores = accuracy_model(model)
    results.append(scores)
    names.append(name)

dashboard = pd.DataFrame(results,names)
print(dashboard)  

#----------------------------------------------------------------------------------------------------------------------
### KNNRegression


os.chdir('C:/Users/haris/OneDrive/Desktop/GreatLearning/MachineLearning2/Day1_Classroom/KNN/KNN Regression')

df = pd.read_csv('train.csv')
df.head()
df.isnull().sum()
#missing values in Item_weight and Outlet_size needs to be imputed
mean = df['Item_Weight'].mean() #imputing item_weight with mean
df['Item_Weight'].fillna(mean, inplace =True)

mode = df['Outlet_Size'].mode() #imputing outlet size with mode
df['Outlet_Size'].fillna(mode[0], inplace =True)

df.drop(['Item_Identifier', 'Outlet_Identifier'], axis=1, inplace=True)
df = pd.get_dummies(df)

df.head()

from sklearn.model_selection import train_test_split
train , test = train_test_split(df, test_size = 0.3)

x_train = train.drop('Item_Outlet_Sales', axis=1)
y_train = train['Item_Outlet_Sales']

x_test = test.drop('Item_Outlet_Sales', axis = 1)
y_test = test['Item_Outlet_Sales']

sns.heatmap(data=x_train.corr())

df.columns


scaler = MinMaxScaler(feature_range=(0, 1))

x_train_scaled = scaler.fit_transform(x_train)
x_train = pd.DataFrame(x_train_scaled)

x_test_scaled = scaler.fit_transform(x_test)
x_test = pd.DataFrame(x_test_scaled)

rmse_val = [] #to store rmse values for different k
for K in range(20):
    K = K+1
    model = neighbors.KNeighborsRegressor(n_neighbors = K)

    model.fit(x_train, y_train)  #fit the model
    pred=model.predict(x_test) #make prediction on test set
    error = sqrt(mean_squared_error(y_test,pred)) #calculate rmse
    rmse_val.append(error) #store rmse values
    print('RMSE value for k= ' , K , 'is:', error)
    
#plotting the rmse values against k values
curve = pd.DataFrame(rmse_val) #elbow curve 
curve.plot()

finalmodel = neighbors.KNeighborsRegressor(n_neighbors = 9)

#----------------------------------------------------------------------------------------------------------------------
### KNN+Breast+Cancer+Modeling+29
NNH = KNeighborsClassifier(n_neighbors= 5 , weights = 'distance' )
bc_df = pd.read_csv("wisc_bc_data.csv")
bc_df.shape
bc_df.dtypes
bc_df['diagnosis'] = bc_df.diagnosis.astype('category')
bc_df.describe().transpose()

# Class distribution among B and M is almost 2:1. The model will better predict B and M
bc_df.groupby(["diagnosis"]).count()

# The first column is id column which is patient id and nothing to do with the model attriibutes. So drop it.
bc_df = bc_df.drop(labels = "id", axis = 1)

# Create a separate dataframe consisting only of the features i.e independent attributes
bc_feature_df = bc_df.drop(labels= "diagnosis" , axis = 1)
bc_feature_df.head()

# convert the features into z scores as we do not know what units / scales were used and store them in new dataframe
# It is always adviced to scale numeric attributes in models that calculate distances.
bc_feature_df_z = bc_feature_df.apply(zscore)  # convert all attributes to Z scale 
bc_feature_df_z.describe()

# Capture the class values from the 'diagnosis' column into a pandas series akin to array 
bc_labels = bc_df["diagnosis"]

# store the bc_labels data into a separate np array
y = np.array(bc_labels)
y.shape

# Split X and y into training and test set in 75:25 ratio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=1)

# Call Nearest Neighbour algorithm
NNH.fit(X_train, y_train)

# For every test data point, predict it's label based on 5 nearest neighbours in this model. The majority class will 
# be assigned to the test data point
predicted_labels = NNH.predict(X_test)
NNH.score(X_test, y_test)

# calculate accuracy measures and confusion matrix
print(metrics.confusion_matrix(y_test, predicted_labels))
# Let us analyze the different attributes for distribution and the correlation by using scatter matrix
sns.pairplot(bc_df)

# As is evident from the scatter matrix, many dimensions have strong correlation and that is not surprising
# Area and Perimeter are function of radius, so they will have strong correlation. Why take multiple dimensions 
# when they convey the same information to the model?

# To to drop dependent columns from bc_df
bc_features_pruned_df_z =  bc_feature_df_z.drop(['radius_mean'], axis=1)

X = np.array(bc_features_pruned_df_z)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=1)

# Call Nearest Neighbour algorithm
NNH.fit(X_train, y_train)

# For every test data point, predict it's label based on 5 nearest neighbours in this model. The majority class will 
# be assigned to the test data point
predicted_labels = NNH.predict(X_test)

# get the accuracy score which is how many test cases were correctly predicted as a ratio of total number of test cases
NNH.score(X_test, y_test)

# calculate accuracy measures and confusion matrix
print(metrics.confusion_matrix(y_test, predicted_labels))

# peformance has dropped! So, be careful about the dimensions you drop. 
#Domain expertise is a must to know whether dropping radius or dropping area
#will be better. The area may be a stronger predictor than radius and the
#way they are calculated under a electron microscope may be effecting the outcome



#----------------------------------------------------------------------------------------------------------------------
### KNN - In-Class - Lab Exercise (Session 3) - Question
# 1. Load Data
plt.rcParams['figure.figsize'] = [15,8]
# load the csv file
df = pd.read_csv('bank.csv')
df.boxplot()

# 2. Separate the dependent and the independent variables. Also, in the target variable, replace yes with 0 and no with 1.
Q1=df.quantile(0.25)
Q3=df.quantile(0.75)
IQR=Q3-Q1
df_final=df[~((df<(Q1-1.5*IQR)) | (df>(Q3+1.5*IQR)))].
df_final.boxplot()

# 3. Replace the value "unknown" from each column with NaN.
df_final.replace(to_replace='unknown',value=np.NaN,inplace=True);

# 4. Look for the null values and treat the null values.
df_final.isnull().sum()
df_final.dropna(inplace=True)
df_final.isnull().sum()

# 5. Remove the unnecessary variables that will not contribute to the model.
df_final.shape[0]/df.shape[0]*100

# 6. Plot the distribution of all the numeric variables and find the value of skewness for each variable
df_final.hist()
df_final.skew()

#7. Plot the distribution of the target variable.
df_final[["y"]].hist()

# 8. Scale all the numeric variables using standard scalar.
df_num = df_final.select_dtypes(include = [np.number]).drop('y', axis=1)
df_num.columns
X_scaler = StandardScaler()

num_scaled = X_scaler.fit_transform(df_num)
df_num_scaled = pd.DataFrame(num_scaled, columns = df_num.columns)

df_cat = df_final.select_dtypes(include = [np.object])
df_cat.columns

X = pd.concat([df_num_scaled, df_cat], axis = 1).dropna()
X.head()
y=df_final[["y"]]

## K Nearest Neighbors (KNN)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=100)

print('X_train', X_train.shape)
print('y_train', y_train.shape)
print('X_test', X_test.shape)
print('y_test', y_test.shape)

# 9. Create a function to draw a confusion matrix (heatmap) and a function to plot a roc-auc curve

def plot_confusion_matrix(model):
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    conf_matrix = pd.DataFrame(data = cm,columns = ['Predicted:0','Predicted:1'], index = ['Actual:0','Actual:1'])
    sns.heatmap(conf_matrix, annot = True, fmt = 'd', cmap = ListedColormap(['lightskyblue']), cbar = False, 
                linewidths = 0.1, annot_kws = {'size':25})
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.show()

def plot_roc(model):
    y_pred_prob = model.predict_proba(X_test)[:,1]
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
    plt.plot(fpr, tpr)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.plot([0, 1], [0, 1],'r--')
    plt.title('ROC curve for Term Deposit Classifier', fontsize = 15)
    plt.xlabel('False positive rate (1-Specificity)', fontsize = 15)
    plt.ylabel('True positive rate (Sensitivity)', fontsize = 15)
    plt.text(x = 0.02, y = 0.9, s = ('AUC Score:',round(roc_auc_score(y_test, y_pred_prob),4)))
    plt.grid(True)

#10. Build a knn model on a training dataset using euclidean distance to predict whether or not the client subscribed the term deposit. Calculate the accuracy of the model.
knn_classification = KNeighborsClassifier(n_neighbors = 3)
knn_model = knn_classification.fit(X_train, y_train)

#11. Plot a confusion matrix using the function created above and print a classification report
plot_confusion_matrix(knn_model)

y_pred = knn_model.predict(X_test)
print('accuracy_score:',metrics.accuracy_score(y_test, y_pred))
print('kappa_score:',metrics.cohen_kappa_score(y_test, y_pred))
print('kappa_score:',metrics.cohen_kappa_score(y_test, y_pred))
print('recall_score:',metrics.recall_score(y_test, y_pred))

#12. Find the optimal value of 'k' in knn with 3 fold cross validation.
tuned_paramaters = {'n_neighbors': np.arange(1, 3, 1),
                   'metric': ['hamming','euclidean','manhattan','Chebyshev']}
knn_classification = KNeighborsClassifier()
knn_grid = GridSearchCV(estimator = knn_classification, 
                        param_grid = tuned_paramaters, 
                        cv = 5, 
                        scoring = 'accuracy')
knn_grid.fit(X_train, y_train)
print('Best parameters for KNN Classifier: ', knn_grid.best_params_, '\n')

#13. Build a KNN model with the best parameters and find the accuracy. Also generate a classification report
knn_classification = KNeighborsClassifier(metric='manhattan', n_neighbors = 2)
knn_model_tuned = knn_classification.fit(X_train, y_train)
y_tuned = knn_model_tuned.predict(X_test)
print('accuracy_score:',metrics.accuracy_score(y_test, y_tuned))
print('kappa_score:',metrics.cohen_kappa_score(y_test, y_tuned))
print('kappa_score:',metrics.cohen_kappa_score(y_test, y_tuned))
print('recall_score:',metrics.recall_score(y_test, y_tuned))


#14. Find the area under the receiver operating characteristic curve and the confusion matrix for the tuned KNN model built in question 13.
plot_roc(knn_model_tuned)


#15. Calculate the percentage of misclassified and correctly classified observations
y_pred = knn_model.predict(X_test)
tp=confusion_matrix(y_test, y_pred)[0][0]
fp=confusion_matrix(y_test, y_pred)[0][1]
fn=confusion_matrix(y_test, y_pred)[1][0]
tn=confusion_matrix(y_test, y_pred)[1][1]
print("percentage of misclassified observations for original Model",100*(fp+fn)/(fp+fn+tp+tn))
print("percentage of correctly classified observations for original model",100*(tp+tn)/(fp+fn+tp+tn))
print()
y_pred = knn_model_tuned.predict(X_test)
tp=confusion_matrix(y_test, y_pred)[0][0]
fp=confusion_matrix(y_test, y_pred)[0][1]
fn=confusion_matrix(y_test, y_pred)[1][0]
tn=confusion_matrix(y_test, y_pred)[1][1]
print("percentage of misclassified observations for tuned Model",100*(fp+fn)/(fp+fn+tp+tn))
print("percentage of correctly classified observations for tuned model",100*(tp+tn)/(fp+fn+tp+tn))


#16. Compute the accuracy for each value of k and append the value in a list 'accuracy'. Build knn models for distance metric 'euclidean'. Consider only the odd numbers for the 'k' between the range 1 and 25.
tuned_paramaters = {'n_neighbors': np.arange(1, 25, 2),
                   'metric': ['hamming','euclidean','manhattan','Chebyshev']}
knn_classification = KNeighborsClassifier()
knn_grid = GridSearchCV(estimator = knn_classification, 
                        param_grid = tuned_paramaters, 
                        cv = 5, 
                        scoring = 'accuracy')
knn_grid.fit(X_train, y_train)
print('Best parameters for KNN Classifier: ', knn_grid.best_params_, '\n')

error_rate = []
for i in np.arange(1,25,2):
    knn = KNeighborsClassifier(i, metric = 'euclidean')
    score = cross_val_score(knn, X_train, y_train, cv = 5)
    score = score.mean()
    error_rate.append(1 - score)


plt.plot(range(1,25,2), error_rate)
plt.title('Error Rate', fontsize = 15)
plt.xlabel('K', fontsize = 15)
plt.ylabel('Error Rate', fontsize = 15)
plt.xticks(np.arange(1, 25, step = 2))

plt.axvline(x = 3, color = 'red')

plt.show()


#17. Draw a line plot to see the accuracy (list created in the above question) for each value of K using euclidean distance as a metric of KNN model and find the optimal value of 'k'.
plot_roc(knn_grid)


#----------------------------------------------------------------------------------------------------------------------
### ML2 - In-Class - Lab Exercise (Session 0) - Question
df = pd.read_csv("Heart_disease.csv")
df.isnull().sum().sort_values()

md = df.isnull().sum()
per = df.isnull().sum()/df.shape[0]*100
pd.concat([md, per], axis=1, keys=["Total", "Percentage"]).sort_values("Percentage")

df.male=df.male.astype("object")
df.education=df.education.astype("object")
df.currentSmoker=df.currentSmoker.astype("object")
df.prevalentStroke=df.prevalentStroke.astype("object")
df.prevalentHyp=df.prevalentHyp.astype("object")
df.diabetes=df.diabetes.astype("object")
df.CVD=df.CVD.astype("object")
df=df.drop("education")

df.hist()
plt.tight_layout()
plt.show()
df.drop(['male','currentSmoker','prevalentStroke','prevalentHyp','diabetes','CVD'], axis = 1).skew()
        
Mean_heartRate=df.heartRate.mean()
Mean_BMI=df.BMI.mean()
Mean_cigsPerDay=df.cigsPerDay.mean()
Mean_totChol=df.totChol.mean()
Mean_BPMeds=df.BPMeds.mean()
Mean_glucose=df.glucose.mean()

df.heartRate.replace(to_replace=np.nan, value=Mean_heartRate, inplace=True)
df.BMI.replace(to_replace=np.nan, value=Mean_BMI, inplace=True)
df.cigsPerDay.replace(to_replace=np.nan, value=Mean_cigsPerDay, inplace=True)
df.totChol.replace(to_replace=np.nan, value=Mean_totChol, inplace=True)
df.BPMeds.replace(to_replace=np.nan, value=Mean_BPMeds, inplace=True)
df.glucose.replace(to_replace=np.nan, value=Mean_glucose, inplace=True)

print("Target Variable CVD is Highly Skewed as not all classes are equally represented")
print(df.CVD.value_counts())
sns.countplot(df.CVD)


# 2. Predict whether or not a patient will have cardiovascular disease based on the information about blood pressure of the patient. Columns related to blood pressure are diaBP, sysBP and BPMeds.


New=df[['sysBP', 'diaBP','BPMeds']]
scaler = StandardScaler()
X=pd.DataFrame(scaler.fit_transform(New),columns = New.columns)

y=df[['CVD']]
y=y.astype('int')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)
print("shape of X_train:",X_train.shape)
print("shape of X_test:",X_test.shape)
print("shape of y_train:",y_train.shape)
print("shape of y_test:",y_test.shape)

smt = SMOTE()
X_train, y_train = smt.fit_resample(X_train, y_train)

logreg = sm.Logit(y_train, X_train).fit()
logreg.summary()

# 3. Predict whether or not a patient has cardiovascular disease using the categorical variables in the dataset. How does a unit change in each feature influence the odds of a patient having a cardiocascular disease?

X=df.select_dtypes(include = [np.object]).drop('CVD', axis=1)
y=df[['CVD']]
y=y.astype('int')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

smt = SMOTE()
X_train, y_train = smt.fit_resample(X_train, y_train)

classifier = DecisionTreeClassifier(criterion='entropy', random_state=0) 
decision_tree = classifier.fit(X_train, y_train)
decision_tree

y_pred= classifier.predict(X_test)  
print("accuracy_score",accuracy_score(y_test, y_pred))
print("recall_score",recall_score(y_test, y_pred))
print("confusion_matrix:\n", confusion_matrix(y_test, y_pred))


# 4. Predit if a patient has cardiovascular disease based on whether or not the patient has history of hypertension. Calculate the odds ratio.

X=df[['prevalentHyp']]
y=df[['CVD']]
y=y.astype('int')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)

smt = SMOTE()
X_train, y_train = smt.fit_resample(X_train, y_train)


LogRegr = LogisticRegression()
LogRegr.fit(X_train, y_train)
y_pred = LogRegr.predict(X_test)


print("accuracy_score",accuracy_score(y_test, y_pred))
print("recall_score",recall_score(y_test, y_pred))
print("confusion_matrix:\n", confusion_matrix(y_test, y_pred))


#----------------------------------------------------------------------------------------------------------------------
### ML2- Faculty Notebook (Session 0)-checkpoint

df_admissions = pd.read_csv('Admission_predict.csv')
df_admissions.Research.unique()
df_admissions['Chance of Admit'].unique()

# drop the column 'Serial No.' using drop()
# 'axis = 1' drops the specified column
df_admissions = df_admissions.drop('Serial No.', axis = 1)


## Distribution of numeric independent variables

# for the independent numeric variables, we plot the histogram to check the distribution of the variables
# Note: the hist() function considers the numeric variables only, by default
# we drop the target variable using drop()
# 'axis=1' drops the specified column
df_admissions.drop('Chance of Admit', axis = 1).hist()

# adjust the subplots
plt.tight_layout()

# display the plot
plt.show()  

# print the skewness for each numeric independent variable
print('Skewness:')
# we drop the target variable using drop()
# 'axis=1' drops the specified column
# skew() returns the coefficient of skewness for each variable
df_admissions.drop('Chance of Admit', axis = 1).skew()

## Distribution of categoric independent variable.

# for the independent categoric variable, we plot the count plot to check the distribution of the variable 'Research'
# use countplot() to plot the count of each label in the categorical variable 
sns.countplot(df_admissions.Research)

# add plot and axes labels
# set text size using 'fontsize'
plt.title('Count Plot for Categorical Variable (Research)', fontsize = 15)
plt.xlabel('Research', fontsize = 15)
plt.ylabel('Count', fontsize = 15)

# display the plot
plt.show()

## Distribution of dependent variable.

# consider only the target variable
df_target = df_admissions['Chance of Admit'].copy()

# get counts of 0's and 1's in the 'Chance of Admit' variable
df_target.value_counts()

# plot the countplot of the variable 'Chance of Admit'
sns.countplot(x = df_target)

# use below code to print the values in the graph
# 'x' and 'y' gives position of the text
# 's' is the text 
plt.text(x = -0.05, y = df_target.value_counts()[0] + 1, s = str(round((df_target.value_counts()[0])*100/len(df_target),2)) + '%')
plt.text(x = 0.95, y = df_target.value_counts()[1] +1, s = str(round((df_target.value_counts()[1])*100/len(df_target),2)) + '%')

# add plot and axes labels
# set text size using 'fontsize'
plt.title('Count Plot for Target Variable (Chance of Admit)', fontsize = 15)
plt.xlabel('Target Variable', fontsize = 15)
plt.ylabel('Count', fontsize = 15)

# to show the plot
plt.show()

# 2.5 Missing Value Treatment

# sort the variables on the basis of total null values in the variable
# 'isnull().sum()' returns the number of missing values in each variable
# 'ascending = False' sorts values in the descending order
# the variable with highest number of missing values will appear first
Total = df_admissions.isnull().sum().sort_values(ascending=False)          

# calculate percentage of missing values
# 'ascending = False' sorts values in the descending order
# the variable with highest percentage of missing values will appear first
Percent = (df_admissions.isnull().sum()*100/df_admissions.isnull().count()).sort_values(ascending=False)   

# concat the 'Total' and 'Percent' columns using 'concat' function
# pass a list of column names in parameter 'keys' 
# 'axis = 1' concats along the columns
missing_data = pd.concat([Total, Percent], axis = 1, keys = ['Total', 'Percentage of Missing Values'])    
missing_data

# 2.6 Dummy Encode the Categorical Variables

# Split the dependent and independent variables.
# store the target variable 'Chance of Admit' in a dataframe 'df_target'
df_target = df_admissions['Chance of Admit']

# store all the independent variables in a dataframe 'df_feature' 
# drop the column 'Chance of Admit' using drop()
# 'axis = 1' drops the specified column
df_feature = df_admissions.drop('Chance of Admit', axis = 1)


# Filter numerical and categorical variables.
# filter the numerical features in the dataset
# 'select_dtypes' is used to select the variables with given data type
# 'include = [np.number]' will include all the numerical variables
df_num = df_feature.select_dtypes(include = [np.number])

# display numerical features
df_num.columns

# filter the categorical features in the dataset
# 'select_dtypes' is used to select the variables with given data type
# 'include = [np.object]' will include all the categorical variables
df_cat = df_feature.select_dtypes(include = [np.object])

# display categorical features
df_cat.columns

#The logistic regression method fails in presence of categorical variables. To overcome this we use (n-1) dummy encoding.
#Encode the each categorical variable and create (n-1) dummy variables for n categories of the variable.
# use 'get_dummies' from pandas to create dummy variables
# use 'drop_first' to create (n-1) dummy variables
dummy_var = pd.get_dummies(data = df_cat, drop_first = True)



# 2.7 Scale the Data
# We scale the variables to get all the variables in the same range. With this, we can avoid a problem in which some features come to dominate solely because they tend to have larger values than others.

# initialize the standard scalar
X_scaler = StandardScaler()

# scale all the numerical columns
# standardize all the columns of the dataframe 'df_num'
num_scaled = X_scaler.fit_transform(df_num)

# create a dataframe of scaled numerical variables
# pass the required column names to the parameter 'columns'
df_num_scaled = pd.DataFrame(num_scaled, columns = df_num.columns)

# Concatenate scaled numerical and dummy encoded categorical variables.
# concat the dummy variables with numeric features to create a dataframe of all independent variables
# 'axis=1' concats the dataframes along columns 
X = pd.concat([df_num_scaled, dummy_var], axis = 1)

## 2.8 Train-Test Split

# add a constant column to the dataframe
# while using the 'Logit' method in the Statsmodels library, the method do not consider the intercept by default
# we can add the intercept to the set of independent variables using 'add_constant()'
X = sm.add_constant(X)

# split data into train subset and test subset
# set 'random_state' to generate the same dataset each time you run the code 
# 'test_size' returns the proportion of data to be included in the testing set
X_train, X_test, y_train, y_test = train_test_split(X, df_target, random_state = 10, test_size = 0.2)

# check the dimensions of the train & test subset using 'shape'
# print dimension of train set
print('X_train', X_train.shape)
print('y_train', y_train.shape)

# print dimension of test set
print('X_test', X_test.shape)
print('y_test', y_test.shape)


# Create a generalized function to create a dataframe containing the scores for the models.

# create an empty dataframe to store the scores for various algorithms
score_card = pd.DataFrame(columns=['Probability Cutoff', 'AUC Score', 'Precision Score', 'Recall Score',
                                       'Accuracy Score', 'Kappa Score', 'f1-score'])

# append the result table for all performance scores
# performance measures considered for model comparision are 'AUC Score', 'Precision Score', 'Recall Score','Accuracy Score',
# 'Kappa Score', and 'f1-score'
# compile the required information in a user defined function 
def update_score_card(model, cutoff):
    
    # let 'y_pred_prob' be the predicted values of y
    y_pred_prob = logreg.predict(X_test)

    # convert probabilities to 0 and 1 using 'if_else'
    y_pred = [ 0 if x < cutoff else 1 for x in y_pred_prob]
    
    # assign 'score_card' as global variable
    global score_card

    # append the results to the dataframe 'score_card'
    # 'ignore_index = True' do not consider the index labels
    score_card = score_card.append({'Probability Cutoff': cutoff,
                                    'AUC Score' : metrics.roc_auc_score(y_test, y_pred),
                                    'Precision Score': metrics.precision_score(y_test, y_pred),
                                    'Recall Score': metrics.recall_score(y_test, y_pred),
                                    'Accuracy Score': metrics.accuracy_score(y_test, y_pred),
                                    'Kappa Score':metrics.cohen_kappa_score(y_test, y_pred),
                                    'f1-score': metrics.f1_score(y_test, y_pred)}, 
                                    ignore_index = True)


# 3. Logistic Regression (Full Model)
# Build a full logistic model on a training dataset.

# build the model on train data (X_train and y_train)
# use fit() to fit the logistic regression model
logreg = sm.Logit(y_train, X_train).fit()

# print the summary of the model
print(logreg.summary())


#Interpretation: The Pseudo R-squ. obtained from the above model summary is the value of McFadden's R-squared. This value can be obtained from the formula:

#McFadden's R-squared =  1−𝐿𝑜𝑔−𝐿𝑖𝑘𝑒𝑙𝑖ℎ𝑜𝑜𝑑𝐿𝐿−𝑁𝑢𝑙𝑙 

#Where,
#Log-Likelihood: It is the maximum value of the log-likelihood function
#LL-Null: It is the maximum value of the log-likelihood function for the model containing only the intercept

#The LLR p-value is less than 0.05, implies that the model is significant.

#There are different types of pseudo R-squared such as Cox & Snell R-squared, Nagelkerke R-squared and so on.

#Cox & Snell R-squared: The convergence of the logistic model can be determined by the R-squared value. It is given by the formula:

#Cox & Snell R-squared =  1−(𝐿(𝑀𝐼𝑛𝑡𝑒𝑟𝑐𝑒𝑝𝑡)𝐿(𝑀𝐹𝑢𝑙𝑙))2/𝑁 

#Where,
#L(M): The conditional probability of target variable given the independent variables
#N: Total number of observations

#Note: The maximum of Cox & Snell R-squared is always less than 1. It is equal to  (1−(𝐿(𝑀𝐼𝑛𝑡𝑒𝑟𝑐𝑒𝑝𝑡)2/𝑁) 
#Nagelkerke R-squared: It is defined as the ratio of Cox & Snell R-squared to the maximum of Cox & Snell R-squared. The formula is given as:

#Nagelkerke R-squared =  1−(𝐿(𝑀𝐼𝑛𝑡𝑒𝑟𝑐𝑒𝑝𝑡)𝐿(𝑀𝐹𝑢𝑙𝑙))2/𝑁1−(𝐿(𝑀𝐼𝑛𝑡𝑒𝑟𝑐𝑒𝑝𝑡)2/𝑁 

#Thus, Nagelkerke R-squared can be equal to 1, if  𝐿(𝑀𝐹𝑢𝑙𝑙)=1


# Calculate the AIC (Akaike Information Criterion) value
# It is a relative measure of model evaluation. It gives a trade-off between model accuracy and model complexity.

# 'aic' retuns the AIC value for the model
print('AIC:', logreg.aic)

#  We can use the AIC value to compare different models created on the same dataset.

# Interpret the odds for each variabl
logreg.params

# take the exponential of the coefficient of a variable to calculate the odds
# 'params' returns the coefficients of all the independent variables
# pass the required column name to the parameter, 'columns'
df_odds = pd.DataFrame(np.exp(logreg.params), columns= ['Odds']) 

logreg.predict(X_test[0:1])
y_test[0:1]
test_prediction = logreg.predict(X_test)

 # convert probabilities to 0 and 1 using 'if_else'
cutoff = 0.5
y_pred = [ 0 if x < cutoff else 1 for x in test_prediction]

metrics.accuracy_score(y_test, y_pred)

# Cross Entropy Loss (Log Loss)
metrics.log_loss(y_test, test_prediction)



#----------------------------------------------------------------------------------------------------------------------
### ML2- Faculty Notebook (Session 1) [ COntinuation of Session 0 - Check point]

# Do predictions on the test set.
# let 'y_pred_prob' be the predicted values of y
y_pred_prob = logreg.predict(X_test)

# print the y_pred_prob
y_pred_prob.head()

# Since the target variable can take only two values either 0 or 1. We decide the cut-off of 0.5. i.e. if 'y_pred_prob' is less than 0.5, then consider it to be 0 else consider it to be 1

# convert probabilities to 0 and 1 using 'if_else'
y_pred = [ 0 if x < 0.5 else 1 for x in y_pred_prob]


# create a confusion matrix
# pass the actual and predicted target values to the confusion_matrix()
cm = confusion_matrix(y_test, y_pred)

# label the confusion matrix  
# pass the matrix as 'data'
# pass the required column names to the parameter, 'columns'
# pass the required row names to the parameter, 'index'
conf_matrix = pd.DataFrame(data = cm,columns = ['Predicted:0','Predicted:1'], index = ['Actual:0','Actual:1'])

# plot a heatmap to visualize the confusion matrix
# 'annot' prints the value of each grid 
# 'fmt = d' returns the integer value in each grid
# 'cmap' assigns color to each grid
# as we do not require different colors for each grid in the heatmap,
# use 'ListedColormap' to assign the specified color to the grid
# 'cbar = False' will not return the color bar to the right side of the heatmap
# 'linewidths' assigns the width to the line that divides each grid
# 'annot_kws = {'size':25})' assigns the font size of the annotated text 
sns.heatmap(conf_matrix, annot = True, fmt = 'd', cmap = ListedColormap(['lightskyblue']), cbar = False, 
            linewidths = 0.1, annot_kws = {'size':25})

# set the font size of x-axis ticks using 'fontsize'
plt.xticks(fontsize = 20)

# set the font size of y-axis ticks using 'fontsize'
plt.yticks(fontsize = 20)

# display the plot
plt.show()

# True Negatives are denoted by 'TN'
# Actual 'O' values which are classified correctly
TN = cm[0,0]

# True Positives are denoted by 'TP'
# Actual '1' values which are classified correctly
TP = cm[1,1]

# False Positives are denoted by 'FP'
# it is the type 1 error
# Actual 'O' values which are classified wrongly as '1'
FP = cm[0,1]

# False Negatives are denoted by 'FN'
# it is the type 2 error
# Actual '1' values which are classified wrongly as '0'
FN = cm[1,0]

# Precision: It is defined as the ratio of true positives to the total positive predictions.
precision = TP / (TP+FP)

# Recall: It is the ratio of true positives to the total actual positive observations. It is also known as, Sensitivity or True Positive Rate
recall = TP / (TP+FN)

# Specificity: It is the ratio of true negatives to the total actual negative observations
specificity = TN / (TN+FP)

# f1-score: It is defined as the harmonic mean of precision and recall.
f1_score = 2*((precision*recall)/(precision+recall))

# Accuracy: It is the ratio of correct predictions (i.e. TN+TP) to the total observations. According to the confusion matrix, it is the ratio of the sum of diagonal elements to the sum of all the in the matrix. It is not a very good measure if the dataset is imbalanced.
accuracy = (TN+TP) / (TN+FP+FN+TP)


# We can also calculate the above measures using the classification_report()
# calculate various performance measures
acc_table = classification_report(y_test, y_pred)

#From the above output, we can infer that the recall of the positive class is known as sensitivity and the recall of the negative class is specificity.
#support is the number of observations in the corresponding class.
#The macro average in the output is obtained by averaging the unweighted mean per label and the weighted average is given by averaging the support-weighted mean per label.

#Kappa score: It is a measure of inter-rater reliability. For logistic regression, the actual and predicted values of the target variable are the raters.
kappa = cohen_kappa_score(y_test, y_pred)

#Interpretation: As the kappa score for the full model (with cut-off probability 0.5) is 0.6509, we can say that there is substantial agreement between the actual and predicted values.

#Plot the ROC curve.
#ROC curve is plotted with the true positive rate (tpr) on the y-axis and false positive rate (fpr) on the x-axis. The area under this curve is used as a measure of separability of the model.


# the roc_curve() returns the values for false positive rate, true positive rate and threshold
# pass the actual target values and predicted probabilities to the function
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

# plot the ROC curve
plt.plot(fpr, tpr)

# set limits for x and y axes
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])

# plot the straight line showing worst prediction for the model
plt.plot([0, 1], [0, 1],'r--')

# add plot and axes labels
# set text size using 'fontsize'
plt.title('ROC curve for Admission Prediction Classifier (Full Model)', fontsize = 15)
plt.xlabel('False positive rate (1-Specificity)', fontsize = 15)
plt.ylabel('True positive rate (Sensitivity)', fontsize = 15)

# add the AUC score to the plot
# 'x' and 'y' gives position of the text
# 's' is the text 
# use round() to round-off the AUC score upto 4 digits
plt.text(x = 0.02, y = 0.9, s = ('AUC Score:', round(metrics.roc_auc_score(y_test, y_pred_prob),4)))
                               
# plot the grid
plt.grid(True)

# Interpretation: The red dotted line represents the ROC curve of a purely random classifier; a good classifier stays as far away from that line as possible (toward the top-left corner).
# From the above plot, we can see that our classifier (logistic regression) is away from the dotted line; with the AUC score 0.9367.

# 3.1 Identify the Best Cut-off Value
# Tabulate the performance measures for different cut-offs.
# The performance measures that we obtained above, are for the cut_off = 0.5. Now, let us consider a list of values as cut-off and calculate the different performance measures

# consider a list of values for cut-off
cutoff = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

# use the for loop to compute performance measures for each value of the cut-off
# call the update_score_card() to update the score card for each cut-off
# pass the model and cut-off value to the function
for value in cutoff:
    update_score_card(logreg, value)

# print the score card 
print('Score Card for Logistic regression:')

# sort the dataframe based on the probability cut-off values ascending order
# 'reset_index' resets the index of the dataframe
# 'drop = True' drops the previous index
score_card = score_card.sort_values('Probability Cutoff').reset_index(drop = True)

# color the cell in the columns 'AUC Score', 'Accuracy Score', 'Kappa Score', 'f1-score' having maximum values
# 'style.highlight_max' assigns color to the maximum value
# pass specified color to the parameter, 'color'
# pass the data to limit the color assignment to the parameter, 'subset' 
score_card.style.highlight_max(color = 'lightblue', subset = ['AUC Score', 'Accuracy Score', 'Kappa Score', 'f1-score'])


#Interpretation: The above dataframe shows that, the model cut_off probability 0.6, returns the highest AUC score, f1-score, kappa score and accuracy.

#In the above method, we passed the list of values for the cut-off. But, this method is not efficient as one can pass different values and obtain a cut-off based on the passed values.
#To obtain the optimal cut-off value we use the following methods:
#Youden's Index
#Cost-based Method

#3.1.1 Youden's Index
#Youden's Index is the classification cut-off probability for which the (Sensitivity + Specificity - 1) is maximized.

#Youden's Index = max(Sensitivity + Specificity - 1) = max(TPR + TNR - 1) = max(TPR - FPR)

#i.e. select the cut-off probability for which the (TPR - FPR) is maximum.


# create a dataframe to store the values for false positive rate, true positive rate and threshold
youdens_table = pd.DataFrame({'TPR': tpr,
                             'FPR': fpr,
                             'Threshold': thresholds})

# calculate the difference between TPR and FPR for each threshold and store the values in a new column 'Difference'
youdens_table['Difference'] = youdens_table.TPR - youdens_table.FPR

# sort the dataframe based on the values of difference 
# 'ascending = False' sorts the data in descending order
# 'reset_index' resets the index of the dataframe
# 'drop = True' drops the previous index
youdens_table = youdens_table.sort_values('Difference', ascending = False).reset_index(drop = True)

# print the first five observations
youdens_table.head()

# As we can see that the optimal cut-off probability is approximately 0.62. Let us consider this cut-off to predict the target values. i.e. if 'y_pred_prob' is less than 0.62, then consider it to be 0 else consider it to be 1.

# convert probabilities to 0 and 1 using 'if_else'
y_pred_youden = [ 0 if x < 0.62 else 1 for x in y_pred_prob]


# Plot the confusion matrix.
# create a confusion matrix
# pass the actual and predicted target values to the confusion_matrix()
cm = confusion_matrix(y_test, y_pred_youden)

# label the confusion matrix  
# pass the matrix as 'data'
# pass the required column names to the parameter, 'columns'
# pass the required row names to the parameter, 'index'
conf_matrix = pd.DataFrame(data = cm,columns = ['Predicted:0','Predicted:1'], index = ['Actual:0','Actual:1'])

# plot a heatmap to visualize the confusion matrix
# 'annot' prints the value of each grid 
# 'fmt = d' returns the integer value in each grid
# 'cmap' assigns color to each grid
# as we do not require different colors for each grid in the heatmap,
# use 'ListedColormap' to assign the specified color to the grid
# 'cbar = False' will not return the color bar to the right side of the heatmap
# 'linewidths' assigns the width to the line that divides each grid
# 'annot_kws = {'size':25})' assigns the font size of the annotated text 
sns.heatmap(conf_matrix, annot = True, fmt = 'd', cmap = ListedColormap(['lightskyblue']), cbar = False, 
            linewidths = 0.1, annot_kws = {'size':25})

# set the font size of x-axis ticks using 'fontsize'
plt.xticks(fontsize = 20)

# set the font size of y-axis ticks using 'fontsize'
plt.yticks(fontsize = 20)

# display the plot
plt.show()


# Compute various performance metrics.
# calculate various performance measures
acc_table = classification_report(y_test, y_pred_youden)

# print the table
print(acc_table)


# Interpretation: From the above output, we can see that the model with cut-off = 0.62, is 85% accurate. The specificity and the sensitivity are nearly balanced.

# compute the kappa value
kappa = cohen_kappa_score(y_test, y_pred_youden)

# Interpretation: As the kappa score for the full model (with cut-off probability 0.62) is 0.6992, we can say that there is substantial agreement between the actual and predicted values.

# 3.1.2 Cost-based Method
# The full logistic regression model (build in section 3), have different values for false positives (FP) and false negatives (FN). Thus, we can use the cost-based method to calculate the optimal value of the cut-off. In this method, we find the optimal value of the cut-off for which the total cost is minimum. The total cost is given by the formula:

# total_cost = FN x C_1 + FP x C_2
#Where,
# C_1: It is the cost of false negatives
# C_2: It is the cost of false positives
# The cost values can be decided using business knowledge.


# define a function to calculate the total_cost for a cut-off value
# pass the actual values of y, predicted probabilities of y, cost for FN and FP
def calculate_total_cost(actual_value, predicted_value, cost_FN, cost_FP):

    # pass the actual and predicted values to calculate the confusion matrix
    cm = confusion_matrix(actual_value, predicted_value)           
    
    # create an array of the confusion matrix
    cm_array = np.array(cm)
    
    # return the total_cost
    return cm_array[1,0] * cost_FN + cm_array[0,1] * cost_FP

# create an empty dataframe to store the cost for different probability cut-offs
df_total_cost = pd.DataFrame(columns = ['cut-off', 'total_cost'])

# initialize i to '0' corresponding to the 1st row in the dataframe
i = 0

# use for loop to calculate 'total_cost' for each cut-off probability value
# call the function 'calculate_total_cost' to calculate the cost
# pass the actual y-values
# calculate the predicted y-values from 'y_pred_prob' for the cut-off probability value
# assign the costs 3.5 and 2 to False Negatives and False Positives respectively
# add the obtained 'cut_off' and 'total_cost' at the ith index of the dataframe
for cut_off in range(10, 100):
    total_cost = calculate_total_cost(y_test,  y_pred_prob.map(lambda x: 1 if x > (cut_off/100) else 0), 3.5, 2) 
    df_total_cost.loc[i] = [(cut_off/100), total_cost] 
    
    # increment the value of 'i' for each row index in the dataframe 'df_total_cost'
    i += 1


# sort the dataframe based on the 'total_cost' in the ascending order
# print the first ten rows in the dataframe
#df_total_cost.sort_values('total_cost', ascending = True).head(10)

# From the above output we can see that, the 'total_cost' is same for the cut-off probability values 0.56, 0.57, 0.58, 0.59, 0.60 and 0.61. Thus, we can consider any of these value as the cut-off probability.

#Here, we are considering the cut-off value as 0.58. i.e. if 'y_pred_prob' is less than 0.58, then consider it to be 0 else consider it to be 1.


# convert probabilities to 0 and 1 using 'if_else'
y_pred_cost = [ 0 if x < 0.58 else 1 for x in y_pred_prob]

# create a confusion matrix
# pass the actual and predicted target values to the confusion_matrix()
cm = confusion_matrix(y_test, y_pred_cost)

# label the confusion matrix  
# pass the matrix as 'data'
# pass the required column names to the parameter, 'columns'
# pass the required row names to the parameter, 'index'
conf_matrix = pd.DataFrame(data = cm,columns = ['Predicted:0','Predicted:1'], index = ['Actual:0','Actual:1'])

# plot a heatmap to visualize the confusion matrix
# 'annot' prints the value of each grid 
# 'fmt = d' returns the integer value in each grid
# 'cmap' assigns color to each grid
# as we do not require different colors for each grid in the heatmap,
# use 'ListedColormap' to assign the specified color to the grid
# 'cbar = False' will not return the color bar to the right side of the heatmap
# 'linewidths' assigns the width to the line that divides each grid
# 'annot_kws = {'size':25})' assigns the font size of the annotated text 
sns.heatmap(conf_matrix, annot = True, fmt = 'd', cmap = ListedColormap(['lightskyblue']), cbar = False, 
            linewidths = 0.1, annot_kws = {'size':25})

# set the font size of x-axis ticks using 'fontsize'
plt.xticks(fontsize = 20)

# set the font size of y-axis ticks using 'fontsize'
plt.yticks(fontsize = 20)

# display the plot
plt.show()

# Compute various performance metrics.

# calculate various performance measures
acc_table = classification_report(y_test, y_pred_cost)

# print the table
print(acc_table)

# compute the kappa value
kappa = cohen_kappa_score(y_test, y_pred_cost)


#Interpretation: As the kappa score for the full model (with cut-off probability 0.58) is 0.7247, we can say that there is substantial agreement between the actual and predicted values.


#4. Recursive Feature Elimination (RFE)
#In the linear regression module, we learn about various techniques for selecting the significant features in the dataset. In this example, let us consider the RFE method for feature selection.

# consider the independent variables (without the intercept term)
# as, X_train and X_test contains the intercept term
# use 'iloc' to select the variables wthout intercept term 
X_train_rfe = X_train.iloc[:,1:]
X_test_rfe = X_test.iloc[:,1:]

# initiate logistic regression model to use in feature selection
logreg = LogisticRegression()

# build the RFE model
# pass the logistic regression model to 'estimator'
# pass number of required features to 'n_features_to_select'
# if we do not pass the number of features, RFE considers half of the features
rfe_model = RFE(estimator = logreg, n_features_to_select = 3)

# fit the RFE model on the train dataset using fit()
rfe_model = rfe_model.fit(X_train_rfe, y_train)

# create a series containing feature and its corresponding rank obtained from RFE
# 'ranking_' returns the rank of each variable after applying RFE
# pass the ranks as the 'data' of a series
# 'index' assigns feature names as index of a series 
feat_index = pd.Series(data = rfe_model.ranking_, index = X_train_rfe.columns)

# select the features with rank = 1
# 'index' returns the indices of a series (i.e. features with rank=1) 
signi_feat_rfe = feat_index[feat_index==1].index

# print the significant features obtained from RFE
print(signi_feat_rfe)

# Build the logisitc regression model using the variables obtained from RFE

# build the model on train data (X_train and y_train)
# use fit() to fit the logistic regression model
# consider the variables obtained from RFE method and the intercept term
logreg_rfe = sm.Logit(y_train, X_train[['const', 'GRE Score', 'University Rating', 'CGPA']]).fit()

# print the summary of the model
print(logreg_rfe.summary())



# Calculate the AIC (Akaike Information Criterion) value.
# It is a relative measure of model evaluation. It gives a trade-off between model accuracy and model complexity.


# 'aic' retuns the AIC value for the model
print('AIC:', logreg_rfe.aic)


# let 'y_pred_prob_rfe' be the predicted values of y
y_pred_prob_rfe = logreg_rfe.predict(X_test[['const', 'GRE Score', 'University Rating', 'CGPA']])

# print the y_pred_prob_rfe
y_pred_prob_rfe.head()


# Since the target variable can take only two values either 0 or 1. We consider the cut-off value 0.6. i.e. if 'y_pred_prob_rfe' is less than 0.6, then consider it to be 0 else consider it to be 1.

# convert probabilities to 0 and 1 using 'if_else'
y_pred_rfe = [ 0 if x < 0.6 else 1 for x in y_pred_prob_rfe]


# print the first five observations of y_pred_rfe
y_pred_rfe[0:5]


# create a confusion matrix
# pass the actual and predicted target values to the confusion_matrix()
cm = confusion_matrix(y_test, y_pred_rfe)

# label the confusion matrix  
# pass the matrix as 'data'
# pass the required column names to the parameter, 'columns'
# pass the required row names to the parameter, 'index'
conf_matrix = pd.DataFrame(data = cm,columns = ['Predicted:0','Predicted:1'], index = ['Actual:0','Actual:1'])

# plot a heatmap to visualize the confusion matrix
# 'annot' prints the value of each grid 
# 'fmt = d' returns the integer value in each grid
# 'cmap' assigns color to each grid
# as we do not require different colors for each grid in the heatmap,
# use 'ListedColormap' to assign the specified color to the grid
# 'cbar = False' will not return the color bar to the right side of the heatmap
# 'linewidths' assigns the width to the line that divides each grid
# 'annot_kws = {'size':25})' assigns the font size of the annotated text 
sns.heatmap(conf_matrix, annot = True, fmt = 'd', cmap = ListedColormap(['lightskyblue']), cbar = False, 
            linewidths = 0.1, annot_kws = {'size':25})

# set the font size of x-axis ticks using 'fontsize'
plt.xticks(fontsize = 20)

# set the font size of y-axis ticks using 'fontsize'
plt.yticks(fontsize = 20)

# display the plot
plt.show()

# performance measures obtained by classification_report()
result = classification_report(y_test, y_pred_rfe)

# print the result
print(result)


# compute the kappa value
kappa = cohen_kappa_score(y_test, y_pred_rfe)

# print the kappa value
print('kappa value:',kappa)

# the roc_curve() returns the values for false positive rate, true positive rate and threshold
# pass the actual target values and predicted probabilities to the function
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob_rfe)

# plot the ROC curve
plt.plot(fpr, tpr)

# set limits for x and y axes
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])

# plot the straight line showing worst prediction for the model
plt.plot([0, 1], [0, 1],'r--')

# add plot and axes labels
# set text size using 'fontsize'
plt.title('ROC curve for Admission Prediction Classifier (RFE Model)', fontsize = 15)
plt.xlabel('False positive rate (1-Specificity)', fontsize = 15)
plt.ylabel('True positive rate (Sensitivity)', fontsize = 15)

# add the AUC score to the plot
# 'x' and 'y' gives position of the text
# 's' is the text 
# use round() to round-off the AUC score upto 4 digits
plt.text(x = 0.02, y = 0.9, s = ('AUC Score:', round(metrics.roc_auc_score(y_test, y_pred_prob_rfe),4)))
                               
# plot the grid
plt.grid(True)

# Interpretation: The red dotted line represents the ROC curve of a purely random classifier; a good classifier stays as far away from that line as possible (toward the top-left corner).
# From the above plot, we can see that our classifier (logistic regression with features obtained from RFE method) is away from the dotted line; with the AUC score 0.9273




#----------------------------------------------------------------------------------------------------------------------
### ML2 - In-Class - Lab Exercise (Session 1) - Question

df = pd.read_csv("Heart_disease.csv")
df.male=df.male.astype("object")
df.currentSmoker=df.currentSmoker.astype("object")
df.prevalentStroke=df.prevalentStroke.astype("object")
df.prevalentHyp=df.prevalentHyp.astype("object")
df.diabetes=df.diabetes.astype("object")
df.CVD=df.CVD.astype("object")
df.dtypes


Mean_heartRate=df.heartRate.mean()
Mean_BMI=df.BMI.mean()
Mean_cigsPerDay=df.cigsPerDay.mean()
Mean_totChol=df.totChol.mean()
Mean_BPMeds=df.BPMeds.mean()
Mean_glucose=df.glucose.mean()


#Perform an analysis for missing values
df.hist()
plt.tight_layout()
plt.show()
df.drop(['male','currentSmoker','prevalentStroke','prevalentHyp','diabetes','CVD'], axis = 1).skew()
          
#1. Are all the classes of target variable 'CVD' fairly represented by records in the considered dataset ?
print("Target Variable CVD is Highly Skewed as not all classes are equally represented")
print(df.CVD.value_counts())
sns.countplot(df.CVD)    

# 2. Predict whether or not a patient will have cardiovascular disease based on the information about blood pressure of the patient. Columns related to blood pressure are diaBP, sysBP and BPMeds.

New=df[['sysBP', 'diaBP','BPMeds']]
scaler = StandardScaler()
X=pd.DataFrame(scaler.fit_transform(New),columns = New.columns)

y=df[['CVD']]
y=y.astype('int')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)
print("shape of X_train:",X_train.shape)
print("shape of X_test:",X_test.shape)
print("shape of y_train:",y_train.shape)
print("shape of y_test:",y_test.shape)


smt = SMOTE()
X_train, y_train = smt.fit_resample(X_train, y_train)
print("shape of X_train:",X_train.shape)
print("shape of y_train:",y_train.shape)

LogRegr = LogisticRegression()
LogRegr.fit(X_train, y_train)
y_pred = LogRegr.predict(X_test)


print("accuracy_score",accuracy_score(y_test, y_pred))
print("recall_score",recall_score(y_test, y_pred))
print("confusion_matrix:\n", confusion_matrix(y_test, y_pred))


# 3. Predict whether or not a patient has cardiovascular disease using the categorical variables in the dataset. How does a unit change in each feature influence the odds of a patient having a cardiocascular disease?

X=df.select_dtypes(include = [np.object]).drop('CVD', axis=1)
y=df[['CVD']]
y=y.astype('int')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)
print("shape of X_train:",X_train.shape)
print("shape of X_test:",X_test.shape)
print("shape of y_train:",y_train.shape)
print("shape of y_test:",y_test.shape)

smt = SMOTE()
X_train, y_train = smt.fit_resample(X_train, y_train)

classifier = DecisionTreeClassifier(criterion='entropy', random_state=0) 
decision_tree = classifier.fit(X_train, y_train)
decision_tree


y_pred= classifier.predict(X_test)  
print("accuracy_score",accuracy_score(y_test, y_pred))
print("recall_score",recall_score(y_test, y_pred))
print("confusion_matrix:\n", confusion_matrix(y_test, y_pred))


# 4. Predit if a patient has cardiovascular disease based on whether or not the patient has history of hypertension. Calculate the odds ratio.
X=df[['prevalentHyp']]
y=df[['CVD']]
y=y.astype('int')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)
print("shape of X_train:",X_train.shape)
print("shape of X_test:",X_test.shape)
print("shape of y_train:",y_train.shape)
print("shape of y_test:",y_test.shape)


X.isnull().sum().sort_values()


smt = SMOTE()
X_train, y_train = smt.fit_resample(X_train, y_train)


logreg = sm.Logit(y_train, X_train).fit()
logreg.summary()
logreg.params

df_odds = pd.DataFrame(np.exp(logreg.params), columns= ['Odds']) 
df_odds


## 2. Model Evaluation Metrics
# 5. Build a full model to predict if a patient will have a cardiovascular disease. Find the value of Mcfadden's R2.

df_objects=df.select_dtypes(include = [np.object]).drop('CVD', axis=1)
df_dummies=pd.get_dummies(df_objects, drop_first=True)

df_numbers=df.select_dtypes(include = [np.number]).drop('education', axis=1)
scaler = StandardScaler()
df_scaled=pd.DataFrame(scaler.fit_transform(df_numbers),columns = df_numbers.columns)

X=pd.concat([df_dummies, df_numbers], axis=1)
y=df[['CVD']]
y=y.astype('int')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)
print("shape of X_train:",X_train.shape)
print("shape of X_test:",X_test.shape)
print("shape of y_train:",y_train.shape)
print("shape of y_test:",y_test.shape)
smt = SMOTE()
X_train, y_train = smt.fit_resample(X_train, y_train)
print("shape of X_train:",X_train.shape)
print("shape of y_train:",y_train.shape)

logreg = sm.Logit(y_train, X_train).fit()
logreg.summary()

print("Mcfadden's R2=0.09375")
Model5_AIC=logreg.aic
Model5_Entrohpy=round(metrics.roc_auc_score(y_test, y_pred),4)

# 6. Find the significant variables in the full model when all the variables are considered in prediction of whether or not a patient has cardiovascular disease.

print("All variables except Education are Significant Variables")
logreg = sm.Logit(y_train, X_train).fit()
logreg.summary()

# 7. How do the coefficients of each feature form the dataset impact the odds of a patient having a cardiovascular disease?

df_odds = pd.DataFrame(np.exp(logreg.params), columns= ['Odds']).sort_values('Odds' , ascending=False)
df_odds

# 3. Performance evaluation metrics
# 8. For the full model, calculate the accuracy manually using the confusion matrix. Consider 0.5 as the probability threshold.


LogRegr = LogisticRegression()
LogRegr.fit(X_train, y_train)
y_pred = LogRegr.predict(X_test)

print("accuracy_score",accuracy_score(y_test, y_pred))
print("recall_score",recall_score(y_test, y_pred))
print("confusion_matrix:\n", confusion_matrix(y_test, y_pred))

TP=confusion_matrix(y_test, y_pred)[0][0]
FP=confusion_matrix(y_test, y_pred)[0][1]
TN=confusion_matrix(y_test, y_pred)[1][0]
FN=confusion_matrix(y_test, y_pred)[1][1]
Accuracy=(TP+TN)/(TP+TN+FP+FN)
print("Accuracy of Model:", Accuracy)

# 9. Calculate value of kappa for the full model built in question 5. Consider threshold value as 0.18
LogRegr = LogisticRegression()
LogRegr.fit(X_train, y_train)
y_pred = LogRegr.predict(X_test)
cutoff = 0.18
y_prob_pred = [ 0 if x < cutoff else 1 for x in y_pred]
metrics.cohen_kappa_score(y_test, y_prob_pred)

# 10. Identify the features from the dataset that are involved in multicollinearity. After that, split the updated data using train_test_split.

vif = pd.DataFrame()
vif["variables"] = X.columns
vif["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
vif.sort_values('VIF' , ascending=False)


df_objects=df.select_dtypes(include = [np.object]).drop('CVD', axis=1)
df_dummies=pd.get_dummies(df_objects, drop_first=True)

df_numbers=df.select_dtypes(include = [np.number]).drop('education', axis=1)
scaler = StandardScaler()
df_scaled=pd.DataFrame(scaler.fit_transform(df_numbers),columns = df_numbers.columns)

X=pd.concat([df_dummies, df_numbers], axis=1)
y=df[['CVD']]
y=y.astype('int')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)
print("shape of X_train:",X_train.shape)
print("shape of X_test:",X_test.shape)
print("shape of y_train:",y_train.shape)
print("shape of y_test:",y_test.shape)

# 11. Use the data obtained from Q10 and identify 5 features that contribute most in the prediction of target variable.

print(" 5 features that contribute most in the prediction of target variable are ")
vif.sort_values('VIF' , ascending=False,ignore_index=True)[0:5]["variables"]

# 12. Build a model using the features obtained in question 11. For the model find:
# Accuracy
# F1 score

New=df[['sysBP', 'diaBP','BMI','age','heartRate']]
scaler = StandardScaler()
X=pd.DataFrame(scaler.fit_transform(New),columns = New.columns)
y=df[['CVD']]
y=y.astype('int')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)
print("shape of X_train:",X_train.shape)
print("shape of X_test:",X_test.shape)
print("shape of y_train:",y_train.shape)
print("shape of y_test:",y_test.shape)
    
smt = SMOTE()
X_train, y_train = smt.fit_resample(X_train, y_train)
print("shape of X_train:",X_train.shape)
print("shape of y_train:",y_train.shape)

LogRegr = LogisticRegression()
LogRegr.fit(X_train, y_train)
y_pred = LogRegr.predict(X_test)

print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
print("f1-score:",metrics.f1_score(y_test, y_pred))


#13. Compare the full model in question 5 and the model built in question 12 using their ROC curves.

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

# plot the ROC curve
plt.plot(fpr, tpr)


plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])


plt.plot([0, 1], [0, 1],'r--')


plt.title('ROC curve for Admission Prediction Classifier (Full Model)', fontsize = 15)
plt.xlabel('False positive rate (1-Specificity)', fontsize = 15)
plt.ylabel('True positive rate (Sensitivity)', fontsize = 15)

plt.text(x = 0.02, y = 0.9, s = ('AUC Score:', round(metrics.roc_auc_score(y_test, y_pred),4)))
                               
plt.grid(True)


# 14. Build a logistic regression model using information about heart rate of the patients. Compute the AUC score

df_objects=df.select_dtypes(include = [np.object]).drop('CVD', axis=1)
df_dummies=pd.get_dummies(df_objects, drop_first=True)

df_numbers=df.select_dtypes(include = [np.number]).drop('education', axis=1)
scaler = StandardScaler()
df_scaled=pd.DataFrame(scaler.fit_transform(df_numbers),columns = df_numbers.columns)

X=pd.concat([df_dummies, df_numbers], axis=1)
y=df[['CVD']]
y=y.astype('int')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)
print("shape of X_train:",X_train.shape)
print("shape of X_test:",X_test.shape)
print("shape of y_train:",y_train.shape)
print("shape of y_test:",y_test.shape)

smt = SMOTE()
X_train, y_train = smt.fit_resample(X_train, y_train)
print("shape of X_train:",X_train.shape)
print("shape of y_train:",y_train.shape)

LogRegr = LogisticRegression()
LogRegr.fit(X_train, y_train)
y_pred = LogRegr.predict(X_test)


print("AUC Score:",round(metrics.roc_auc_score(y_test, y_pred),4))

# 15. Calculate the cross entropy for the model built in question 14.
print("Cross Enthrophy(log_loss):",round(metrics.roc_auc_score(y_test, y_pred),4))

# 16. Compare the model built in question 14 to the full model built in question 5.
Model14_AIC=logreg.aic
print("Model5_AIC=", Model5_AIC)
print("Model14_AIC=", Model14_AIC)

# 17. What is the cross entropy for the full model? Use the full model in Q5.
print("Cross Enthrophy(log_loss) for Model in Q5:",Model5_Entrohpy)

# 18. Predict whether a patient has cardiovascular disease based on smoking habits of the patient. For the model find the following:
# Precision
# Recall
# F1 score

X=df[['currentSmoker']]
y=y.astype('int')
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=1)
print("shape of X_train:",X_train.shape)
print("shape of X_test:",X_test.shape)
print("shape of y_train:",y_train.shape)
print("shape of y_test:",y_test.shape)

smt = SMOTE()
X_train, y_train = smt.fit_resample(X_train, y_train)
print("shape of X_train:",X_train.shape)
print("shape of y_train:",y_train.shape)



LogRegr = LogisticRegression()
LogRegr.fit(X_train, y_train)
y_pred = LogRegr.predict(X_test)

print("Precision:",metrics.precision_score(y_test, y_pred))
print("Recall:",metrics.recall_score(y_test, y_pred))
print("f1-score:",metrics.f1_score(y_test, y_pred))

# 4. Determining optimal threshold
# 19. Obtain the optimal value threshold for the full model using the Youden's index.

fpr, tpr, thresholds = roc_curve(y_test, y_pred)

youdens_table = pd.DataFrame({'TPR': tpr,'FPR': fpr,'Threshold': thresholds})
youdens_table['Difference'] = youdens_table.TPR - youdens_table.FPR
youdens_table.sort_values('Difference', ascending = False).reset_index(drop = True)



# 20. Consider the costs of false negatives and false positives as 3 and 1.3 respectively to obtain the optimal cut-off probability for which the total cost will be minimum.

def calculate_total_cost(actual_value, predicted_value, cost_FN, cost_FP):
    cm = confusion_matrix(actual_value, predicted_value)           
    cm_array = np.array(cm)
    return cm_array[1,0] * cost_FN + cm_array[0,1] * cost_FP


y_pred_prob = [ 0 if  x > (cut_off/100) else 1 for x in y_pred]
df_total_cost = pd.DataFrame(columns = ['cut-off', 'total_cost'])
i = 0
for cut_off in range(10, 100):
    total_cost = calculate_total_cost(y_test,  y_pred_prob, 3, 1.3) 
    df_total_cost.loc[i] = [(cut_off/100), total_cost] 
    i += 1
df_total_cost.sort_values('total_cost', ascending = True).head(10)GaussianNB


#----------------------------------------------------------------------------------------------------------------------
### NB - In-Class - Lab Exercise (Session 2) - Question

df = pd.read_csv('bank.csv')

# 1. Remove the outliers (if any).
df.boxplot()
Q1=df.quantile(0.25)
Q3=df.quantile(0.75)
IQR=Q3-Q1
df_final=df[~((df<(Q1-1.5*IQR)) | (df>(Q3+1.5*IQR)))]
df_final.boxplot()



# 2. Separate the dependent and the independent variables. Also, in the target variable, replace yes with 0 and no with 1.
Independent=df_final.drop('y', axis =1)
Dependent["y"]=df_final["y"].apply(lambda x: 0 if x == 'yes' else 1)
Dependent=pd.DataFrame(data=Dependent, columns=['y'])
df_final[["y"]]=Dependent[["y"]]

#3. Replace the value "unknown" from each column with NaN.
df_final.replace(to_replace='unknown',value=np.NaN,inplace=True);


#4. Look for the null values and treat the null values.
df_final.isnull().sum()
df_final.isnull().sum().sort_values(ascending=False)/ df_final.shape[0] * 100
df_final.dropna(inplace=True)
df_final.isnull().sum()

#5. Remove the unnecessary variables that will not contribute to the model.
df_final.shape[0]/df.shape[0]*100
print("We still have around 68% data, so we are good to proceeed")

#6. Plot the distribution of all the numeric variables and find the value of skewness for each variable.
df_final.hist()
df_final.skew()

#7. Plot the distribution of the target variable.
df_final[["y"]].hist()


#8. Scale all the numeric variables using standard scalar.
df_num = df_final.select_dtypes(include = [np.number]).drop('y', axis=1)
df_num.columns
X_scaler = StandardScaler()

num_scaled = X_scaler.fit_transform(df_num)
df_num_scaled = pd.DataFrame(num_scaled, columns = df_num.columns)

df_cat = df_final.select_dtypes(include = [np.object])
df_cat.columns
X = pd.concat([df_num_scaled, df_cat], axis = 1).dropna()
X.head()
y=df_final[["y"]]

# 2. Naive Bayes
#We shall use the bank marketing dataset that we cleaned above
#Before applying classification techniques to predict whether the client subscribed the term deposit or not, let us split the dataset in train and test set.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state=100)

print('X_train', X_train.shape)
print('y_train', y_train.shape)
print('X_test', X_test.shape)
print('y_test', y_test.shape)

#9. Create a function to draw a confusion matrix (heatmap) and a function to plot a roc-auc curve.

def plot_confusion_matrix(model):
    y_pred = model.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    conf_matrix = pd.DataFrame(data = cm,columns = ['Predicted:0','Predicted:1'], index = ['Actual:0','Actual:1'])
    sns.heatmap(conf_matrix, annot = True, fmt = 'd', cmap = ListedColormap(['lightskyblue']), cbar = False, 
                linewidths = 0.1, annot_kws = {'size':25})
    plt.xticks(fontsize = 20)
    plt.yticks(fontsize = 20)
    plt.show()

def plot_roc(model):
    y_pred_prob = model.predict_proba(X_test)[:,1]
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)
    plt.plot(fpr, tpr)
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])
    plt.plot([0, 1], [0, 1],'r--')
    plt.title('ROC curve for Term Deposit Classifier', fontsize = 15)
    plt.xlabel('False positive rate (1-Specificity)', fontsize = 15)
    plt.ylabel('True positive rate (Sensitivity)', fontsize = 15)
    plt.text(x = 0.02, y = 0.9, s = ('AUC Score:',round(roc_auc_score(y_test, y_pred_prob),4)))
    plt.grid(True)

#10. Build a Gaussian naive bayes model and generate a classification report. Also tell how well is the model performing.
Gaussian = GaussianNB()
Gaussian_model = Gaussian.fit(X_train, y_train)
plot_confusion_matrix(Gaussian_model)

y_pred = Gaussian_model.predict(X_test)
print('accuracy_score:',metrics.accuracy_score(y_test, y_pred))
print('kappa_score:',metrics.cohen_kappa_score(y_test, y_pred))
print('kappa_score:',metrics.cohen_kappa_score(y_test, y_pred))
print('recall_score:',metrics.recall_score(y_test, y_pred))

#11. Find the area under the receiver operating characteristic curve and the confusion matrix for the Naive Bayes model built in question 10.
plot_roc(Gaussian_model)

#12. Build a Gaussian Naive Bayes model and perform 10 fold cross validation and find the average accuracy.
tuned_paramaters = {'n_neighbors': np.arange(1, 10, 1),
                   'metric': ['hamming','euclidean','manhattan','Chebyshev']}
knn_classification = KNeighborsClassifier()
knn_grid = GridSearchCV(estimator = knn_classification, 
                        param_grid = tuned_paramaters, 
                        cv = 5, 
                        scoring = 'accuracy')
knn_grid.fit(X_train, y_train)
print('Best parameters for KNN Classifier: ', knn_grid.best_params_, '\n')


#----------------------------------------------------------------------------------------------------------------------
### ML2 - Faculty Notebook (Session 4)  [ Continued from ML2- Faculty Notebook (Session 0)-checkpoint - CHnages Track at 2.7]

#2.7 Train-Test Split
#Before applying various classification techniques to predict the admission status of the student, let us split the dataset in train and test set.

# split data into train subset and test subset
# set 'random_state' to generate the same dataset each time you run the code 
# 'test_size' returns the proportion of data to be included in the test set
X_train, X_test, y_train, y_test = train_test_split(X, df_target, random_state = 10, test_size = 0.2)

# check the dimensions of the train & test subset using 'shape'
# print dimension of train set
print('X_train', X_train.shape)
print('y_train', y_train.shape)

# print dimension of test set
print('X_test', X_test.shape)
print('y_test', y_test.shape)


#Create a generalized function to calculate the metrics for the train and the test set.
# create a generalized function to calculate the metrics values for train set
def get_train_report(model):
    
    # for training set:
    # train_pred: prediction made by the model on the train dataset 'X_train'
    # y_train: actual values of the target variable for the train dataset

    # predict the output of the target variable from the train data 
    train_pred = model.predict(X_train)

    # return the performace measures on train set
    return(classification_report(y_train, train_pred))


# create a generalized function to calculate the metrics values for test set
def get_test_report(model):
    
    # for test set:
    # test_pred: prediction made by the model on the test dataset 'X_test'
    # y_test: actual values of the target variable for the test dataset

    # predict the output of the target variable from the test data 
    test_pred = model.predict(X_test)

    # return the performace measures on test set
    return(classification_report(y_test, test_pred))

# 3. Decision Tree for Classification
# Decision Tree is a non-parametric supervised learning method. It builds a model in the form of a tree structure. It breaks down a dataset into smaller and smaller subsets, which is called splitting. A decision node is a node on which a decision of split is to be made. A node that can not be split further is known as the terminal/leaf node. A leaf node represents the decision. A decision tree can work with both numerical and categorical variables.

# A decision tree for classification is built using criteria like the Gini index and entropy.

# Gini Index
# Gini index measures the probability of the sample being wrongly classified. The value of the Gini index varies between 0 and 1. We choose the variable with a low Gini index. The Gini index of the variable is calculated as:

# 𝐺𝑖𝑛𝑖=1−∑𝑛𝑖=1𝑝2𝑖

# Where,
#𝑝𝑖: Probability of occurrence of the class 'i'

# Entropy
# Entropy is one of the criteria used to build the decision tree. It calculates the heterogeneity of the sample. The entropy is zero if the sample is completely homogeneous, and it is equal to 1 if the sample is equally divided. Entropy of the variable 'X' is calculated as:

# 𝐸(𝑋)=−∑𝑐𝑖=1𝑝𝑖𝑙𝑜𝑔2𝑝𝑖

# Where,
# 𝑝𝑖: Probability of occurrence of the class 'i'

# And the conditional emtropy of the variable is given as:

# 𝐸(𝑇,𝑋)=∑𝑐𝜖𝑋𝑃(𝑐)𝐸(𝑐)

# Where,
# 𝑃(𝑐): Probability of occurrence of the class 'c'
# 𝐸(𝑐): Entropy of the class 'c'

# The information gain is the difference between the entropy of the target variable and the entropy of the target variable given an independent variable. We split the on the variable that corresponds to the highest information gain.

# Build a full decision tree model on a train dataset using 'entropy'.
# instantiate the 'DecisionTreeClassifier' object using 'entropy' criterion
# pass the 'random_state' to obtain the same samples for each time you run the code
decision_tree_classification = DecisionTreeClassifier(criterion = 'entropy', random_state = 10)

# fit the model using fit() on train data
decision_tree = decision_tree_classification.fit(X_train, y_train)
# Plot a decision tree.
# To visualize our decision tree we will use Graphviz. If you are an anaconda user then install it by using conda install graphviz otherwise write the command pip install graphviz.

# save the column names in 'labels'
# labels = X_train.columns

# export a decision tree in DOT format
# pass the 'decision_tree' to export it to Graphviz
# pass the column names to 'feature_names'
# pass the required class labels to 'class_names'
# dot_data = tree.export_graphviz(decision_tree, feature_names = labels, class_names = ["0","1"])  

# plot the decision tree using DOT format in 'dot_data'
graph = pydotplus.graph_from_dot_data(dot_data)  

# display the decision tree
Image(graph.create_png())




#----------------------------------------------------------------------------------------------------------------------
### ML2 - Faculty Notebook (Session 5)  [ vContinues from ML2 - Faculty Notebook (Session 4)]


#Over-fitting in Decision Tree
#The decision tree is said to be over-fitted if it tries to perfectly fit all the observations in the training data. We can calculate the difference between the train and test accuracy to identify if there is over-fitting.

#Calculate performance measures on the train set.

# compute the performance measures on train data
# call the function 'get_train_report'
# pass the decision tree to the function
train_report = get_train_report(decision_tree)

# print the performance measures
print(train_report)


#Calculate performance measures on the test set.

# compute the performance measures on test data
# call the function 'get_test_report'
# pass the decision tree to the function
test_report = get_test_report(decision_tree)

# print the performance measures
print(test_report)
#Interpretation: From the above output, we can see that there is a difference between the train and test accuracy; thus, we can conclude that the decision tree is over-fitted on the train data.

#If we tune the hyperparameters in the decision tree, it helps to avoid the over-fitting of the tree.

#Build a decision tree using 'criterion = gini', 'max_depth = 5', 'min_samples_split = 4', 'max_leaf_nodes = 6'.
# pass the criteria 'gini' to the parameter, 'criterion' 
# max_depth: that assigns maximum depth of the tree
# min_samples_split: assigns minimum number of samples to split an internal node
# max_leaf_nodes': assigns maximum number of leaf nodes in the tree
# pass the 'random_state' to obtain the same samples for each time you run the code

dt_model = DecisionTreeClassifier(criterion = 'gini',
                                  max_depth = 5,
                                  min_samples_split = 4,
                                  max_leaf_nodes = 6,
                                  random_state = 10)

# fit the model using fit() on train data
decision_tree = dt_model.fit(X_train, y_train)

# compute the performance measures on train data
# call the function 'get_train_report'
# pass the decision tree to the function
train_report = get_train_report(decision_tree)

# print the performance measures
print('Train data:\n', train_report)

# compute the performance measures on test data
# call the function 'get_test_report'
# pass the decision tree to the function
test_report = get_test_report(decision_tree)

# print the performance measures
print('Test data:\n', test_report)

#nterpretation: From the above output, we can see that there is slight significant difference between the train and test accuracy; thus, we can conclude that the decision tree is less over-fiited after specifying some of the hyperparameters.


#.1 Tune the Hyperparameters using GridSearchCV (Decision Tree)
#yperparameters are the parameters in the model that are preset by the user. GridSearch considers all the combinations of hyperparameters and returns the best hyperparameter values. We pass some of the hyperparameters in the decision tree to the GridSearchCV() and build the tree using the optimal values obtained using GridSearch method.

# create a dictionary with hyperparameters and its values
# pass the criteria 'entropy' and 'gini' to the parameter, 'criterion' 
# pass the range of values to 'max_depth' that assigns maximum depth of the tree
# 'max_features' assigns maximum number of features to consider for the best split. We pass the string 'sqrt' and 'log2'
# 'sqrt' considers maximum number of features equal to the square root of total features
# 'log2' considers maximum number of features equal to the log of total features with base 2
# pass the range of values to 'min_samples_split' that assigns minimum number of samples to split an internal node
# pass the range of values to 'min_samples_leaf' that assigns minimum number of samples required at the terminal/leaf node
# pass the range of values to 'max_leaf_nodes' that assigns maximum number of leaf nodes in the tree
tuned_paramaters = [{'criterion': ['entropy', 'gini'], 
                     'max_depth': range(2, 10),
                     'max_features': ["sqrt", "log2"],
                     'min_samples_split': range(2,10),
                     'min_samples_leaf': range(1,10),
                     'max_leaf_nodes': range(1, 10)}]
 
# instantiate the 'DecisionTreeClassifier' 
# pass the 'random_state' to obtain the same samples for each time you run the code
decision_tree_classification = DecisionTreeClassifier(random_state = 10)

# use GridSearchCV() to find the optimal value of the hyperparameters
# estimator: pass the decision tree classifier model
# param_grid: pass the list 'tuned_parameters'
# cv: number of folds in k-fold i.e. here cv = 5
tree_grid = GridSearchCV(estimator = decision_tree_classification, 
                         param_grid = tuned_paramaters, 
                         cv = 5)

# fit the model on X_train and y_train using fit()
tree_grid_model = tree_grid.fit(X_train, y_train)

# get the best parameters
print('Best parameters for decision tree classifier: ', tree_grid_model.best_params_, '\n')

## Build the model using the tuned hyperparameters.
# instantiate the 'DecisionTreeClassifier'
# 'best_params_' returns the dictionary containing best parameter values and parameter name  
# 'get()' returns the value of specified parameter
# pass the 'random_state' to obtain the same samples for each time you run the code
dt_model = DecisionTreeClassifier(criterion = tree_grid_model.best_params_.get('criterion'),
                                  max_depth = tree_grid_model.best_params_.get('max_depth'),
                                  max_features = tree_grid_model.best_params_.get('max_features'),
                                  max_leaf_nodes = tree_grid_model.best_params_.get('max_leaf_nodes'),
                                  min_samples_leaf = tree_grid_model.best_params_.get('min_samples_leaf'),
                                  min_samples_split = tree_grid_model.best_params_.get('min_samples_split'),
                                  random_state = 10)

# use fit() to fit the model on the train set
dt_model = dt_model.fit(X_train, y_train)
Plot the decision tree with tuned hyperparameters.

# save the column names in 'labels'
labels = X_train.columns

# export a decision tree in DOT format
# pass the 'dt_model' to export it to Graphviz
# pass the column names to 'feature_names'
# pass the required class labels to 'class_names'
dot_data = tree.export_graphviz(dt_model, feature_names = labels, class_names = ["0","1"])  

# plot the decision tree using DOT format in 'dot_data'
graph = pydotplus.graph_from_dot_data(dot_data)  

# display the decision tree
Image(graph.create_png())

# double-click on the image below to get an expanded view
# Interpretation: Initially the split is at the variable GRE Score <= 319.5. Thus, for the student if the GRE score is less than or equal to 319.5; it will satisfy the condition and further check the condition on the left internal node. i.e. TOEFL Score <= 106.5. On the other hand, if the GRE score is greater than 319.5; the tree checks for the condition on the right internal node. i.e. University Rating <= 3.5.

# For a node, entropy represents the entopy of the target variable. samples represents the number of samples in the node. Value indicates the number of samples in each class of the target variable, and class represents the label of the majority class in the node.

# Calculate performance measures on the train set.

# print the performance measures for train set for the model with best parameters
# call the function 'get_test_report'
# pass the decision tree using GridSearch to the function

print('Classification Report for train set: \n', get_train_report(dt_model))

# Calculate performance measures on the test set.
# print the performance measures for test set for the model with best parameters
# call the function 'get_test_report'
# pass the decision tree using GridSearch to the function

print('Classification Report for test set: \n', get_test_report(dt_model))

# Interpretation: From the above output, we can see that there is no significant difference between the train and test accuracy; thus, we can conclude that the decision tree after tuning the hyperparameters avoids the over-fitting of the data.

# 4. Random Forest for Classification
# It is the method of constructing multiple decision trees on randomly selected data samples. We can use the bootstrap sampling method to select the random samples of the same size from the dataset to construct multiple trees. This method is used for both regression and classification analysis. The random forest returns the prediction based on all the individual decision trees prediction. For regression, it returns the average of all the predicted values; and for classification, it returns the class, which is the mode of all the predicted classes.

# It avoids the over-fitting problem as it considers a random data sample to construct a decision tree.

# instantiate the 'RandomForestClassifier'
# pass the required number of trees in the random forest to the parameter, 'n_estimators'
# pass the 'random_state' to obtain the same samples for each time you run the code
rf_classification = RandomForestClassifier(n_estimators = 10, random_state = 10)

# use fit() to fit the model on the train set
rf_model = rf_classification.fit(X_train, y_train)

# Calculate performance measures on the train set.

# compute the performance measures on train data
# call the function 'get_train_report'
# pass the random forest model to the function
train_report = get_train_report(rf_model)

# print the performace measures
print(train_report) 
# Calculate performance measures on the test set.

# compute the performance measures on test data
# call the function 'get_test_report'
# pass the random forest model to the function
test_report = get_test_report(rf_model)

# print the performace measures
print(test_report) 

# 4.1 Tune the Hyperparameters using GridSearchCV (Random Forest)
# create a dictionary with hyperparameters and its values
# pass the criteria 'entropy' and 'gini' to the parameter, 'criterion' 
# pass a list of values to 'n_estimators' to build the different number of trees in the random forest
# pass a list of values to 'max_depth' that assigns maximum depth of the tree
# 'max_features' assigns maximum number of features to consider for the best split. We pass the string 'sqrt' and 'log2'
# 'sqrt' considers maximum number of features equal to the square root of total features
# 'log2' considers maximum number of features equal to the log of total features with base 2
# pass a list of values to 'min_samples_split' that assigns minimum number of samples to split an internal node
# pass a list of values to 'min_samples_leaf' that assigns minimum number of samples required at the terminal/leaf node
# pass a list of values to 'max_leaf_nodes' that assigns maximum number of leaf nodes in the tree
tuned_paramaters = [{'criterion': ['entropy', 'gini'],
                     'n_estimators': [10, 30, 50, 70, 90],
                     'max_depth': [10, 15, 20],
                     'max_features': ['sqrt', 'log2'],
                     'min_samples_split': [2, 5, 8, 11],
                     'min_samples_leaf': [1, 5, 9],
                     'max_leaf_nodes': [2, 5, 8, 11]}]

 
# instantiate the 'RandomForestClassifier' 
# pass the 'random_state' to obtain the same samples for each time you run the code
random_forest_classification = RandomForestClassifier(random_state = 10)

# use GridSearchCV() to find the optimal value of the hyperparameters
# estimator: pass the random forest classifier model
# param_grid: pass the list 'tuned_parameters'
# cv: number of folds in k-fold i.e. here cv = 5
rf_grid = GridSearchCV(estimator = random_forest_classification, 
                       param_grid = tuned_paramaters, 
                       cv = 5)

# use fit() to fit the model on the train set
rf_grid_model = rf_grid.fit(X_train, y_train)

# get the best parameters
print('Best parameters for random forest classifier: ', rf_grid_model.best_params_, '\n')


# Build the model using the tuned hyperparameters.
# instantiate the 'RandomForestClassifier'
# 'best_params_' returns the dictionary containing best parameter values and parameter name  
# 'get()' returns the value of specified parameter
# pass the 'random_state' to obtain the same samples for each time you run the code

rf_model = RandomForestClassifier(criterion = rf_grid_model.best_params_.get('criterion'), 
                                  n_estimators = rf_grid_model.best_params_.get('n_estimators'),
                                  max_depth = rf_grid_model.best_params_.get('max_depth'),
                                  max_features = rf_grid_model.best_params_.get('max_features'),
                                  max_leaf_nodes = rf_grid_model.best_params_.get('max_leaf_nodes'),
                                  min_samples_leaf = rf_grid_model.best_params_.get('min_samples_leaf'),
                                  min_samples_split = rf_grid_model.best_params_.get('min_samples_split'),
                                  random_state = 10)

# use fit() to fit the model on the train set
rf_model = rf_model.fit(X_train, y_train)


# print the performance measures for test set for the model with best parameters
print('Classification Report for test set:\n', get_test_report(rf_model))
# Interpretation: The accuracy of the test dataset increased from 0.81 to 0.84 after tuning of the hyperparameters. Also, the sensitivity and specificity of the model are balanced.

# Identify the Important Features
# Let us create a barplot to identify the important feature in the dataset.

# The method feature_importances_ returns the value corresponding to each feature which is defined as the ratio of total decrease in Gini impurity across every tree in the forest where the feature is used to the total count of trees in the forest. This is also caled as, Gini Importance.

# There is another accuracy-based method. It calculates the average decrease in the accuracy calculated on the out-of-bag samples, with and without shuffling the variable across all the trees in the random forest. The out-of-bag samples are the samples in the training dataset which are not considered whild building a tree.

# create a dataframe that stores the feature names and their importance
# 'feature_importances_' returns the features based on the gini importance

important_features = pd.DataFrame({'Features': X_train.columns, 
                                   'Importance': rf_model.feature_importances_})

# sort the dataframe in the descending order according to the feature importance
important_features = important_features.sort_values('Importance', ascending = False)


# create a barplot to visualize the features based on their importance
sns.barplot(x = 'Importance', y = 'Features', data = important_features)
plt.title('ROC curve for Admission Prediction Classifier', fontsize = 15)

# add plot and axes labels
# set text size using 'fontsize'
plt.title('Feature Importance', fontsize = 15)
plt.xlabel('Importance', fontsize = 15)
plt.ylabel('Features', fontsize = 15)

# display the plot
plt.show()
# Interpretation: From the above bar plot, we can see that CGPA is the most important feature in the dataset.


#----------------------------------------------------------------------------------------------------------------------
### ML2 - Faculty Notebook (Session 6) [ continuation from ML2 - Faculty Notebook (Session 5)]


# 3. Boosting Methods
# The Ensemble technique considers multiple models for predicting the results. Bagging and Boosting are two of the types of ensembles. The bagging methods construct the multiple models in parallel; whereas, the boosting methods construct the models sequentially.

#Earlier, we have studied one of the bagging (bootstrap aggregating) technique i.e. Random Forest.

#The boosting method fits multiple weak classifiers to create a strong classifier. In this method, the model tries to correct the errors in the previous model. In this section, we learn some of the boosting methods such as AdaBoost, Gradient Boosting and XGBoost.


#3.1 AdaBoost
#Let us build the AdaBoost classifier with decision trees. The model creates several stumps (decision tree with only a single decision node and two leaf nodes) on the train set and predicts the class based on these weak learners (stumps). For the first model, it assigns equal weights to each sample. It assigns the higher weight for the wrongly predicted samples and lower weight for the correctly predicted samples. This method continues till all the observations are correctly classified or the predefined number of stumps is created.

#Build an Adaboost model on a training dataset.
# instantiate the 'AdaBoostClassifier'
# n_estimators: number of estimators at which boosting is terminated
# pass the 'random_state' to obtain the same results for each code implementation
ada_model = AdaBoostClassifier(n_estimators = 40, random_state = 10)

# fit the model using fit() on train data
ada_model.fit(X_train, y_train)

#Let us understand the parameters in the AdaBoostClassifier():

#algorithm=SAMME.R: It is the default boosting algorithm. This algorithm uses predicted class probabilities to build the stumps.

#base_estimator=None: By default, the estimator is a decision tree with a maximum depth equal to 1 (stump).
#learning_rate=1.0: It considers the contribution of each estimator in the classifier.
#n_estimators=40: It is the number of estimators at which boosting is terminated.
#random_state=10: It returns the same set of samples for each code implementation.

print(get_train_report(ada_model))
#Plot the confusion matrix.
# call the function to plot the confusion matrix
# pass the AdaBoost model to the function

plot_confusion_matrix(ada_model)


#Calculate performance measures on the test set.
# compute the performance measures on test data
# call the function 'get_test_report'
# pass the AdaBoost model to the function
test_report = get_test_report(ada_model)

# print the performance measures
print(test_report)


#Interpretation: The output shows that the model is 81% accurate.

#Plot the ROC curve.
# call the function to plot the ROC curve
# pass the AdaBoost model to the function

plot_roc(ada_model)

#Interpretation: The red dotted line represents the ROC curve of a purely random classifier; a good classifier stays as far away from that line as possible (toward the top-left corner).
#From the above plot, we can see that the AdaBoost model is away from the dotted line; with the AUC score 0.9132.


#3.2 Gradient Boosting
#This method optimizes the differentiable loss function by building the number of weak learners (decision trees) sequentially. It considers the residuals from the previous model and fits the next model to the residuals. The algorithm uses a gradient descent method to minimize the error.

#Build a gradient boosting model on a training dataset.
# instantiate the 'GradientBoostingClassifier' 
# n_estimators: number of estimators to consider
# 'max_depth': assigns maximum depth of the tree
# pass the 'random_state' to obtain the same results for each code implementation

gboost_model = GradientBoostingClassifier(n_estimators = 150, max_depth = 10, random_state = 10)

# fit the model using fit() on train data
gboost_model.fit(X_train, y_train)

#Let us understand the parameters in the GradientBoostingClassifier():

#ccp_alpha=0.0: The complexity parameter used for pruning. By default, there is no pruning.
#criterion=friedman_mse: The criteria to measure the quality of a split.
#init=None: The estimator for initial predictions.
#learning_rate=0.1: It considers the contribution of each estimator in the classifier.
#loss=deviance: The loss function to be optimized.
#max_depth=10: Assigns the maximum depth of the tree.
#max_features=None: Maximum features to consider for the split.
#max_leaf_nodes=None: Maximum number of leaf/terminal nodes in the tree.
#min_impurity_decrease=0.0: A node splits if it decreases the impurity by the value given by this parameter.
#min_impurity_split=None: Minimum value of impurity for a node to split.
#min_samples_leaf=1: Minimum number of samples needed at the leaf/terminal node.
#min_samples_split=2: Minimum number of samples needed at the internal node to split.
#min_weight_fraction_leaf=0.0: Minimum weighted fraction needed at a leaf node.
#n_estimators=150: The number of estimators to consider.
#n_iter_no_change=None: Number of iterations after which the training should terminate if the score is not improving.
#presort='deprecated': It considers whether to presort the data. (This parameter may not be available in the latest versions).
#random_state=10: It returns the same set of samples for each code implementation.
#subsample=1.0: Fraction of samples to use for fitting each estimator.
#tol=0.0001: Value of tolerance to terminate the training.
#validation_fraction=0.1: Fraction of training dataset used for validation.
#verbose=0: Enables verbose output (by default, no progress will be printed).
#warm_start=False: Whether to reuse the solution of previous code implementation (by default, it does not consider the previous solution).

#Plot the confusion matrix.
# call the function to plot the confusion matrix
# pass the gradient boosting model to the function

plot_confusion_matrix(gboost_model)


#Calculate performance measures on the test set.

# compute the performance measures on test data
# call the function 'get_test_report'
# pass the gradient boosting model to the function
test_report = get_test_report(gboost_model)

# print the performance measures
print(test_report)
#Interpretation: The classification report shows that the model is 79% accurate. Also, the sensitivity and specificity are equal.

#Plot the ROC curve.
# call the function to plot the ROC curve
# pass the gradient boosting model to the function
plot_roc(gboost_model)

#Interpretation: The red dotted line represents the ROC curve of a purely random classifier; a good classifier stays as far away from that line as possible (toward the top-left corner).
#From the above plot, we can see that the gradient boosting model is away from the dotted line; with the AUC score 0.8954.


#3.3 XGBoost
#XGBoost (extreme gradient boost) is an alternative form of gradient boosting method. This method generally considers the initial prediction as 0.5 and build the decision tree to predict the residuals. It considers the regularization parameter to avoid overfitting.

#Build an XGBoost model on a training dataset.
# instantiate the 'XGBClassifier'
# set the maximum depth of the tree using the parameter, 'max_depth'
# pass the value of minimum loss reduction required for partition of the leaf node to the parameter, 'gamma'
xgb_model = XGBClassifier(max_depth = 10, gamma = 1)

# fit the model using fit() on train data
xgb_model.fit(X_train, y_train)

#Let us understand the parameters in the XGBClassifier():

#base_score=0.5: Initial prediction for base learners.
#booster=gbtree: Considers the regression tree as the base learners.
#colsample_bylevel=1: Fraction of variables to consider for each level.
#colsample_bynode=1: Fraction of variables to consider for each split.
#colsample_bytree=1: Fraction of variables to consider for each tree.
#gamma=1: Value of minimum loss reduction required for the partition of the leaf node.
#gpu_id=-1: It considers all the GPU's.
#importance_type=gain: Importance type for calculating feature importance.
#interaction_constraints='': By default, no interaction between the features is allowed.
#learning_rate=0.300000012: It considers the contribution of each estimator in the classifier.
#max_delta_step=0: Maximum delta step allowed for each tree's weight estimation to be.
#max_depth=10: Maximum depth of each tree.
#min_child_weight=1: Minimum sum of hessian (p*(1-p)) required in a leaf node.
#missing=nan: Value to consider as a missing value.
#monotone_constraints='()': Constraint of variable monotonicity. (adding increasing/decreasing constraint on the variables )
#n_estimators=100: The number of estimators to consider.
#n_jobs=0: Number of parallel threads to run the classifier.
#num_parallel_tree=1: It is used for boosting random forest.
#objective='binary:logistic': Considers the binary logistic regression as a learning objective.
#random_state=0: It returns the same set of samples for each code implementation.
#reg_alpha=0: Lasso regularization term for weights.
#reg_lambda=1: Ridge regularization term for weights.
#scale_pos_weight=1: Ratio of the number of negative class to the positive class.
#subsample=1: Fraction of total training data points.
#tree_method='exact': Considers the exact greedy algorithm.
#validate_parameters=1: Performs validation on input paramerters.
#verbosity=None: Enables verbose output (by default, no progress will be printed).

#Plot the confusion matrix.
# call the function to plot the confusion matrix
# pass the XGBoost model to the function
plot_confusion_matrix(xgb_model)

#Calculate performance measures on the test set.

print(get_train_report(xgb_model))
# compute the performance measures on test data
# call the function 'get_test_report'
# pass the XGBoost model to the function
test_report = get_test_report(xgb_model)

# print the performance measures
print(test_report)
#Interpretation: The above output shows that the f1-score and accuracy of the model is 0.84

##Plot the ROC curve.
# call the function to plot the ROC curve
# pass the XGBoost model to the function

plot_roc(xgb_model)

#Interpretation: The red dotted line represents the ROC curve of a purely random classifier; a good classifier stays as far away from that line as possible (toward the top-left corner).
#From the above plot, we can see that the XGBoost model is away from the dotted line; with the AUC score 0.8888.


#3.3.1 Tune the Hyperparameters (GridSearchCV)
#Let us tune the hyperparameters to obtain the optimal values for the XGBoost model.

# create a dictionary with hyperparameters and its values
# learning_rate: pass the list of boosting learning rates
# max_depth: pass the range of values as the maximum tree depth for base learners
# gamma: pass the list of minimum loss reduction values required to make a further partition on a leaf node of the tree
tuning_parameters = {'learning_rate': [0.1, 0.2, 0.3, 0.4, 0.5, 0.6],
                     'max_depth': range(3,10),
                     'gamma': [0, 1, 2, 3, 4]}

# instantiate the 'XGBClassifier' 
xgb_model = XGBClassifier()

# use GridSearchCV() to find the optimal value of the hyperparameters
# estimator: pass the XGBoost classifier model
# param_grid: pass the list 'tuned_parameters'
# cv: number of folds in k-fold i.e. here cv = 3
# scoring: pass a measure to evaluate the model on test set
xgb_grid = GridSearchCV(estimator = xgb_model, param_grid = tuning_parameters, cv = 3, scoring = 'roc_auc')

# fit the model on X_train and y_train using fit()
xgb_grid.fit(X_train, y_train)

# get the best parameters
print('Best parameters for XGBoost classifier: ', xgb_grid.best_params_, '\n')

#Build the model using the tuned hyperparameters.
# instantiate the 'XGBClassifier'
# 'best_params_' returns the dictionary containing best parameter values and parameter name  
# 'get()' returns the value of specified parameter
xgb_grid_model = XGBClassifier(learning_rate = xgb_grid.best_params_.get('learning_rate'),
                               max_depth = xgb_grid.best_params_.get('max_depth'),
                              gamma = xgb_grid.best_params_.get('gamma'))

# use fit() to fit the model on the train set
xgb_model = xgb_grid_model.fit(X_train, y_train)

# print the performance measures for test set for the model with best parameters
print('Classification Report for test set:\n', get_test_report(xgb_model))
print(get_train_report(xgb_grid_model))


#Interpretation: The above output shows that the f1-score and accuracy of the model is 0.84.

#Plot the ROC curve.
# call the function to plot the ROC curve
# pass the XGBoost model to the function
plot_roc(xgb_model)

#Interpretation: The red dotted line represents the ROC curve of a purely random classifier; a good classifier stays as far away from that line as possible (toward the top-left corner).
#From the above plot, we can see that the XGBoost model (GridSearchCV) is away from the dotted line; with the AUC score 0.9145.

#Identify the Important Features using XGBoost
#Let us create a barplot to identify the important feature in the dataset.

#The method feature_importances_ returns the value corresponding to each feature which is defined as the ratio of the average gain across all the splits in which the feature is used to the total average gain of all the features.

#There are different methods like weight, cover, total_gain and total_cover which returns the feature importance based on different criteria.

#weight: It is the frequency of a feature used to split the data in all the trees.
#cover: It is the average cover value of a feature for all the splits.
#total_gain: It is the sum of gain of a feature for all the splits.
#total_cover: It is the sum of a cover of a feature for all the splits.

# create a dataframe that stores the feature names and their importance
# 'feature_importances_' returns the features based on the average gain 
important_features = pd.DataFrame({'Features': X_train.columns, 
                                   'Importance': xgb_model.feature_importances_})

# sort the dataframe in the descending order according to the feature importance
important_features = important_features.sort_values('Importance', ascending = False)

# create a barplot to visualize the features based on their importance
sns.barplot(x = 'Importance', y = 'Features', data = important_features)

# add plot and axes labels
# set text size using 'fontsize'
plt.title('Feature Importance', fontsize = 15)
plt.xlabel('Importance', fontsize = 15)
plt.ylabel('Features', fontsize = 15)

# display the plot
plt.show()

#Interpretation: The above bar plot shows that, the variable CGPA is of highest importance.


4. Stack Generalization
#Stacking is a machine learning technique that takes several classification or regression models and uses their predictions as the input for the meta-classifier (final classifier) or meta-regressor (final regressor).

#As we are using the distance-based algorithm like KNN, we scale the data before applying the stacking technique.

# initialize the standard scalar
X_scaler = StandardScaler()

# scale all the numerical columns
# standardize all the columns of the dataframe 'df_num'
num_scaled = X_scaler.fit_transform(df_num)

# create a dataframe of scaled numerical variables
# pass the required column names to the parameter 'columns'
df_num_scaled = pd.DataFrame(num_scaled, columns = df_num.columns)
df_num
df_num.loc[0,:]
X_scaler.transform(df_num.loc[0:1,:])
X_scaler.transform([[337,118,4,4.5,4.5,9.65]])


#Concatenate scaled numerical and dummy encoded categorical variables.

# concat the dummy variables with scaled numeric features to create a dataframe of all independent variables
# 'axis=1' concats the dataframes along columns 
X = pd.concat([df_num_scaled, dummy_var], axis = 1)

# display first five observations
X.head()
df_num.head(n=1)

#Let us split the dataset in train and test set.

# split data into train subset and test subset
# set 'random_state' to generate the same dataset each time you run the code 
# 'test_size' returns the proportion of data to be included in the test set
X_train, X_test, y_train, y_test = train_test_split(X, df_target, random_state = 10, test_size = 0.2)

# check the dimensions of the train & test subset using 'shape'
# print dimension of train set

print('X_train', X_train.shape)
print('y_train', y_train.shape)

# print dimension of test set
print('X_test', X_test.shape)
print('y_test', y_test.shape)

#Build the stacking classifier using the Random forest, KNN and Naive bayes as base learners (consider the hyperparameters tuned using GridSearchCV in the previous sessions).
# consider the various algorithms as base learners
base_learners = [('rf_model', RandomForestClassifier(criterion = 'entropy', max_depth = 10, max_features = 'sqrt', 
                                                     max_leaf_nodes = 8, min_samples_leaf = 5, min_samples_split = 2, 
                                                     n_estimators = 50, random_state = 10)),
                 ('KNN_model', KNeighborsClassifier(n_neighbors = 17, metric = 'euclidean')),
                 ('NB_model', GaussianNB())]

# initialize stacking classifier 
# pass the base learners to the parameter, 'estimators'
# pass the Naive Bayes model as the 'final_estimator'/ meta model
stack_model = StackingClassifier(estimators = base_learners, final_estimator = GaussianNB())


# fit the model on train dataset
stack_model.fit(X_train, y_train)
Plot the confusion matrix.

# call the function to plot the confusion matrix
# pass the stack model to the function
plot_confusion_matrix(stack_model)
Calculate performance measures on the test set.

# compute the performance measures on test data
# call the function 'get_test_report'
# pass the XGBoost model to the function
test_report = get_test_report(stack_model)

# print the performance measures
print(test_report)

#Interpretation: The above output shows that the f1-score and accuracy of the model is 0.86

##Plot the ROC curve.
# call the function to plot the ROC curve
# pass the stack model to the function
plot_roc(stack_model)


#Interpretation: The red dotted line represents the ROC curve of a purely random classifier; a good classifier stays as far away from that line as possible (toward the top-left corner).
#From the above plot, we can see that the stacking model is away from the dotted line; with the AUC score 0.9492.

import pickle
with open('admission.pickle', 'wb') as file:
    pickle.dump(stack_model,file)
with open('scaler.pickle', 'wb') as file:
    pickle.dump(X_scaler,file)


#----------------------------------------------------------------------------------------------------------------------
### Naive+Bayesian+Pima+Diabetes+



url = "https://archive.ics.uci.edu/ml/machine-learning-databases/pima-indians-diabetes/pima-indians-diabetes.data"
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(url, names=names)

array = dataframe.values
X = array[:,0:8] # select all rows and first 7 columns which are the attributes
Y = array[:,8]   # select all rows and the 8th column which is the classification "Yes", "No" for diabeties
test_size = 0.30 # taking 70:30 training and test set
seed = 7  # Random numbmer seeding for reapeatability of the code
X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size=test_size, random_state=seed)




model = GaussianNB()
model.fit(X_train, Y_train)
print(model)
# make predictions
expected = Y_test
predicted = model.predict(X_test)
# summarize the fit of the model
print(metrics.classification_report(expected, predicted))
print(metrics.confusion_matrix(expected, predicted))

#Precision: Within a given set of positively-labeled results, the fraction that were true positives = tp/(tp + fp) Recall: Given a set of positively-labeled results, the fraction of all positives that were retrieved = tp/(tp + fn) Accuracy: tp + tn / (tp + tn + fp +fn) But this measure can be dominated by larger class. Suppose 10, 90 and 80 of 90 is correctly predicted while only 2 of 0 is predicted correctly. Accuracy is 80+2 / 100 i.e. 82%
#TO over come the dominance of the majority class, use weighted measure (not shown)
#F is harmonic mean of precision and recal given by ((B^2 +1) PR) / (B^2P +R) When B is set to 1 we get F1 = 2PR / (P+R)

#----------------------------------------------------------------------------------------------------------------------
### pimadiabetes_dt


# load dataset
pima = pd.read_csv("diabetes.csv")
# load dataset
pima = pd.read_csv("diabetes.csv")
pima.head()
#split dataset in features and target variable
feature_cols = ['Pregnancies', 'Insulin', 'BMI', 'Age','Glucose','BloodPressure','DiabetesPedigreeFunction','SkinThickness']
X = pima[feature_cols] # Features
y = pima.Outcome # Target variable
# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test
# Create Decision Tree classifer object
clf = DecisionTreeClassifier(criterion='entropy')

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)
clf
# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO  
from IPython.display import Image  
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('diabetes.png')
Image(graph.create_png()
from sklearn.tree import export_graphviz
from sklearn.externals.six import StringIO  
from IPython.display import Image  
import pydotplus

dot_data = StringIO()
export_graphviz(clf, out_file=dot_data,  
                filled=True, rounded=True,
                special_characters=True,feature_names = feature_cols,class_names=['0','1'])
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('diabetes.png')
Image(graph.create_png())



#----------------------------------------------------------------------------------------------------------------------
### poisnous_mushroom_detection

df = pd.read_csv('mushrooms.csv')
df.shape
df.columns
df.head(5)
labelencoder=LabelEncoder()
for column in df.columns:
    df[column] = labelencoder.fit_transform(df[column])
df.describe()
df=df.drop(["veil-type"],axis=1)
plt.figure()
pd.Series(df['class']).value_counts().sort_index().plot(kind = 'bar')
plt.ylabel("Count")
plt.xlabel("class")
plt.title('Number of poisonous/edible mushrooms (0=edible, 1=poisonous)');
X=df.drop(['class'], axis=1)
Y=df['class']
X_train, X_test,Y_train,Y_test = train_test_split(X,Y, test_size = 0.1)
from sklearn.naive_bayes import GaussianNB

clf_GNB = GaussianNB()
clf_GNB = clf_GNB.fit(X_train, Y_train)
y_pred_GNB=clf_GNB.predict(X_test)
y_pred_GNB
from sklearn.metrics import accuracy_score
accuracy_score(Y_test, y_pred_GNB)
from sklearn.metrics import confusion_matrix
confusion_matrix = confusion_matrix(Y_test, y_pred_GNB)
print(confusion_matrix)




#----------------------------------------------------------------------------------------------------------------------
### Polynomialfeaures_creation
X = np.arange(6).reshape(3, 2)


from sklearn.preprocessing import PolynomialFeatures
poly = PolynomialFeatures(2)
poly.fit_transform(X)
poly = PolynomialFeatures(2,interaction_only=True)
poly.fit_transform(X)




#----------------------------------------------------------------------------------------------------------------------
### randomforest_diebetes



from sklearn.ensemble import RandomForestClassifier
from sklearn import model_selection
X = array[:,0:8]
Y = array[:,8]
seed = 7
kfold = model_selection.KFold(n_splits=10)
num_trees = 100
max_features = 3
model = RandomForestClassifier(n_estimators=num_trees, max_features=max_features)
results = model_selection.cross_val_score(model, X, Y, cv=kfold)
print(results.mean())

      
      
#----------------------------------------------------------------------------------------------------------------------
### ROC_Threshold_Management+29


# Evaluating a classification model
# read the data into a Pandas DataFrame
col_names = ['pregnant', 'glucose', 'bp', 'skin', 'insulin', 'bmi', 'pedigree', 'age', 'label']
pima = pd.read_csv('d:\gli\ml-data\pima-indians-diabetes.data', header=None, names=col_names)
# print the first 5 rows of data
pima.head()

# define X and y
feature_cols = ['pregnant','glucose', 'bp', 'skin', 'insulin', 'bmi', 'age']
X = pima[feature_cols]
y = pima.label

# split X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y , random_state=1)

# train a logistic regression model on the training set
from sklearn.linear_model import LogisticRegression
logreg = LogisticRegression()
logreg.fit(X_train, y_train)
      
# make class predictions for the testing set
y_pred_class = logreg.predict(X_test)

#Classification accuracy: percentage of correct predictions

# calculate accuracy
      
from sklearn import metrics
print(metrics.accuracy_score(y_test, y_pred_class))
      
#Confusion matrix
#Table that describes the performance of a classification model

cm = metrics.confusion_matrix(y_test, y_pred_class)
plt.clf()
plt.imshow(cm, interpolation='nearest', cmap=plt.cm.Wistia)
classNames = ['Non_diabetic','Diabetic']
plt.title('Confusion Matrix - Test Data')
plt.ylabel('Actual label')
plt.xlabel('Predicted label')
tick_marks = np.arange(len(classNames))
plt.xticks(tick_marks, classNames, rotation=45)
plt.yticks(tick_marks, classNames)
s = [['TN','FP'], ['FN', 'TP']]
 
for i in range(2):
    for j in range(2):
        plt.text(j,i, str(s[i][j])+" = "+str(cm[i][j]))

plt.show()
TP = 40
TN = 110
FP = 13
FN = 29
      
#Metrics computed from a confusion matrix
#Classification Accuracy: Overall, how often is the classifier correct?

print((TP + TN) / float(TP + TN + FP + FN))
print(metrics.accuracy_score(y_test, y_pred_class))
      
#Classification Error: Overall, how often is the classifier incorrect?

#Also known as "Misclassification Rate"
print((FP + FN) / float(TP + TN + FP + FN))
print(1 - metrics.accuracy_score(y_test, y_pred_class))
      
#Sensitivity: When the actual value is positive, how often is the prediction correct?

#How "sensitive" is the classifier to detecting positive instances?
#Also known as "True Positive Rate" or "Recall"
print(TP / float(TP + FN))
print(metrics.recall_score(y_test, y_pred_class))
      
#Specificity: When the actual value is negative, how often is the prediction correct?
#How "specific" (or "selective") is the classifier in predicting positive instances?
print(TN / float(TN + FP))
      
#False Positive Rate: When the actual value is negative, how often is the prediction incorrect?
print(FP / float(TN + FP))
      
#Precision: When a positive value is predicted, how often is the prediction correct?
#How "precise" is the classifier when predicting positive instances?
print(TP / float(TP + FP))
print(metrics.precision_score(y_test, y_pred_class))
      
#Adjusting the classification threshold
# print the first 10 predicted class with default threshold of .5
logreg.predict(X_test)[0:10]
      
# print the first 10 predicted probabilities of class membership
logreg.predict_proba(X_test)[0:10, :]
      
# print the first 10 predicted probabilities for class 1  (diabetics)
logreg.predict_proba(X_test)[0:10, 1]
      
# store the predicted probabilities for diabetic class for all records... 
y_pred_prob = logreg.predict_proba(X_test)[:, 1]
      
#Reduce the threshold from .5 to .3 to predict the diabetics class. This will make the model sensitive to diabetic class
# predict diabetes if the predicted probability is greater than 0.3
from sklearn.preprocessing import binarize
y_pred_class = binarize([y_pred_prob], 0.3)[0]  # deciding the class of the 1st 10 records based on new threshold
      
# print the first 10 predicted probabilities
y_pred_prob[0:10]
      
# print the first 10 predicted classes with the lower threshold. Note the change in class...
# with threshold of .5 (default) , the first data point would belong to 0 class i.e. non-diabetic 
y_pred_class[0:10]
      
# previous confusion matrix (default threshold of 0.5)
print(metrics.confusion_matrix(y_test, y_pred_class))
      
# sensitivity has increased (used to be 0.24)
print(46 / float(46 + 16))
      
# specificity has decreased (used to be 0.91)
print(80 / float(80 + 50))
      
# Observations:
#Default threshold of .5 is not sensitive towards diabetic class. Lowering the threshold increases the sensitivity to
#diabetic class
#ROC Curves and Area Under the Curve (AUC)

#Question: Wouldn't it be nice if we could see how sensitivity and specificity are affected by various thresholds, without actually changing the threshold?

#Answer: Plot the ROC curve!

# IMPORTANT: first argument is true values, second argument is predicted probabilities

import matplotlib.pyplot as plt
fpr, tpr, thresholds = metrics.roc_curve(y_test, y_pred_prob)
plt.plot(fpr, tpr)
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])
plt.title('ROC curve for diabetes classifier')
plt.xlabel('False Positive Rate (1 - Specificity)')
plt.ylabel('True Positive Rate (Sensitivity)')
plt.grid(True)
      
#ROC curve can help you to choose a threshold that balances sensitivity and specificity in a way that makes sense for your particular context
#You can't actually see the thresholds used to generate the curve on the ROC curve itself
# define a function that accepts a threshold and prints sensitivity and specificity
def evaluate_threshold(threshold):
    print('Sensitivity:', tpr[thresholds > threshold][-1])
    print('Specificity:', 1 - fpr[thresholds > threshold][-1])
evaluate_threshold(0.5)
evaluate_threshold(0.3)
      
#AUC is the percentage of the ROC plot that is underneath the curve:

# IMPORTANT: first argument is true values, second argument is predicted probabilities
print(metrics.roc_auc_score(y_test, y_pred_prob))
      
#AUC is useful as a single number summary of classifier performance.
#If you randomly chose one positive and one negative observation, AUC represents the likelihood that your classifier will assign a higher predicted probability to the positive observation.
#AUC is useful even when there is high class imbalance (unlike classification accuracy).
# calculate cross-validated AUC
from sklearn.cross_validation import cross_val_score
cross_val_score(logreg, X, y, cv=10, scoring='roc_auc').mean()
      
#Confusion matrix advantages:
#Allows you to calculate a variety of metrics
#Useful for multi-class problems (more than two response classes)
#ROC/AUC advantages:

#Does not require you to set a classification threshold
#Still useful when there is high class imbalance
      
      
      
#----------------------------------------------------------------------------------------------------------------------
### SMOTE-NEARMISS

bank = pd.read_csv("bank-full.csv", sep = ";", na_values = "unknown")
bank.head()
bank.shape
bank.columns
bank["default"] = bank["default"].map({"no":0,"yes":1})
bank["housing"] = bank["housing"].map({"no":0,"yes":1})
bank["loan"] = bank["loan"].map({"no":0,"yes":1})
bank["y"] = bank["y"].map({"no":0,"yes":1})
bank.education = bank.education.map({"primary": 0, "secondary":1, "tertiary":2})
bank.month = pd.to_datetime(bank.month, format = "%b").dt.month
bank.isnull().sum()
bank.drop(["poutcome", "contact"], axis = 1, inplace = True)
bank.dropna(inplace = True)
bank = pd.get_dummies(bank, drop_first = True)
bank.y.value_counts()
X = bank.drop("y", axis = 1)
y = bank.y
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 1, stratify=y)
y_train.value_counts()
lr = LogisticRegression()
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)

print(confusion_matrix(y_test, y_pred))

print(accuracy_score(y_test, y_pred))

print(recall_score(y_test, y_pred))
#SMOTE-----------------------------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 1, stratify=y)

smt = SMOTE()
X_train, y_train = smt.fit_sample(X_train, y_train)
np.bincount(y_train)
lr = LogisticRegression()
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)

print(confusion_matrix(y_test, y_pred))

print(accuracy_score(y_test, y_pred))

print(recall_score(y_test, y_pred))
#NearMiss--------------------------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 1, stratify=y)

nr = NearMiss()
X_train, y_train = nr.fit_sample(X_train, y_train)
np.bincount(y_train)
lr = LogisticRegression()
lr.fit(X_train, y_train)

y_pred = lr.predict(X_test)

print(confusion_matrix(y_test, y_pred))

print(accuracy_score(y_test, y_pred))

print(recall_score(y_test, y_pred))
     
#----------------------------------------------------------------------------------------------------------------------
### stacking

##Read the data
data = pd.read_csv("stack.csv")
data.head()

#Identify Independent & Dependent data
##segregate X & y
X = data.iloc[:,:25].values
y = data.iloc[:,25].values
Train test split
# train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X,  y,  test_size = 0.20,  random_state = 42) 
      
#Stacking
# define the base models
level_0 = list()
level_0.append(('lr', LogisticRegression()))
level_0.append(('knn', KNeighborsClassifier()))
level_0.append(('cart', DecisionTreeClassifier()))
level_0.append(('bayes', GaussianNB()))

# define meta learner model
level_1 = LogisticRegression()

# define the stacking ensemble
model = StackingClassifier(estimators=level_0, final_estimator=level_1, cv=5)
      
#Evaluation
cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
scores = cross_val_score(model, X_train, y_train, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
print('>%s %.3f (%.3f)' % ('stacking', mean(scores), std(scores)))
      
#Graphical Evaluation
# plot model performance for comparison
pyplot.boxplot(scores, labels=['stacking'], showmeans=True)
pyplot.show()
      
#Prediction
# fit the model on all available data
model.fit(X_train, y_train)

# make a prediction for one example
yhat = model.predict(X_test)
      
#test performance
from sklearn.metrics import accuracy_score
score = accuracy_score(y_test, yhat)
print(score)
      
# get the dataset
def get_dataset():
    ##Read the data
    data = pd.read_csv("stack.csv")
    ##segregate X & y
    X = data.iloc[:,:25].values
    y = data.iloc[:,25].values
    return X, y
 
# get a stacking ensemble of models
def get_stacking():
    # define the base models
    level_0 = list()
    level_0.append(('lr', LogisticRegression()))
    level_0.append(('knn', KNeighborsClassifier()))
    level_0.append(('cart', DecisionTreeClassifier()))
    level_0.append(('bayes', GaussianNB()))
    # define meta learner model
    level_1 = LogisticRegression()
    # define the stacking ensemble
    model = StackingClassifier(estimators=level_0, final_estimator=level_1, cv=5)
    return model
 
# get a list of models to evaluate
def get_models():
    models = dict()
    models['stacking'] = get_stacking()
    return models
 
# evaluate a give model using cross-validation
def evaluate_model(model, X, y):
    cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)
    scores = cross_val_score(model, X, y, scoring='accuracy', cv=cv, n_jobs=-1, error_score='raise')
    return scores

# define dataset
X, y = get_dataset()
# get the models to evaluate
models = get_models()
# evaluate the models and store results
results, names = list(), list()
for name, model in models.items():
    scores = evaluate_model(model, X, y)
    results.append(scores)
    names.append(name)
    print('>%s %.3f (%.3f)' % (name, mean(scores), std(scores)))
# plot model performance for comparison
pyplot.boxplot(results, labels=names, showmeans=True)
pyplot.show()

      
      
      
#----------------------------------------------------------------------------------------------------------------------
### Voting


# Read the data
data = pd.read_csv("stack.csv")
data.head()
# Read the data
data = pd.read_csv("stack.csv")
data.head()
      
#Segregate Independent & Dependant data
# segregate X & y
X = data.iloc[:,:25].values
y = data.iloc[:,25].values
      
#Segregate Train test data
# train_test_split 
X_train, X_test, y_train, y_test = train_test_split(X,  y,  test_size = 0.20,  random_state = 42) 
      
#Classifiers
# group / ensemble of models 
models = []
models.append(('lr', LogisticRegression()))
models.append(('knn', KNeighborsClassifier()))
models.append(('cart', DecisionTreeClassifier()))
models.append(('bayes', GaussianNB()))
      
#Hard Voting
# Voting Classifier with hard voting 
vot_hard = VotingClassifier(estimators = model, voting ='hard') 
vot_hard.fit(X_train, y_train) 
y_pred = vot_hard.predict(X_test) 
      
#Performance on test
# using accuracy_score metric to predict accuracy 
score = accuracy_score(y_test, y_pred) 
print("Hard Voting Score ",  score) 
      
#Soft Voting
# Voting Classifier with soft voting 
vot_soft = VotingClassifier(estimators = model, voting ='soft') 
vot_soft.fit(X_train, y_train) 
y_pred = vot_soft.predict(X_test) 
      
#Performance on test
# using accuracy_score 
score = accuracy_score(y_test, y_pred) 
print("Soft Voting Score " , score) 
      
      
      
#----------------------------------------------------------------------------------------------------------------------
### votingclassifier

      
X = array[:,0:8]
Y = array[:,8]
seed = 7
kfold = model_selection.KFold(n_splits=10, random_state=seed)
# create the sub models
estimators = []
model1 = LogisticRegression()
estimators.append(('logistic', model1))
model2 = DecisionTreeClassifier()
estimators.append(('cart', model2))
model3 = SVC()
estimators.append(('svm', model3))
# create the ensemble model
ensemble = VotingClassifier(estimators)
results = model_selection.cross_val_score(ensemble, X, Y, cv=kfold)
print(results.mean())
      
estimators
      
ensemble
      
# create the sub models
estimators = []
model1 = LogisticRegression()
estimators.append(('logistic', model1))
model2 = DecisionTreeClassifier()
estimators.append(('cart', model2))
model3 = SVC(probability=True)
estimators.append(('svm', model3))
ensemble = VotingClassifier(estimators,voting='soft')
results = model_selection.cross_val_score(ensemble, X, Y, cv=kfold)
print(results.mean())



          
#----------------------------------------------------------------------------------------------------------------------
###   XGBOOST

#load Dataset
data = pd.read_csv('diabetes.csv')
data.head()
data_full = data.copy()
X_data = data_full.drop('Outcome', axis=1)
y = data_full.Outcome
X_data.head()
      
#Split the dataset into train and Test
seed = 7
test_size = 0.3
X_trian, X_test, y_train, y_test = train_test_split(X_data, y, test_size=test_size, random_state=seed)
      
#Train the XGboost Model for Classification
model1 = xgb.XGBClassifier()
model2 = xgb.XGBClassifier(n_estimators=100, max_depth=8, learning_rate=0.1, subsample=0.5)

train_model1 = model1.fit(X_trian, y_train)
train_model2 = model2.fit(X_trian, y_train)
      
#prediction and Classification Report


pred1 = train_model1.predict(X_test)
pred2 = train_model2.predict(X_test)

print('Model 1 XGboost Report %r' % (classification_report(y_test, pred1)))
print('Model 2 XGboost Report %r' % (classification_report(y_test, pred2)))
      
#Let's use accuracy score


print("Accuracy for model 1: %.2f" % (accuracy_score(y_test, pred1) * 100))
print("Accuracy for model 2: %.2f" % (accuracy_score(y_test, pred2) * 100))

          
#----------------------------------------------------------------------------------------------------------------------
### S2 - Faculty Notebook (Admissions data)

      #2. Data Preparation

#2.1 Read the Data
#Read the dataset and print the first five observations.
# load the csv file
# store the data in 'df_admissions'
df_admissions = pd.read_csv('Admission_predict.csv')

# display first five observations using head()
df_admissions.head()
#Let us now see the number of variables and observations in the data.

# use 'shape' to check the dimension of data
df_admissions.shape
#Interpretation: The data has 400 observations and 9 variables.


#2.2 Check the Data Type
#Check the data type of each variable. If the data type is not as per the data definition, change the data type.

# use 'dtypes' to check the data type of a variable
df_admissions.dtypes
#Interpretation: The variables GRE Score, TOEFL Score, University Rating, SOP, LOR and CGPA are numerical.

#From the above output, we see that the data type of Research is 'int64'.

#But according to the data definition, Research is a categorical variable, which is wrongly interpreted as 'int64', so we will convert these variables data type to 'object'.

#Change the data type as per the data definition.
# convert numerical variables to categorical (object) 
# use astype() to change the data type

# change the data type of 'Research'
df_admissions['Research'] = df_admissions['Research'].astype(object)
      
#Recheck the data type after the conversion.
# recheck the data types using 'dtypes'
df_admissions.dtypes
#Interpretation: Now, all the variables have the correct data type.


#2.3 Remove Insignificant Variables
#The column Serial No. contains the serial number of the student, which is redundant for further analysis. Thus, we drop the column.

# drop the column 'Serial No.' using drop()
# 'axis = 1' drops the specified column
      
df_admissions = df_admissions.drop('Serial No.', axis = 1)

#2.4 Distribution of Variables
#Distribution of numeric independent variables.

# for the independent numeric variables, we plot the histogram to check the distribution of the variables
# Note: the hist() function considers the numeric variables only, by default
# we drop the target variable using drop()
# 'axis=1' drops the specified column
df_admissions.drop('Chance of Admit', axis = 1).hist()

# adjust the subplots
plt.tight_layout()

# display the plot
plt.show()  

# print the skewness for each numeric independent variable
print('Skewness:')
# we drop the target variable using drop()
# 'axis=1' drops the specified column
# skew() returns the coefficient of skewness for each variable
      
df_admissions.drop('Chance of Admit', axis = 1).skew()
      
#Interpretation: The above plot indicates that all the variables are near normally distributed.

#Distribution of categoric independent variable.

# for the independent categoric variable, we plot the count plot to check the distribution of the variable 'Research'
# use countplot() to plot the count of each label in the categorical variable 
      
sns.countplot(df_admissions.Research)

# add plot and axes labels
# set text size using 'fontsize'
      
plt.title('Count Plot for Categorical Variable (Research)', fontsize = 15)
plt.xlabel('Research', fontsize = 15)
plt.ylabel('Count', fontsize = 15)

# display the plot
plt.show()
      
# Distribution of dependent variable.
# consider only the target variable
df_target = df_admissions['Chance of Admit'].copy()

# get counts of 0's and 1's in the 'Chance of Admit' variable
df_target.value_counts()

# plot the countplot of the variable 'Chance of Admit'
sns.countplot(x = df_target)

# use below code to print the values in the graph
# 'x' and 'y' gives position of the text
# 's' is the text 
plt.text(x = -0.05, y = df_target.value_counts()[0] + 1, s = str(round((df_target.value_counts()[0])*100/len(df_target),2)) + '%')
plt.text(x = 0.95, y = df_target.value_counts()[1] +1, s = str(round((df_target.value_counts()[1])*100/len(df_target),2)) + '%')

# add plot and axes labels
# set text size using 'fontsize'
plt.title('Count Plot for Target Variable (Chance of Admit)', fontsize = 15)
plt.xlabel('Target Variable', fontsize = 15)
plt.ylabel('Count', fontsize = 15)

# to show the plot
plt.show()
      
#Interpretation: The above plot shows that there is no imbalance in the target variable.


#2.5 Missing Value Treatment
#First run a check for the presence of missing values and their percentage for each column. Then choose the right approach to treat them.

# sort the variables on the basis of total null values in the variable
# 'isnull().sum()' returns the number of missing values in each variable
# 'ascending = False' sorts values in the descending order
# the variable with highest number of missing values will appear first
Total = df_admissions.isnull().sum().sort_values(ascending=False)          

# calculate percentage of missing values
# 'ascending = False' sorts values in the descending order
# the variable with highest percentage of missing values will appear first
Percent = (df_admissions.isnull().sum()*100/df_admissions.isnull().count()).sort_values(ascending=False)   

# concat the 'Total' and 'Percent' columns using 'concat' function
# pass a list of column names in parameter 'keys' 
# 'axis = 1' concats along the columns
      
missing_data = pd.concat([Total, Percent], axis = 1, keys = ['Total', 'Percentage of Missing Values'])    
missing_data
      
      
#Interpretation: The above output shows that there are no missing values in the data.


#2.6 Dummy Encode the Categorical Variables
#Split the dependent and independent variables.
# store the target variable 'Chance of Admit' in a dataframe 'df_target'
      
df_target = df_admissions['Chance of Admit']

# store all the independent variables in a dataframe 'df_feature' 
# drop the column 'Chance of Admit' using drop()
# 'axis = 1' drops the specified column
df_feature = df_admissions.drop('Chance of Admit', axis = 1)
      
#Filter numerical and categorical variables.
# filter the numerical features in the dataset
# 'select_dtypes' is used to select the variables with given data type
# 'include = [np.number]' will include all the numerical variables
df_num = df_feature.select_dtypes(include = [np.number])

# display numerical features
df_num.columns
# filter the categorical features in the dataset
# 'select_dtypes' is used to select the variables with given data type
# 'include = [np.object]' will include all the categorical variables
#df_cat = df_feature.select_dtypes(include = [np.object])

# display categorical features
df_cat.columns
      
#The classification method fails in presence of categorical variables. To overcome this we use (n-1) dummy encoding.

#Encode the each categorical variable and create (n-1) dummy variables for n categories of the variable.

# use 'get_dummies' from pandas to create dummy variables
# use 'drop_first' to create (n-1) dummy variables

dummy_var = pd.get_dummies(data = df_cat, drop_first = True)

#2.7 Scale the Data
#We scale the variables to get all the variables in the same range. With this, we can avoid a problem in which some features come to dominate solely because they tend to have larger values than others.

# initialize the standard scalar
X_scaler = StandardScaler()
      
# scale all the numerical columns
# standardize all the columns of the dataframe 'df_num'
num_scaled = X_scaler.fit_transform(df_num)

# create a dataframe of scaled numerical variables
# pass the required column names to the parameter 'columns'
df_num_scaled = pd.DataFrame(num_scaled, columns = df_num.columns)
Concatenate numerical and dummy encoded categorical variables.

# concat the dummy variables with numeric features to create a dataframe of all independent variables
# 'axis=1' concats the dataframes along columns 
X = pd.concat([df_num_scaled, dummy_var], axis = 1)

# display first five observations
X.head()

#2.8 Train-Test Split
#Before applying various classification techniques to predict the admission status of the student, let us split the dataset in train and test set.

# split data into train subset and test subset
# set 'random_state' to generate the same dataset each time you run the code 
# 'test_size' returns the proportion of data to be included in the testing set
X_train, X_test, y_train, y_test = train_test_split(X, df_target, random_state = 10, test_size = 0.2)

# check the dimensions of the train & test subset using 'shape'
# print dimension of train set
print('X_train', X_train.shape)
print('y_train', y_train.shape)

# print dimension of test set
print('X_test', X_test.shape)
print('y_test', y_test.shape)
      

# create a generalized function to calculate the performance metrics values for test set
def get_test_report(model):
    
    # for test set:
    # test_pred: prediction made by the model on the test dataset 'X_test'
    # y_test: actual values of the target variable for the test dataset

    # predict the output of the target variable from the test data 
    test_pred = model.predict(X_test)

    # return the classification report for test data
    return(classification_report(y_test, test_pred))
      
#Define a function to plot the confusion matrix.
# define a to plot a confusion matrix for the model
def plot_confusion_matrix(model):
    
    # predict the target values using X_test
    y_pred = model.predict(X_test)
    
    # create a confusion matrix
    # pass the actual and predicted target values to the confusion_matrix()
    cm = confusion_matrix(y_test, y_pred)

    # label the confusion matrix  
    # pass the matrix as 'data'
    # pass the required column names to the parameter, 'columns'
    # pass the required row names to the parameter, 'index'
    conf_matrix = pd.DataFrame(data = cm,columns = ['Predicted:0','Predicted:1'], index = ['Actual:0','Actual:1'])

    # plot a heatmap to visualize the confusion matrix
    # 'annot' prints the value of each grid 
    # 'fmt = d' returns the integer value in each grid
    # 'cmap' assigns color to each grid
    # as we do not require different colors for each grid in the heatmap,
    # use 'ListedColormap' to assign the specified color to the grid
    # 'cbar = False' will not return the color bar to the right side of the heatmap
    # 'linewidths' assigns the width to the line that divides each grid
    # 'annot_kws = {'size':25})' assigns the font size of the annotated text 
    sns.heatmap(conf_matrix, annot = True, fmt = 'd', cmap = ListedColormap(['lightskyblue']), cbar = False, 
                linewidths = 0.1, annot_kws = {'size':25})

    # set the font size of x-axis ticks using 'fontsize'
    plt.xticks(fontsize = 20)

    # set the font size of y-axis ticks using 'fontsize'
    plt.yticks(fontsize = 20)

    # display the plot
    plt.show()
      

# define a function to plot the ROC curve and print the ROC-AUC score
def plot_roc(model):
    
    # predict the probability of target variable using X_test
    # consider the probability of positive class by subsetting with '[:,1]'
    y_pred_prob = model.predict_proba(X_test)[:,1]
    
    # the roc_curve() returns the values for false positive rate, true positive rate and threshold
    # pass the actual target values and predicted probabilities to the function
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

    # plot the ROC curve
    plt.plot(fpr, tpr)

    # set limits for x and y axes
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])

    # plot the straight line showing worst prediction for the model
    plt.plot([0, 1], [0, 1],'r--')

    # add plot and axes labels
    # set text size using 'fontsize'
    plt.title('ROC curve for Admission Prediction Classifier', fontsize = 15)
    plt.xlabel('False positive rate (1-Specificity)', fontsize = 15)
    plt.ylabel('True positive rate (Sensitivity)', fontsize = 15)

    # add the AUC score to the plot
    # 'x' and 'y' gives position of the text
    # 's' is the text 
    # use round() to round-off the AUC score upto 4 digits
    plt.text(x = 0.02, y = 0.9, s = ('AUC Score:',round(roc_auc_score(y_test, y_pred_prob),4)))

    # plot the grid
    plt.grid(True)

# 3. K Nearest Neighbors (KNN)
# KNN is a classification machine learning algorithm used to identify the class of the observation. This algorithm search for K nearest points to determine the class of an observation. To identify the nearest points, it considers the distance metrics like Euclidean, Manhattan, Chebyshev, Hamming, and so on.

# Build a knn model on a training dataset using euclidean distance.
# instantiate the 'KNeighborsClassifier'
# n_neighnors: number of neighbors to consider
# default metric is minkowski, and with p=2 it is equivalent to the euclidean metric
knn_classification = KNeighborsClassifier(n_neighbors = 3)

# fit the model using fit() on train data
knn_model = knn_classification.fit(X_train, y_train)
      
#Build a confusion matrix.
# call the function to plot the confusion matrix
# pass the knn model to the function
plot_confusion_matrix(knn_model)
      
#Calculate performance measures on the test set.

# compute the performance measures on test data
# call the function 'get_test_report'
# pass the knn model to the function
test_report = get_test_report(knn_model)

# print the performace measures
print(test_report)
      
#Interpretation: The accuracy is 84% for this model.

#Plot the ROC curve.

# call the function to plot the ROC curve
# pass the knn model to the function
plot_roc(knn_model)
      
#Interpretation: The red dotted line represents the ROC curve of a purely random classifier; a good classifier stays as far away from that line as possible (toward the top-left corner).
#From the above plot, we can see that our classifier (knn_model with n_neighbors = 3) is away from the dotted line; with the AUC score 0.8747.


#3.1 Optimal Value of K (using GridSearchCV)
# create a dictionary with hyperparameters and its values
# n_neighnors: number of neighbors to consider
# usually, we consider the odd value of 'n_neighnors' to avoid the equal number of nearest points with more than one class
# pass the different distance metrics to the parameter, 'metric'
tuned_paramaters = {'n_neighbors': np.arange(1, 25, 2),
                   'metric': ['hamming','euclidean','manhattan','Chebyshev']}
 
# instantiate the 'KNeighborsClassifier' 
knn_classification = KNeighborsClassifier()

# use GridSearchCV() to find the optimal value of the hyperparameters
# estimator: pass the knn model
# param_grid: pass the list 'tuned_parameters'
# cv: number of folds in k-fold i.e. here cv = 5
# scoring: pass the scoring parameter 'accuracy'
knn_grid = GridSearchCV(estimator = knn_classification, 
                        param_grid = tuned_paramaters, 
                        cv = 5, 
                        scoring = 'accuracy')

# fit the model on X_train and y_train using fit()
knn_grid.fit(X_train, y_train)

# get the best parameters
print('Best parameters for KNN Classifier: ', knn_grid.best_params_, '\n')
      
#Draw a line plot to see the error rate for each value of K using euclidean distance as a metric of KNN model
# consider an empty list to store error rate
error_rate = []

# use for loop to build a knn model for each K
for i in np.arange(1,25,2):
    
    # setup a knn classifier with k neighbors
    # use the 'euclidean' metric 
    knn = KNeighborsClassifier(i, metric = 'euclidean')
   
    # fit the model using 'cross_val_score'
    # pass the knn model as 'estimator'
    # use 5-fold cross validation
    score = cross_val_score(knn, X_train, y_train, cv = 5)
    
    # calculate the mean score
    score = score.mean()
    
    # compute error rate 
    error_rate.append(1 - score)

# plot the error_rate for different values of K 
plt.plot(range(1,25,2), error_rate)

# add plot and axes labels
# set text size using 'fontsize'
plt.title('Error Rate', fontsize = 15)
plt.xlabel('K', fontsize = 15)
plt.ylabel('Error Rate', fontsize = 15)

# set the x-axis labels
plt.xticks(np.arange(1, 25, step = 2))

# plot a vertical line across the minimum error rate
plt.axvline(x = 17, color = 'red')

# display the plot
plt.show()
      
#Interpretation: We can see that the optimal value of K (= 17) obtained from the GridSearchCV() results in a lowest error rate.

#Calculate performance measures on the test set.

# print the performance measures for test set for the model with best parameters
# call the function 'get_test_report'
# pass the knn model using GridSearch to the function
print('Classification Report for test set: \n', get_test_report(knn_grid))

#Plot the ROC curve.

# call the function to plot the ROC curve
# pass the knn model to the function
plot_roc(knn_grid)

#Interpretation: From the above plot, we can see that our classifier (knn_model with n_neighbors = 17) is away from the red dotted line; with the AUC score 0.9464.


#4. Naive Bayes Algorithm
#It uses a Bayes' Theorem with the assumption of independence of predictor variables. The sklearn library provides different naive bayes classifiers, as GaussianNB, MultinomialNB and so on.

#Build a naive bayes model on a training dataset.
# instantiate the 'GaussianNB'
gnb = GaussianNB()

# fit the model using fit() on train data
gnb_model = gnb.fit(X_train, y_train)
      
#Build a confusion matrix.
# call the function to plot the confusion matrix
# pass the gaussian naive bayes model to the function
plot_confusion_matrix(gnb_model)
      
#Calculate performance measures on the test set.

# compute the performance measures on test data
# call the function 'get_test_report'
# pass the gaussian naive bayes model to the function
test_report = get_test_report(gnb_model)

# print the performace measures
print(test_report)
      
#Plot the ROC curve.

# call the function to plot the ROC curve
# pass the gaussian naive bayes model to the function
plot_roc(gnb_model)
      
#Interpretation: From the above plot, we can see that our classifier (gnb_model) is away from the red dotted line; with the AUC score 0.9511.

#Note: Algorithms like Naive Bayes and tree based algorithms do not need feature scaling or normalization. Performing a features scaling in these algorithms may not have much effect.


#5. Comparison between KNN Model and Naive Bayes Model
# K Nearest Neighbors
y_pred_prob_knn = knn_grid.predict_proba(X_test)[:,1]
    
# the roc_curve() returns the values for false positive rate, true positive rate and threshold
# pass the actual target values and predicted probabilities to the function
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob_knn)

# add the AUC score to the plot
auc_score_knn = roc_auc_score(y_test, y_pred_prob_knn)

# plot the ROC curve
plt.plot(fpr, tpr, label='KNN Model (AUC Score = %0.4f)' % auc_score_knn)

# Gaussian Naive Bayes
y_pred_prob_gnb = gnb_model.predict_proba(X_test)[:,1]
    
# the roc_curve() returns the values for false positive rate, true positive rate and threshold
# pass the actual target values and predicted probabilities to the function
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob_gnb)

# add the AUC score to the plot
auc_score_gnb = roc_auc_score(y_test, y_pred_prob_gnb)

# plot the ROC curve
plt.plot(fpr, tpr, label='GNB Model (AUC Score = %0.4f)' % auc_score_gnb)

# set limits for x and y axes
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.0])

# plot the straight line showing worst prediction for the model
plt.plot([0, 1], [0, 1],'r--')

# add plot and axes labels
# set text size using 'fontsize'
plt.title('GNB Model Vs. KNN Model', fontsize = 15)
plt.xlabel('False positive rate (1-Specificity)', fontsize = 15)
plt.ylabel('True positive rate (Sensitivity)', fontsize = 15)

# set the position of legend
plt.legend(loc = 'lower right')

# plot the grid
plt.grid(True)
#Interpretation: The Auc Score of Gaussian Naive Bayes model is slightly higher than that of KNN Model.



          
#----------------------------------------------------------------------------------------------------------------------
### S2 - Faculty Notebook (Brest Cancer Data)

      #2.1 Read the Data
#Read the dataset and print the first five observations.
# load the csv file
# store the data in 'df_cancer'
df_cancer = pd.read_csv('bcancer.csv')

# display first five observations using head()
df_cancer.head()
#Let us now see the number of variables and observations in the data.

# use 'shape' to check the dimension of data
df_cancer.shape
#Interpretation: The data has 569 observations and 31 variables.


2.2 Check the Data Type
#Check the data type of each variable. If the data type is not as per the data definition, change the data type.

# use 'dtypes' to check the data type of a variable
df_cancer.dtypes
#Interpretation: All the indeppendent variables are numeric.


#2.3 Distribution of Variables
#Distribution of numeric independent variables.

# for the independent numeric variables, we plot the histogram to check the distribution of the variables
# Note: the hist() function considers the numeric variables only, by default
# we drop the target variable using drop()
# 'axis=1' drops the specified column
df_cancer.drop('diagnosis', axis = 1).hist()

# adjust the subplots
plt.tight_layout()

# display the plot
plt.show()
#Distribution of dependent variable.
# consider only the target variable
df_target = df_cancer['diagnosis'].copy()

# get counts of 0's and 1's in the 'diagnosis' variable
df_target.value_counts()

# plot the countplot of the variable 'diagnosis'
sns.countplot(x = df_target)

# use below code to print the values in the graph
# 'x' and 'y' gives position of the text
# 's' is the text 
plt.text(x = -0.05, y = df_target.value_counts()[1] + 1, s = str(round((df_target.value_counts()[1])*100/len(df_target),2)) + '%')
plt.text(x = 0.95, y = df_target.value_counts()[0] +1, s = str(round((df_target.value_counts()[0])*100/len(df_target),2)) + '%')

# add plot and axes labels
# set text size using 'fontsize'
plt.title('Count Plot for Target Variable (Diagnosis)', fontsize = 15)
plt.xlabel('Target Variable', fontsize = 15)
plt.ylabel('Count', fontsize = 15)

# to show the plot
plt.show()
#Interpretation: The above plot shows that there is not that much imbalance in the target variable.


#2.4 Missing Value Treatment
#First run a check for the presence of missing values and their percentage for each column. Then choose the right approach to treat them.

# sort the variables on the basis of total null values in the variable
# 'isnull().sum()' returns the number of missing values in each variable
# 'ascending = False' sorts values in the descending order
# the variable with highest number of missing values will appear first
Total = df_cancer.isnull().sum().sort_values(ascending=False)          

# calculate percentage of missing values
# 'ascending = False' sorts values in the descending order
# the variable with highest percentage of missing values will appear first
Percent = (df_cancer.isnull().sum()*100/df_cancer.isnull().count()).sort_values(ascending=False)   

# concat the 'Total' and 'Percent' columns using 'concat' function
# pass a list of column names in parameter 'keys' 
# 'axis = 1' concats along the columns
missing_data = pd.concat([Total, Percent], axis = 1, keys = ['Total', 'Percentage of Missing Values'])    
missing_data
#Interpretation: The above output shows that there are no missing values in the data.

#Split the dependent and independent variables.
# store the target variable 'diagnosis' in a dataframe 'df_target'
df_target = df_cancer['diagnosis']

# store all the independent variables in a dataframe 'df_feature' 
# drop the column 'diagnosis' using drop()
# 'axis = 1' drops the specified column
df_feature = df_cancer.drop('diagnosis', axis = 1)
# if the value in the target variable is 'M' then replace it with 0 else with 1
# i.e. set 0 for malignant (negative class)
for i in range(len(df_target)):
    if df_target[i] == 'M':
        df_target[i] = 0
    else:
        df_target[i] = 1
        
# change the datatype of the target variable to integer
df_target = df_target.astype('int')

# filter the numerical features in the dataset
# 'select_dtypes' is used to select the variables with given data type
# 'include = [np.number]' will include all the numerical variables
df_feature = df_feature.select_dtypes(include = [np.number])

# display numerical features
df_feature.columns

#2.5 Scale the Data
#We scale the variables to get all the variables in the same range. With this, we can avoid a problem in which some features come to dominate solely because they tend to have larger values than others.

# initialize the standard scalar
X_scaler = StandardScaler()

# scale all the numerical columns
# standardize all the columns of the dataframe 'df_feature'
num_scaled = X_scaler.fit_transform(df_feature)

# create a dataframe of scaled numerical variables
# pass the required column names to the parameter 'columns'
X = pd.DataFrame(num_scaled, columns = df_feature.columns)

X.head()

#2.6 Train-Test Split
# split data into train subset and test subset
# set 'random_state' to generate the same dataset each time you run the code 
# 'test_size' returns the proportion of data to be included in the testing set
X_train, X_test, y_train, y_test = train_test_split(X, df_target, random_state = 10, test_size = 0.2)

# check the dimensions of the train & test subset using 'shape'
# print dimension of train set
print('X_train', X_train.shape)
print('y_train', y_train.shape)

# print dimension of test set
print('X_test', X_test.shape)
print('y_test', y_test.shape)

# create a generalized function to calculate the performance metrics values for test set
def get_test_report(model):
    
    # for test set:
    # test_pred: prediction made by the model on the test dataset 'X_test'
    # y_test: actual values of the target variable for the test dataset

    # predict the output of the target variable from the test data 
    test_pred = model.predict(X_test)

    # return the classification report for test data
    return(classification_report(y_test, test_pred))

# define a to plot a confusion matrix for the model
def plot_confusion_matrix(model):
    
    # predict the target values using X_test
    y_pred = model.predict(X_test)
    
    # create a confusion matrix
    # pass the actual and predicted target values to the confusion_matrix()
    cm = confusion_matrix(y_test, y_pred)

    # label the confusion matrix  
    # pass the matrix as 'data'
    # pass the required column names to the parameter, 'columns'
    # pass the required row names to the parameter, 'index'
    conf_matrix = pd.DataFrame(data = cm,columns = ['Predicted:0','Predicted:1'], index = ['Actual:0','Actual:1'])

    # plot a heatmap to visualize the confusion matrix
    # 'annot' prints the value of each grid 
    # 'fmt = d' returns the integer value in each grid
    # 'cmap' assigns color to each grid
    # as we do not require different colors for each grid in the heatmap,
    # use 'ListedColormap' to assign the specified color to the grid
    # 'cbar = False' will not return the color bar to the right side of the heatmap
    # 'linewidths' assigns the width to the line that divides each grid
    # 'annot_kws = {'size':25})' assigns the font size of the annotated text 
    sns.heatmap(conf_matrix, annot = True, fmt = 'd', cmap = ListedColormap(['lightskyblue']), cbar = False, 
                linewidths = 0.1, annot_kws = {'size':25})

    # set the font size of x-axis ticks using 'fontsize'
    plt.xticks(fontsize = 20)

    # set the font size of y-axis ticks using 'fontsize'
    plt.yticks(fontsize = 20)

    # display the plot
    plt.show()
      

# define a function to plot the ROC curve and print the ROC-AUC score
def plot_roc(model):
    
    # predict the probability of target variable using X_test
    # consider the probability of positive class by subsetting with '[:,1]'
    y_pred_prob = model.predict_proba(X_test)[:,1]
    
    # the roc_curve() returns the values for false positive rate, true positive rate and threshold
    # pass the actual target values and predicted probabilities to the function
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

    # plot the ROC curve
    plt.plot(fpr, tpr)

    # set limits for x and y axes
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])

    # plot the straight line showing worst prediction for the model
    plt.plot([0, 1], [0, 1],'r--')

    # add plot and axes labels
    # set text size using 'fontsize'
    plt.title('ROC curve for Cancer Prediction Classifier', fontsize = 15)
    plt.xlabel('False positive rate (1-Specificity)', fontsize = 15)
    plt.ylabel('True positive rate (Sensitivity)', fontsize = 15)

    # add the AUC score to the plot
    # 'x' and 'y' gives position of the text
    # 's' is the text 
    # use round() to round-off the AUC score upto 4 digits
    plt.text(x = 0.02, y = 0.9, s = ('AUC Score:',round(roc_auc_score(y_test, y_pred_prob),4)))

    # plot the grid
    plt.grid(True)

# 3. Naive Bayes Algorithm
# It uses a Bayes' Theorem with the assumption of independence of predictor variables. The sklearn library provides different naive bayes classifiers, as GaussianNB, MultinomialNB and so on.

# Build a naive bayes model on a training dataset.
# instantiate the 'GaussianNB'
gnb = GaussianNB()

# fit the model using fit() on train data
gnb_model = gnb.fit(X_train, y_train)
      
#Build a confusion matrix.
# call the function to plot the confusion matrix
# pass the gaussian naive bayes model to the function
plot_confusion_matrix(gnb_model)
#Calculate performance measures on the test set.

# compute the performance measures on test data
# call the function 'get_test_report'
# pass the gaussian naive bayes model to the function
test_report = get_test_report(gnb_model)

# print the performace measures
print(test_report)
Plot the ROC curve.

# call the function to plot the ROC curve
# pass the gaussian naive bayes model to the function
plot_roc(gnb_model)
      
#Interpretation: From the above plot, we can see that our classifier (gnb_model) is away from the red dotted line; with the AUC score 0.9836.

#Note: Algorithms like Naive Bayes and tree based algorithms do not need feature scaling or normalization. Performing a features scaling in these algorithms may not have much effect.

          
#----------------------------------------------------------------------------------------------------------------------
### S3 - Faculty Notebook (Brest Cancer Data)

      
#2.1 Read the Data
#Read the dataset and print the first five observations.
# load the csv file
# store the data in 'df_cancer'
df_cancer = pd.read_csv('bcancer.csv')

# display first five observations using head()
df_cancer.head()
#Let us now see the number of variables and observations in the data.

# use 'shape' to check the dimension of data
df_cancer.shape
#Interpretation: The data has 569 observations and 31 variables.


2.2 Check the Data Type
#Check the data type of each variable. If the data type is not as per the data definition, change the data type.

# use 'dtypes' to check the data type of a variable
df_cancer.dtypes
#Interpretation: All the indeppendent variables are numeric.


#2.3 Distribution of Variables
#Distribution of numeric independent variables.

# for the independent numeric variables, we plot the histogram to check the distribution of the variables
# Note: the hist() function considers the numeric variables only, by default
# we drop the target variable using drop()
# 'axis=1' drops the specified column
df_cancer.drop('diagnosis', axis = 1).hist()

# adjust the subplots
plt.tight_layout()

# display the plot
plt.show()

#Distribution of dependent variable.
# consider only the target variable
df_target = df_cancer['diagnosis'].copy()

# get counts of 0's and 1's in the 'diagnosis' variable
df_target.value_counts()

# plot the countplot of the variable 'diagnosis'
sns.countplot(x = df_target)

# use below code to print the values in the graph
# 'x' and 'y' gives position of the text
# 's' is the text 
plt.text(x = -0.05, y = df_target.value_counts()[1] + 1, s = str(round((df_target.value_counts()[1])*100/len(df_target),2)) + '%')
plt.text(x = 0.95, y = df_target.value_counts()[0] +1, s = str(round((df_target.value_counts()[0])*100/len(df_target),2)) + '%')

# add plot and axes labels
# set text size using 'fontsize'
plt.title('Count Plot for Target Variable (Diagnosis)', fontsize = 15)
plt.xlabel('Target Variable', fontsize = 15)
plt.ylabel('Count', fontsize = 15)

# to show the plot
plt.show()
#Interpretation: The above plot shows that there is not that much imbalance in the target variable.


#2.4 Missing Value Treatment
#First run a check for the presence of missing values and their percentage for each column. Then choose the right approach to treat them.

# sort the variables on the basis of total null values in the variable
# 'isnull().sum()' returns the number of missing values in each variable
# 'ascending = False' sorts values in the descending order
# the variable with highest number of missing values will appear first
Total = df_cancer.isnull().sum().sort_values(ascending=False)          

# calculate percentage of missing values
# 'ascending = False' sorts values in the descending order
# the variable with highest percentage of missing values will appear first
Percent = (df_cancer.isnull().sum()*100/df_cancer.isnull().count()).sort_values(ascending=False)   
​
# concat the 'Total' and 'Percent' columns using 'concat' function
# pass a list of column names in parameter 'keys' 
# 'axis = 1' concats along the columns
missing_data = pd.concat([Total, Percent], axis = 1, keys = ['Total', 'Percentage of Missing Values'])    
missing_data

#Interpretation: The above output shows that there are no missing values in the data.

#Split the dependent and independent variables.
# store the target variable 'diagnosis' in a dataframe 'df_target'
df_target = df_cancer['diagnosis']

# store all the independent variables in a dataframe 'df_feature' 
# drop the column 'diagnosis' using drop()
# 'axis = 1' drops the specified column
df_feature = df_cancer.drop('diagnosis', axis = 1)
# if the value in the target variable is 'M' then replace it with 0 else with 1
# i.e. set 0 for malignant (negative class)
for i in range(len(df_target)):
    if df_target[i] == 'M':
        df_target[i] = 0
    else:
        df_target[i] = 1
        
# change the datatype of the target variable to integer
df_target = df_target.astype('int')

# filter the numerical features in the dataset
# 'select_dtypes' is used to select the variables with given data type
# 'include = [np.number]' will include all the numerical variables
df_feature = df_feature.select_dtypes(include = [np.number])

# display numerical features
df_feature.columns

#2.5 Scale the Data
#We scale the variables to get all the variables in the same range. With this, we can avoid a problem in which some features come to dominate solely because they tend to have larger values than others.

# initialize the standard scalar
X_scaler = StandardScaler()

# scale all the numerical columns
# standardize all the columns of the dataframe 'df_feature'
num_scaled = X_scaler.fit_transform(df_feature)

# create a dataframe of scaled numerical variables
# pass the required column names to the parameter 'columns'
X = pd.DataFrame(num_scaled, columns = df_feature.columns)

X.head()

#2.6 Train-Test Split
# split data into train subset and test subset
# set 'random_state' to generate the same dataset each time you run the code 
# 'test_size' returns the proportion of data to be included in the testing set
X_train, X_test, y_train, y_test = train_test_split(X, df_target, random_state = 10, test_size = 0.2)

# check the dimensions of the train & test subset using 'shape'
# print dimension of train set
print('X_train', X_train.shape)
print('y_train', y_train.shape)

# print dimension of test set
print('X_test', X_test.shape)
print('y_test', y_test.shape)


# create a generalized function to calculate the performance metrics values for test set
def get_test_report(model):
    
    # for test set:
    # test_pred: prediction made by the model on the test dataset 'X_test'
    # y_test: actual values of the target variable for the test dataset

    # predict the output of the target variable from the test data 
    test_pred = model.predict(X_test)

    # return the classification report for test data
    return(classification_report(y_test, test_pred))


# define a to plot a confusion matrix for the model
def plot_confusion_matrix(model):
    
    # predict the target values using X_test
    y_pred = model.predict(X_test)
    
    # create a confusion matrix
    # pass the actual and predicted target values to the confusion_matrix()
    cm = confusion_matrix(y_test, y_pred)
​
    # label the confusion matrix  
    # pass the matrix as 'data'
    # pass the required column names to the parameter, 'columns'
    # pass the required row names to the parameter, 'index'
    conf_matrix = pd.DataFrame(data = cm,columns = ['Predicted:0','Predicted:1'], index = ['Actual:0','Actual:1'])
​
    # plot a heatmap to visualize the confusion matrix
    # 'annot' prints the value of each grid 
    # 'fmt = d' returns the integer value in each grid
    # 'cmap' assigns color to each grid
    # as we do not require different colors for each grid in the heatmap,
    # use 'ListedColormap' to assign the specified color to the grid
    # 'cbar = False' will not return the color bar to the right side of the heatmap
    # 'linewidths' assigns the width to the line that divides each grid
    # 'annot_kws = {'size':25})' assigns the font size of the annotated text 
    sns.heatmap(conf_matrix, annot = True, fmt = 'd', cmap = ListedColormap(['lightskyblue']), cbar = False, 
                linewidths = 0.1, annot_kws = {'size':25})

    # set the font size of x-axis ticks using 'fontsize'
    plt.xticks(fontsize = 20)

    # set the font size of y-axis ticks using 'fontsize'
    plt.yticks(fontsize = 20)

    # display the plot
    plt.show()


# define a function to plot the ROC curve and print the ROC-AUC score
def plot_roc(model):
    
    # predict the probability of target variable using X_test
    # consider the probability of positive class by subsetting with '[:,1]'
    y_pred_prob = model.predict_proba(X_test)[:,1]
    
    # the roc_curve() returns the values for false positive rate, true positive rate and threshold
    # pass the actual target values and predicted probabilities to the function
    fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob)

    # plot the ROC curve
    plt.plot(fpr, tpr)

    # set limits for x and y axes
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.0])

    # plot the straight line showing worst prediction for the model
    plt.plot([0, 1], [0, 1],'r--')

    # add plot and axes labels
    # set text size using 'fontsize'
    plt.title('ROC curve for Cancer Prediction Classifier', fontsize = 15)
    plt.xlabel('False positive rate (1-Specificity)', fontsize = 15)
    plt.ylabel('True positive rate (Sensitivity)', fontsize = 15)
​
    # add the AUC score to the plot
    # 'x' and 'y' gives position of the text
    # 's' is the text 
    # use round() to round-off the AUC score upto 4 digits
    plt.text(x = 0.02, y = 0.9, s = ('AUC Score:',round(roc_auc_score(y_test, y_pred_prob),4)))
​
    # plot the grid
    plt.grid(True)

#3. K Nearest Neighbors (KNN)
#KNN is a classification machine learning algorithm used to identify the class of the observation. This algorithm search for K nearest points to determine the class of an observation. To identify the nearest points, it considers the distance metrics like Euclidean, Manhattan, Chebyshev, Hamming, and so on.

#Build a knn model on a training dataset using euclidean distance.
# instantiate the 'KNeighborsClassifier'
# n_neighnors: number of neighbors to consider
# default metric is minkowski, and with p=2 it is equivalent to the euclidean metric
knn_classification = KNeighborsClassifier(n_neighbors = 3)

# fit the model using fit() on train data
knn_model = knn_classification.fit(X_train, y_train)

#Build a confusion matrix.
# call the function to plot the confusion matrix
# pass the knn model to the function
plot_confusion_matrix(knn_model)

#Calculate performance measures on the test set.

# compute the performance measures on test data
# call the function 'get_test_report'
# pass the knn model to the function
test_report = get_test_report(knn_model)

# print the performace measures
print(test_report)

#Interpretation: The accuracy is 98% for this model.

#Plot the ROC curve.

# call the function to plot the ROC curve
# pass the knn model to the function
plot_roc(knn_model)

#Interpretation: The red dotted line represents the ROC curve of a purely random classifier; a good classifier stays as far away from that line as possible (toward the top-left corner).
#From the above plot, we can see that our classifier (knn_model with n_neighbors = 3) is away from the dotted line; with the AUC score 0.9976.


#3.1 Optimal Value of K (using GridSearchCV)
# create a dictionary with hyperparameters and its values
# n_neighnors: number of neighbors to consider
# usually, we consider the odd value of 'n_neighnors' to avoid the equal number of nearest points with more than one class
# pass the different distance metrics to the parameter, 'metric'
tuned_paramaters = {'n_neighbors': np.arange(1, 25, 2),
                   'metric': ['hamming','euclidean','manhattan','Chebyshev']}
 
# instantiate the 'KNeighborsClassifier' 
knn_classification = KNeighborsClassifier()

# use GridSearchCV() to find the optimal value of the hyperparameters
# estimator: pass the knn model
# param_grid: pass the list 'tuned_parameters'
# cv: number of folds in k-fold i.e. here cv = 5
# scoring: pass the scoring parameter 'accuracy'
knn_grid = GridSearchCV(estimator = knn_classification, 
                        param_grid = tuned_paramaters, 
                        cv = 5, 
                        scoring = 'accuracy')

# fit the model on X_train and y_train using fit()
knn_grid.fit(X_train, y_train)

# get the best parameters
print('Best parameters for KNN Classifier: ', knn_grid.best_params_, '\n')

#Draw a line plot to see the error rate for each value of K using euclidean distance as a metric of KNN model
# consider an empty list to store error rate
error_rate = []
​
# use for loop to build a knn model for each K
for i in np.arange(1,25,2):
    
    # setup a knn classifier with k neighbors
    # use the 'euclidean' metric 
    knn = KNeighborsClassifier(i, metric = 'euclidean')
   
    # fit the model using 'cross_val_score'
    # pass the knn model as 'estimator'
    # use 5-fold cross validation
    score = cross_val_score(knn, X_train, y_train, cv = 5)
    
    # calculate the mean score
    score = score.mean()
    
    # compute error rate 
    error_rate.append(1 - score)

# plot the error_rate for different values of K 
plt.plot(range(1,25,2), error_rate)

# add plot and axes labels
# set text size using 'fontsize'
plt.title('Error Rate', fontsize = 15)
plt.xlabel('K', fontsize = 15)
plt.ylabel('Error Rate', fontsize = 15)

# set the x-axis labels
plt.xticks(np.arange(1, 25, step = 2))

# plot a vertical line across the minimum error rate
plt.axvline(x = 3, color = 'red')

# display the plot
plt.show()
Interpretation: We can see that the optimal value of K (= 3) obtained from the GridSearchCV() results in a lowest error rate.

#Calculate performance measures on the test set.

# print the performance measures for test set for the model with best parameters
# call the function 'get_test_report'
# pass the knn model using GridSearch to the function
print('Classification Report for test set: \n', get_test_report(knn_grid))



# call the function to plot the ROC curve
# pass the knn model to the function
plot_roc(knn_grid)

#Interpretation: From the above plot, we can see that our classifier (knn_model with n_neighbors = 3) is away from the red dotted line; with the AUC score 0.9976.


#4. Naive Bayes Algorithm
#It uses a Bayes' Theorem with the assumption of independence of predictor variables. The sklearn library provides different naive bayes classifiers, as GaussianNB, MultinomialNB and so on.

#Build a naive bayes model on a training dataset.
# instantiate the 'GaussianNB'
gnb = GaussianNB()

# fit the model using fit() on train data
gnb_model = gnb.fit(X_train, y_train)

#Build a confusion matrix.
# call the function to plot the confusion matrix
# pass the gaussian naive bayes model to the function

plot_confusion_matrix(gnb_model)
#Calculate performance measures on the test set.

# compute the performance measures on test data
# call the function 'get_test_report'
# pass the gaussian naive bayes model to the function
test_report = get_test_report(gnb_model)

# print the performace measures
print(test_report)
#Plot the ROC curve.

# call the function to plot the ROC curve
# pass the gaussian naive bayes model to the function
plot_roc(gnb_model)
#Interpretation: From the above plot, we can see that our classifier (gnb_model) is away from the red dotted line; with the AUC score 0.9836.

Note: Algorithms like Naive Bayes and tree based algorithms do not need feature scaling or normalization. Performing a features scaling in these algorithms may not have much effect.


#5. Comparison between KNN Model and Naive Bayes Model
# K Nearest Neighbors
#y_pred_prob_knn = knn_grid.predict_proba(X_test)[:,1]
    
# the roc_curve() returns the values for false positive rate, true positive rate and threshold
# pass the actual target values and predicted probabilities to the function
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob_knn)

# add the AUC score to the plot
auc_score_knn = roc_auc_score(y_test, y_pred_prob_knn)

# plot the ROC curve
plt.plot(fpr, tpr, label='KNN Model (AUC Score = %0.4f)' % auc_score_knn)

# Gaussian Naive Bayes
y_pred_prob_gnb = gnb_model.predict_proba(X_test)[:,1]
    
# the roc_curve() returns the values for false positive rate, true positive rate and threshold
# pass the actual target values and predicted probabilities to the function
fpr, tpr, thresholds = roc_curve(y_test, y_pred_prob_gnb)

# add the AUC score to the plot
auc_score_gnb = roc_auc_score(y_test, y_pred_prob_gnb)

# plot the ROC curve
plt.plot(fpr, tpr, label='GNB Model (AUC Score = %0.4f)' % auc_score_gnb)

# set limits for x and y axes
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.2])

# plot the straight line showing worst prediction for the model
plt.plot([0, 1], [0, 1],'r--')

# add plot and axes labels
# set text size using 'fontsize'
plt.title('GNB Model Vs. KNN Model', fontsize = 15)
plt.xlabel('False positive rate (1-Specificity)', fontsize = 15)
plt.ylabel('True positive rate (Sensitivity)', fontsize = 15)

# set the position of legend
plt.legend(loc = 'lower right')

# plot the grid
plt.grid(True)
#Interpretation: The Auc Score of KNN Model is slightly higher than that of Gaussian Naive Bayes model. but in terms of stability, we can say that Gaussian Naive Bayes model is more stable than the KNN model because the sensitivity and the specificity for Gaussian Naive Bayes model are stable.

      
      
""")