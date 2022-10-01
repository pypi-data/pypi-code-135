import numpy as np
import pandas as pd
import csv
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination

class BN:
    def __init__(self):
        self.data = pd.read_csv('7-dataset.csv')
        self.data = self.data.replace('?', np.nan)

    def show(self):
        print('Sample instances from the dataset are given below')
        print(self.data.head())
        print('\n Attributes and datatypes')
        print(self.show.dtypes)


    def selectandfit(self):
        self.model = BayesianModel(
            [('age', 'heartdisease'), ('gender', 'heartdisease'), ('cp', 'heartdisease'), ('trestbps', 'heartdisease'),
             ('heartdisease', 'chol'), ('heartdisease', 'fbs'), ('heartdisease', 'restecg'),
             ('heartdisease', 'thalach'), ('heartdisease', 'exang'), ('heartdisease', 'oldpeak')])

        print('\nLearning CPD using Maximum likelihood estimators')
        self.model.fit(self.data, estimator=MaximumLikelihoodEstimator)

        print('\n Inferencing with Bayesian Network:')
        self.HeartDiseasetest_infer = VariableElimination(self.model)


    def probability(self):
        print('\nProbability of HeartDisease given evidence= restecg')
        self.q1=self.HeartDiseasetest_infer.query(variables=['heartdisease'], evidence={'restecg':1})
        print(self.q1)
        print('\n 2. Probability of HeartDisease given evidence= cp ')
        self.q2=self.HeartDiseasetest_infer.query(variables=['heartdisease'], evidence={'cp':2})
        print(self.q2)
