#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:42:07 2019

@author: siddharth
"""

import numpy as np
from base_estimator import BaseEstimator


class NaiveBayesClassifier(BaseEstimator):
    
    ''' Implementing for binary class only '''
    
    n_classes = 2
    
    def fit(self,x,y = None):
        
        self._setup_input(x,y)
        
        # checking the target labels
        assert np.unique(y) == [0,1]
        
        self._mean = np.zeros((self.n_classes,self.n_features),dtype = np.float32)
        self._var = np.zeros((self.n_classes,self.n_features),dtype = np.float32)
        self._prior = np.zeros(self.n_classes,dtype = np.float32)
        
        for cl in range(self.n_classes):
            
            # masking the index [True,False,False,True,False] 
            x_c = x[y==cl]
            
            self._mean[cl] = np.mean(x_c,axis=0)
            self._var[cl] =  np.var(x_c,axis=0)
            
            self._prior = x_c.shape[0]/float(x.shape[0])
            
    def _predict(self,x,y=None):
        
        predictions = np.apply_along_axis(self._predict_each_row,1,x)
        
        # normalizing the probabilities
        
        ex = np.exp(predictions)
        
        norm_prob = ex/np.sum(ex,axis=1,keepdims=True)
        
        return norm_prob
            
    
    def _predict_each_row(self,x):
        
        ''' predicting the log likelihood '''
        
        output = []
        
        for cl in range(self.n_classes):
            prior_prob = np.log(self._prior[cl])      
            
            likelihood_prob = np.log(self._pdf(x,cl)).sum()
            
            # We are adding probabilities as multiplicative prob becomes additive after log
            total_prob = prior_prob + likelihood_prob
            
            output.append(total_prob)
        
        return output
    
    def _pdf(self,x,y):
        
        mean = self._mean[y]
        var = self._var[y]
        
        numerator = np.exp(-(x-mean)**2 / (2*var))
        denominator  = np.sqrt(2*np.pi * var)
        
        return numerator/denominator