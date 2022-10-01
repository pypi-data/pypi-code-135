import time
import pandas as pd
import numpy as np
import tensorflow as tf
from keras import metrics
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import SGDClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import AdaBoostClassifier
from xgboost import XGBClassifier
from lightgbm import LGBMClassifier
from catboost import CatBoostClassifier
from sklearn.linear_model import PassiveAggressiveClassifier
from sklearn.ensemble import BaggingClassifier

from sklearn.linear_model import LinearRegression
from sklearn.svm import SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from lightgbm import LGBMRegressor
from xgboost.sklearn import XGBRegressor
from sklearn.ensemble import AdaBoostRegressor
from catboost import CatBoostRegressor
from sklearn.linear_model import SGDRegressor
from sklearn.kernel_ridge import KernelRidge
from sklearn.linear_model import ElasticNet
from sklearn.linear_model import BayesianRidge
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsRegressor

from keras.models import Sequential
from keras.layers import Dense, Dropout
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from tensorflow.keras.losses import MeanSquaredError
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score
from keras.utils import np_utils
from sklearn import metrics

import plotly.graph_objects as go
import joblib
import os


def convert_plotly_plots_to_html(fig, path, name):
    fig.write_html(path + '/file_'+ name +'.html')

def convert_df_to_plotly_table(df, title=""):
    rowEvenColor = '#7094db'
    rowOddColor = '#adc2eb'
    
    n=len(list(df.columns))
    fig = go.Figure(data=[go.Table(
    columnwidth = [1000]*n,
    header=dict(values=list(df.columns),
                line_color='white',
                fill_color='#24478f',
                align = ['left', 'center'],
                font = dict(color = 'seashell', size = 15),
                height=50),
    
    cells=dict(values=df.transpose().values.tolist(),
               line_color='white',
               fill_color = [[rowOddColor,rowEvenColor]*1000],
               align = ['left', 'center'],
               font = dict(color = 'black', size = 15),
               height=40
              ))])

    fig.update_layout(
        margin=dict(l=0, r=0, t=50, b=0),
        paper_bgcolor="#feffe7",
        title=title
    )
    return fig

def neural_network_classification_multiclass(x_train, x_test, y_train, y_test, D, saveModel, path, num):
    name = "Perceptron (NN) Classifier"
    input_dim1 = len(x_train.columns)
    start = time.time()

    model = Sequential()
    model.add(Dense(16, input_dim=input_dim1,
              kernel_initializer='normal', activation='relu'))
    Dropout(0.2),
    model.add(Dense(32, kernel_initializer='normal', activation='relu'))
    Dropout(0.2),
    model.add(Dense(64, kernel_initializer='normal', activation='relu'))
    Dropout(0.2),
    model.add(Dense(128, kernel_initializer='normal', activation='relu'))
    Dropout(0.2),
    model.add(Dense(num, activation='softmax'))
    model.compile(loss='sparse_categorical_crossentropy',
                  optimizer='adam', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=100, verbose=0)

    Y_pred_class = np.argmax(model.predict(x_test), axis=-1)
    Y_val_class = y_test.values

    precision = metrics.precision_score(
        Y_val_class, Y_pred_class, average='macro')
    recall = metrics.recall_score(Y_val_class, Y_pred_class, average='macro')
    f1_score = metrics.f1_score(Y_val_class, Y_pred_class, average='weighted')
    Accuracy_score = metrics.accuracy_score(Y_val_class, Y_pred_class)
    end = time.time()
    time_taken = (end - start)

    D['Accuracy'].append(Accuracy_score)
    D['F1_score'].append(f1_score)
    D['Classifier_name'].append(name)
    D['Time_taken'].append(time_taken)
    D['Precision'].append(precision)
    D['Recall'].append(recall)

    if saveModel:
      if not os.path.exists(path+"/Models"):
        os.makedirs(path+"/Models")
    joblib.dump(model, path +"/Models"+ "/" + name +'.pkl')


