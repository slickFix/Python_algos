#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 31 09:41:46 2019

@author: siddharth
"""

import numpy as np

class BaseEstimator(object):
    
    x= None
    y = None
    y_required = True
    fit_required = True
    
    def _setup_input(self,x,y=None):
        """Ensure inputs to an estimator are in the expected (size,dim etc) format.
        Ensures X and y are stored as numpy ndarrays by converting from an
        array-like object if necessary. Enables estimators to define whether
        they require a set of y target values or not with y_required, e.g.
        kmeans clustering requires no target labels and is fit against only X.
        Parameters
        ----------
        X : array-like
            Feature dataset.
        y : array-like
            Target values. By default is required, but if y_required = false
            then may be omitted.
        """
        
        if not isinstance(x,np.ndarray):
            x = np.array(x)
        
        if x.size() == 0 :
            raise ValueError('Number of features must be >0')
            
        if x.ndim == 1:
            self.n_samples,self.n_features = 1,x.shape
        else:
            self.n_samples,self.n_features = x.shape[0],len(x.shape[1:])
        
        self.x = x
        
        if self.y_required:
            
            if y is None:
                raise ValueError('Missing required argument y')
            
            if not isinstance(y,np.ndarray):
                y = np.array(y)
            
            if y.size() ==0:
                raise ValueError('Number of targets must be >0')
                
        self.y = y
        
    def fit(self,x,y=None):
        self._setup_input(x,y)
        
    def predict(self,x,y=None):
        
        if not isinstance(x,np.ndarray):
            x = np.array(x)
            
        if self.x is not None and not self.fit_required:
            return self._predict(x)
        else:
            raise ValueError("Either input is null or fit is not called or both..")
            
    def _predict(self,x):
        raise NotImplementedError()