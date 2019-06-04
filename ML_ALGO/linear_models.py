#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 14:02:15 2019

@author: siddharth
"""

import logging

import autograd.numpy as np
import autograd as grad

from base_estimator import BaseEstimator
from metrics.metrics import mean_squared_error,binary_crossentropy

np.random.seed(2019)


class BasicRegression_Wrapper(BaseEstimator):
    
    ''' 
    Wrapper class for linear and logistic regression.
    '''
    def __init__(self,lr=0.001,penalty=None,C=0.01,error_tolerance=0.0001,max_iters = 1000):
        '''
        Trains regression models with gradient descent opitmizers and loss function
        depending upon the type of regression
        
        parameters:
        lr : float, default 0.001
            Learning rate.
        penalty : str, {'l1', 'l2', None'}, default None
            Regularization function name.
        C : float, default 0.01
            The regularization coefficient.
        tolerance : float, default 0.0001
            If the gradient descent updates are smaller than `tolerance`, then
            stop optimization process.
        max_iters : int, default 10000
            The maximum number of iterations.
        '''
        self.lr = lr
        self.penalty = penalty
        self.C = C
        self.error_tolerance = error_tolerance
        self.max_iters = max_iters
        self.errors = []
        self.theta = []
        self.n_samples,self.n_features = None,None
        self.cost_func = None
    
    def _loss(self,wt):
        raise NotImplementedError
        
    def init_cost(self):
        raise NotImplementedError
        
    def _add_penalty(self,loss,wt):
        "Applying regularisation to the cost function i.e. _loss"
        
        if self.penalty=='l1':
            
            # not including the bias term for regularisation
            loss+= self.C * np.abs(wt[1:]).sum()
        
        if self.penalty=='l2':
            
            # not including the bias term for regularisation
            loss+= (0.5*self.C) * (wt[1:] ** 2).sum()
            
        return loss
    
    def _calc_cost(self,x,y,theta):
        
        predictions = x.dot(theta)
        error = self.cost_func(predictions,y)
        return error
    
    def fit(self,x,y):
        
        self._setup_input(x,y)
        self.init_cost()
        self.n_samples,self.n_features = x.shape
        
        # initialize weights and bias terms
        self.theta = np.random.normal(size=(self.n_features+1),scale = 0.5)
        
        # adding the intercept term to the input i.e. x
        self.x = self._add_intercept(self.x)
        
        self._train()
    
    @staticmethod
    def _add_intercept(x):
        first_col = np.ones([x.shape[0],1])
        return np.concatenate([first_col,x],axis=1)
    
    def _train(self):
        self.theta,self.errors = self.gradient_descent()
        logging.info(' Theta : %s '%self.theta.flatten())
        
    def _predict(self,x=None):
        
        x = self._add_intercept(x)
        return x.dot(self.theta)
    
    def _gradient_descent(self):
        theta = self.theta
        
        errors = [self._calc_cost(self.x,self.y,self.theta)]
        
        # "defining" the derivative of the loss function
        grad_calc_def = grad(self._loss)
        
        for i in range(1,self.max_iters+1):
            
            # calculates the gradients for all the inputs to the _loss function
            # in this case it is all the weights gradients being calculated
            
            grad = grad_calc_def(theta)
            theta-= self.lr * grad
            
            errors.append(self._calc_cost(self.x,self.y,theta))
            
            logging.info('Iteration: %s Train cost : %s' %(i,errors[i]))
            
            error_diff = np.linalg.norm(errors[i-1]-errors[i])
            
            if error_diff < self.error_tolerance:
                logging.info('Convergence reached')
                break
        
        return theta,errors


class LinearRegression(BasicRegression_Wrapper):
    '''
    Linear Regression with gradient descent as optimizer
    '''
    
    def _loss(self,wt):
        loss = self._calc_cost(np.dot(self.x,wt),self.y)
        return self._add_penalty(loss,wt)
    
    def init_cost(self):
        self._calc_cost = mean_squared_error

class LogisticRegression(BasicRegression_Wrapper):
    '''
    Binary Logistic Regression with gradient descent as optimizer
    '''
    
    def init_cost(self):
        self._calc_cost = binary_crossentropy
        
    def _loss(self,wt):
        loss = self._calc_cost(self.sigmoid(np.dot(self.x,wt)),self.y)
        return self._add_penalty(loss,wt)
    
    @staticmethod
    def sigmoid(x):
        return 0.5 * (np.tanh(0.5*x)+1)
    
    def _predict(self,x=None):
        x = self._add_intercept(x)
        return self.sigmoid(np.dot(x,self.theta))
        