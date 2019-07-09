#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:29:22 2019

@author: siddharth
"""

import numpy as np

from base_estimator import BaseEstimator
from ensemble_utils import mse_criterion
from decision_tree import Decision_tree

# logistic function
from scipy.special import expit

class Loss:
    ''' 
        Base class for loss function.
        These loss functions are used for evaluations of the gbm split.
    
    '''
    
    def __init__(self,regularization=1.0):
        self.regularization = regularization
        
    
    def grad(self,predicted,actual):
        '''First order gradient. '''
        
        raise NotImplementedError()
        
    def hess(self,predicted,actual):
        '''Second order gradient. '''
        
        raise NotImplementedError()
    
    def approximate(self,predicted,actual):
        ''' Approximate a leaf value '''
        
        return self.grad(predicted,actual).sum() / (self.hess(predicted,actual).sum()+ self.regularization)
    
    def transform(self,pred):
        ''' Transform the prediction values. '''
        
        return pred
    
    def gain(self,predicted,actual):
        ''' Calculate the gain for each of the splits for the search '''
        
        numerator = self.grad(predicted,actual).sum() ** 2
        denominator = (self.hess(predicted,actual).sum() + self.regularization)
        
        return 0.5 * (numerator/denominator)
    
class LeastSquareLoss(Loss):
    ''' Least square loss used for gbm regression'''
    
    def grad(self, predicted,actual):
        return actual - predicted
    
    def hess (self, predicted, actual):
        
        return np.ones_like(actual)
    
    
class LogisticLoss(Loss):
    ''' Logistic Loss used for gbm classification '''
    
    def grad(self,predicted,actual):
        
        return actual * expit(-actual*predicted)
    
    def hess(self,predicted,actual):
        
        expits = expit(predicted)
        return expits * (1-expits)
    
    
    def transform(self,output):
         # Apply logistic sigmoid function to the output
         
         return expit(output)
        
class GradientBoosting(BaseEstimator):
    
    ''' Base class for GradientBoosting Trees using Taylor's expansion approximation (same as XgBoost) '''
    
    def __init__(self,n_estimators,max_depth=2,max_features=10,min_samples_split=10,learning_rate=0.1):
        self.n_estimators = n_estimators
        self.max_depth = max_depth
        self.max_features = max_features
        self.min_samples_split = min_samples_split
        self.learning_rate = learning_rate
        self.d_trees = []
        self.loss = None
    
    def fit(self,x,y=None):
        self._setup_input(x,y)
        self.y_mean = np.mean(y)
        self._train()
    
    def _train(self):
        
        y_pred = np.zeros(self.n_samples,np.float32)
        
        for n in range(self.n_estimators):
            
            residuals = self.loss.grad(y_pred,self.y)
            
            d_tree = Decision_tree(regression=True,criterion=mse_criterion)
            
            # passing the target values to the tree learner
            
            targets = {
                    # residual values
                    'y':residuals,
                    
                    # Actual target value
                    
                    'actual':self.y,
                    
                    # Predictions from previous step
                    
                    'y_pred':y_pred
                    }
        
        
            d_tree.train(self,targets,max_features=self.max_features,max_depth=self.max_depth,
                         min_samples_split=self.min_samples_split,loss= self.loss)
            
            predictions = d_tree.predict(self.x)
            y_pred +=self.learning_rate*predictions
            self.d_trees.append(d_tree)
    