def neural_network_classification_binary(x_train, x_test, y_train, y_test, D, saveModel, path):
    name = "Perceptron (NN) Classifier"
    input_dim1 = len(x_train.columns)
    start = time.time()

    model = Sequential()
    model.add(Dense(16, input_dim=input_dim1,
              kernel_initializer='normal', activation='relu'))
    Dropout(0.2),
    model.add(Dense(32, kernel_initializer='normal', activation='relu'))
    Dropout(0.2),
    model.add(Dense(64, kernel_initializer='normal', activation='relu'))
    Dropout(0.2),
    model.add(Dense(128, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(loss='binary_crossentropy',
                  optimizer='adam', metrics=['accuracy'])
    model.fit(x_train, y_train, epochs=100, verbose=0)
    end = time.time()
    time_taken = (end - start)

    Y_pred_class = np.argmax(model.predict(x_test), axis=-1)
    Y_val_class = y_test.values

    precision = metrics.precision_score(
        Y_val_class, Y_pred_class, average='macro')
    recall = metrics.recall_score(Y_val_class, Y_pred_class, average='macro')
    f1_score = metrics.f1_score(Y_val_class, Y_pred_class, average='weighted')
    Accuracy_score = metrics.accuracy_score(Y_val_class, Y_pred_class)

    D['Accuracy'].append(Accuracy_score)
    D['F1_score'].append(f1_score)
    D['Classifier_name'].append(name)
    D['Time_taken'].append(time_taken)
    D['Precision'].append(precision)
    D['Recall'].append(recall)

    if saveModel:
      if not os.path.exists(path+"/Models"):
        os.makedirs(path+"/Models")
    joblib.dump(model, path +"/Models"+ "/" + name +'.pkl')

    
def neural_network_regression(x_train, x_test, y_train, y_test, loss, act_func, D, df_test, df_train, saveModel, path):
    name = "Perceptron (NN) Regressor"
    input_dim1 = len(x_train.columns)
    start = time.time()

    model = Sequential()
    model.add(Dense(16, input_dim=input_dim1,
              kernel_initializer='normal', activation='relu'))
    Dropout(0.2),
    model.add(Dense(32, kernel_initializer='normal', activation='relu'))
    Dropout(0.2),
    model.add(Dense(64, kernel_initializer='normal', activation='relu'))
    Dropout(0.2),
    model.add(Dense(128, kernel_initializer='normal', activation='relu'))
    model.add(Dense(1, kernel_initializer='normal', activation=act_func))

    model.compile(loss=loss, optimizer='adam', metrics=['mse'])
    model.fit(x_train, y_train, epochs=100, verbose=0)

    end = time.time()
    time_taken = (end - start)
    y_pred = model.predict(x_test)

    mse = mean_squared_error(y_test, y_pred, squared=True)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    mae = mean_absolute_error(y_test, y_pred)
    r_square = (r2_score(y_test, y_pred))
    adjusted_r_squared = 1 - \
        (1 - r_square) * (len(df_test) - 1) / \
        (len(df_test) - df_train.shape[1] - 1)

    D['MSE'].append(mse)
    D['RMSE'].append(rmse)
    D['Regressor_name'].append(name)
    D['Time_taken'].append(time_taken)
    D['MAE'].append(mae)
    D['R-Square'].append(r_square)
    D['Adjusted-R-Square'].append(adjusted_r_squared)
    if saveModel:
      if not os.path.exists(path+"/Models"):
        os.makedirs(path+"/Models")
    joblib.dump(model, path +"/Models"+ "/" + name +'.pkl')
    

def Multiclass_Classification(X_train, X_test, y_train, y_test, classifier, name, D, saveModel, path):
    start = time.time()
    # Define model
    model = classifier
    # Training model
    model.fit(X_train, y_train)
    # Prediction using model
    y_pred = model.predict(X_test)
    # evaluating model
    Accuracy_score = accuracy_score(y_test, y_pred)
    F1_score = f1_score(y_test, y_pred, average='weighted')
    precision_scores = precision_score(y_test, y_pred, average="macro")
    recall_scores = recall_score(y_test, y_pred, average="macro")

    end = time.time()
    time_taken = (end - start)
    D['Accuracy'].append(Accuracy_score)
    D['F1_score'].append(F1_score)
    D['Classifier_name'].append(name)
    D['Time_taken'].append(time_taken)
    D['Precision'].append(precision_scores)
    D['Recall'].append(recall_scores)

    if saveModel:
      if not os.path.exists(path+"/Models"):
        os.makedirs(path+"/Models")
    joblib.dump(model, path +"/Models"+ "/" + name +'.pkl')


def classification_report_generation(df, target, n, path=".", saveModel=False):
    
    if not os.path.exists(path):
        os.makedirs(path)

    D = {'Classifier_name': [], 'Accuracy': [], 'F1_score': [],
         'Precision': [], 'Recall': [], 'Time_taken': []}
    # Selecting the columns and dividing data into train and test
    df_train = df[[col for col in list(df.columns) if col != target]]
    df_test = df[target]

    x_train, x_test, y_train, y_test = train_test_split(
        df_train, df_test, test_size=0.20, random_state=0)

    if n == 2:
        # check the evaluation metric with different classifiers out of that xgboost is performing well
        print("Running Logistic Regression Classifier")
        Multiclass_Classification(
            x_train, x_test, y_train, y_test, LogisticRegression(), "Logistic Regression", D, saveModel, path)
        print("Running GaussianNB Classifier")
        Multiclass_Classification(
            x_train, x_test, y_train, y_test, GaussianNB(), "GaussianNB", D, saveModel, path)
        print("Running Decision Tree Classifier")
        Multiclass_Classification(x_train, x_test, y_train, y_test,
                                  DecisionTreeClassifier(), "Decision Tree Classifier", D, saveModel, path)
        print("Running Random Forest Classifier")
        Multiclass_Classification(x_train, x_test, y_train, y_test,
                                  RandomForestClassifier(), "Random Forest Classifier", D, saveModel, path)
        print("Running Gradient Boosting Classifier")
        Multiclass_Classification(x_train, x_test, y_train, y_test, GradientBoostingClassifier(
        ), "Gradient Boosting Classifier", D, saveModel, path)
        print("Running XGBoost Classifier")
        Multiclass_Classification(
            x_train, x_test, y_train, y_test, XGBClassifier(), "XGBoost Classifier", D, saveModel, path)
        print("Running Light GBM Classifier")
        Multiclass_Classification(
            x_train, x_test, y_train, y_test, LGBMClassifier(), "Light GBM Classifier", D, saveModel, path)
        print("Running Ada Boost Classifier")
        Multiclass_Classification(
            x_train, x_test, y_train, y_test, AdaBoostClassifier(), "Ada Boost Classifier", D, saveModel, path)
        print("Running SVM Classifier")
        Multiclass_Classification(
            x_train, x_test, y_train, y_test, SVC(), "SVM Classifier", D, saveModel, path)
        print("Running Neural Network Classifier")
        neural_network_classification_binary(x_train, x_test, y_train, y_test, D, saveModel, path)
        print("Running Stochastic Gradient Descent Classifier")
        Multiclass_Classification(x_train, x_test, y_train, y_test, SGDClassifier(
        ), "Stochastic Gradient Descent Classifier", D, saveModel, path)
        print("Running K-Nearest Neighbor Classifier")
        Multiclass_Classification(x_train, x_test, y_train, y_test, KNeighborsClassifier(
        ), "K-Nearest Neighbor Classifier", D, saveModel, path)
        print("Running Cat Boost Classifier")
        Multiclass_Classification(
            x_train, x_test, y_train, y_test, CatBoostClassifier(verbose=False), "Cat Boost Classifier", D, saveModel, path)
        print("Running Linear Discriminant Analysis Classifier")
        Multiclass_Classification(x_train, x_test, y_train, y_test, LinearDiscriminantAnalysis(
        ), "Linear Discriminant Analysis", D, saveModel, path)
        print("Running Passive Aggressive Classifier")
        Multiclass_Classification(x_train, x_test, y_train, y_test, PassiveAggressiveClassifier(
        ), "Passive Aggressive Classifier", D, saveModel, path)
        print("Running Bagging Classifier")
        Multiclass_Classification(x_train, x_test, y_train, y_test, BaggingClassifier(base_estimator=SVC()),
        "Bagging Classifier", D, saveModel, path)

    if n > 2:
        # check the evaluation metric with different classifiers out of that xgboost is performing well
        print("Running Logistic Regression")
        Multiclass_Classification(x_train, x_test, y_train, y_test, LogisticRegression(
            multi_class='multinomial', max_iter=10000,  solver='lbfgs'), "Logistic Regression", D, saveModel, path)
        print("Running GaussianNB")
        Multiclass_Classification(
            x_train, x_test, y_train, y_test, GaussianNB(), "GaussianNB", D, saveModel, path)
        print("Running Decision Tree Classifier")
        Multiclass_Classification(x_train, x_test, y_train, y_test,
                                  DecisionTreeClassifier(), "Decision Tree Classifier", D, saveModel, path)
        print("Running Random Forest Classifier")
        Multiclass_Classification(x_train, x_test, y_train, y_test,
                                  RandomForestClassifier(), "Random Forest Classifier", D, saveModel, path)
        print("Running Gradient Boosting Classifier")
        Multiclass_Classification(x_train, x_test, y_train, y_test, GradientBoostingClassifier(
        ), "Gradient Boosting Classifier", D, saveModel, path)
        print("Running XGBoost Classifier")
        Multiclass_Classification(
            x_train, x_test, y_train, y_test, XGBClassifier(), "XGBoost Classifier", D, saveModel, path)
        print("Running Light GBM Classifier")
        Multiclass_Classification(
            x_train, x_test, y_train, y_test, LGBMClassifier(), "Light GBM Classifier", D, saveModel, path)
        print("Running Ada Boost Classifier")
        Multiclass_Classification(
            x_train, x_test, y_train, y_test, AdaBoostClassifier(), "Ada Boost Classifier", D, saveModel, path)
        print("Running SVM Classifier")
        Multiclass_Classification(
            x_train, x_test, y_train, y_test, SVC(), "SVM Classifier", D, saveModel, path)
        
        print("Running Neural Network")
        neural_network_classification_multiclass(x_train, x_test, y_train, y_test, D, saveModel, path, num=n)
        
        print("Running Stochastic Gradient Descent Classifier")
        Multiclass_Classification(x_train, x_test, y_train, y_test, SGDClassifier(
        ), "Stochastic Gradient Descent Classifier", D, saveModel, path)
        print("Running K-Nearest Neighbor Classifier")
        Multiclass_Classification(x_train, x_test, y_train, y_test, KNeighborsClassifier(
        ), "K-Nearest Neighbor Classifier", D, saveModel, path)
        print("Running Cat Boost Classifier")
        Multiclass_Classification(
            x_train, x_test, y_train, y_test, CatBoostClassifier(verbose=False), "Cat Boost Classifier", D, saveModel, path)
        print("Running Linear Discriminant Analysis")
        Multiclass_Classification(x_train, x_test, y_train, y_test, LinearDiscriminantAnalysis(
        ), "Linear Discriminant Analysis", D, saveModel, path)
        print("Running Passive Aggressive Classifier")
        Multiclass_Classification(x_train, x_test, y_train, y_test, PassiveAggressiveClassifier(
        ), "Passive Aggressive Classifier", D, saveModel, path)
        print("Running Bagging Classifier")
        Multiclass_Classification(x_train, x_test, y_train, y_test, BaggingClassifier(base_estimator=SVC()),
        "Bagging Classifier", D, saveModel, path)

    Classfication_report = pd.DataFrame(D)
    
    fig_class_report = convert_df_to_plotly_table(
        Classfication_report, title="Classification Report")
    convert_plotly_plots_to_html(fig_class_report, path, "CLASSIFICATION REPORT")

    return Classfication_report


def Regression(X_train, X_test, y_train, y_test, regres, name, D, df_test, df_train, saveModel, path):
    start = time.time()
    model = regres
    # Training model
    model.fit(X_train, y_train)
    # Prediction using model
    y_pred = model.predict(X_test)
    # error calculation
    mse = mean_squared_error(y_test, y_pred, squared=True)
    rmse = mean_squared_error(y_test, y_pred, squared=False)
    mae = mean_absolute_error(y_test, y_pred)
    # getting R Squared
    r_square = (r2_score(y_test, y_pred))
    # getting adjusted R Squared
    adjusted_r_squared = 1 - \
        (1 - r_square) * (len(df_test) - 1) / \
        (len(df_test) - df_train.shape[1] - 1)
    end = time.time()
    time_taken = (end - start)
    D['MSE'].append(mse)
    D['RMSE'].append(rmse)
    D['Regressor_name'].append(name)
    D['Time_taken'].append(time_taken)
    D['MAE'].append(mae)
    D['R-Square'].append(r_square)
    D['Adjusted-R-Square'].append(adjusted_r_squared)
    if saveModel:
      if not os.path.exists(path+"/Models"):
        os.makedirs(path+"/Models")
    joblib.dump(model, path +"/Models"+ "/" + name +'.pkl')


def regression_report_generation(df, target, path=".", saveModel=False):
    if not os.path.exists(path):
        os.makedirs(path)

    D = {'Regressor_name': [], 'MSE': [], 'RMSE': [], 'MAE': [],
         'R-Square': [], 'Adjusted-R-Square': [], 'Time_taken': []}
    # Selecting the columns and dividing data into train and test
    df_train = df[[col for col in list(df.columns) if col != target]]
    df_test = df[target]
    x_train, x_test, y_train, y_test = train_test_split(
        df_train, df_test, test_size=0.20, random_state=0)
    print("Running Linear Regressor")
    Regression(x_train, x_test, y_train, y_test, LinearRegression(),
               "Linear Regressor", D, df_test, df_train, saveModel, path)
    print("Running Decision Tree Regressor")
    Regression(x_train, x_test, y_train, y_test, DecisionTreeRegressor(),
               "Decision Tree Regressor", D, df_test, df_train, saveModel, path)
    print("Running  Random Forest Regressor")
    Regression(x_train, x_test, y_train, y_test, RandomForestRegressor(),
               "Random Forest Regressor", D, df_test, df_train, saveModel, path)
    print("Running Support Vector Regressor")
    Regression(x_train, x_test, y_train, y_test, SVR(),
               "Support Vector regressor", D, df_test, df_train, saveModel, path)
    print("Running Light GBM Regressor")
    Regression(x_train, x_test, y_train, y_test, LGBMRegressor(),
               "Light GBM Regressor", D, df_test, df_train, saveModel, path)
    print("Running Xg Boost Regressor")
    Regression(x_train, x_test, y_train, y_test, XGBRegressor(),
               "Xg Boost Regressor", D, df_test, df_train, saveModel, path)
    print("Running Ada Boost Regressor")
    Regression(x_train, x_test, y_train, y_test, AdaBoostRegressor(),
               "Ada Boost Regressor", D, df_test, df_train, saveModel, path)
    print("Running Neural Network Regressor")
    neural_network_regression(x_train, x_test, y_train, y_test,
                              "MeanSquaredError", "linear", D, df_test, df_train, saveModel, path)
    print("Running Cat Boost Regressor")
    Regression(x_train, x_test, y_train, y_test, CatBoostRegressor(verbose=False),
               "Cat Boost regressor", D, df_test, df_train, saveModel, path)
    print("Running Stochastic Gradient Descent Regressor")
    Regression(x_train, x_test, y_train, y_test, SGDRegressor(),
               "Stochastic Gradient Descent Regressor", D, df_test, df_train, saveModel, path)
    print("Running Kernel Ridge Regressor")
    Regression(x_train, x_test, y_train, y_test, KernelRidge(),
               "Kernel Ridge Regressor", D, df_test, df_train, saveModel, path)
    print("Running Elastic Net Regressor")
    Regression(x_train, x_test, y_train, y_test, ElasticNet(),
               "Elastic Net Regressor", D, df_test, df_train, saveModel, path)
    print("Running Bayesian Ridge Regressor")
    Regression(x_train, x_test, y_train, y_test, BayesianRidge(),
               "Bayesian Ridge Regressor", D, df_test, df_train, saveModel, path)
    print("Running Gradient Boosting Regressor")
    Regression(x_train, x_test, y_train, y_test, GradientBoostingRegressor(
    ), "Gradient Boosting Regressor", D, df_test, df_train, saveModel, path)
    print("Running Elastic Net Regressor")
    Regression(x_train, x_test, y_train, y_test, ElasticNet(),
               "Elastic Net Regressor", D, df_test, df_train, saveModel, path)
    print("Running K Nearest Neighbors Regressor")
    Regression(x_train, x_test, y_train, y_test, KNeighborsRegressor(),
               "K Nearest Neighbors Regressor", D, df_test, df_train, saveModel, path)
    
    regression_report = pd.DataFrame(D)
    
    fig_reg_report = convert_df_to_plotly_table(
        regression_report, title="Regression Report")
    convert_plotly_plots_to_html(fig_reg_report, path,"REGRESSION REPORT")
        
    return regression_report
