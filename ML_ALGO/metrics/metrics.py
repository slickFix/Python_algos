#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 12:06:19 2019

@author: siddharth
"""

import autograd.numpy as np

tend_to_zero = 1e-15

def unhot(function):
    ''' converts one hot representation to single col'''
    
    def wrapper(predictions,actuals):
        
        if len(predictions.shape)>1 and predictions.shape[1]>1:
            predictions = predictions.argmax(axis=1)
            
        if len(actuals.shape)>1 and actuals.shape[1]>1:
            actuals = actuals.argmax(axis=1)
            
        return function(predictions,actuals)
    
    return wrapper


def absolute_error(predictions,actuals):
    return np.abs(actuals-predictions)

def mean_absolute_error(predictions,actuals):
    return np.mean(absolute_error(predictions,actuals))

@unhot
def classification_error(predictions,actuals):
    return (predictions!=actuals).sum()/float(actuals.shape[0])

@unhot
def accuracy(predictions,actuals):
    return 1.0-classification_error(predictions,actuals)

def squared_error(predictions,actuals):
    return (predictions-actuals) ** 2

def mean_squared_error(predictions,actuals):
    return np.mean(squared_error(predictions,actuals))

def squared_log_error(predictions,actuals):
    return (np.log(np.array(predictions)+1) - np.log(np.array(actuals)+1)) ** 2

def mean_squared_log_error(predictions,actuals):
    return np.mean(squared_log_error(predictions,actuals))

def root_mean_squared_error(predictions,actuals):
    return np.sqrt(mean_squared_error(predictions,actuals))

def root_mean_squared_log_error(predictions,actuals):
    return np.sqrt(mean_squared_log_error(predictions,actuals))

def log_loss(predictions,actuals):
    predictions = np.clip(predictions,tend_to_zero,1-tend_to_zero)
    loss =  - np.sum(actuals*np.log(predictions))
    return loss/float(actuals.shape[0])

def hinge(predictions,actuals):
    ''' if the actual class is +1 then if the predictions are greater than +1, then loss is zero
    but it increases linearly for predictions less than +1.
    Similarly if the actual is -1 then if the predictions are less than -1, then loss is zero
    but it increases linearly for predictions greater than -1. '''
    
    return np.mean(np.max(0,1-predictions*actuals))

def binary_crossentropy(predictions,actuals):
    predictions = np.clip(predictions,tend_to_zero,1-tend_to_zero)
    return (-np.sum(actuals*np.log(predictions) + (1-actuals)*np.log(1-predictions)))/float(actuals.shape[0])


# defining alias
    
mse = mean_squared_error
msa = mean_absolute_error
rmse = root_mean_squared_error


def get_metric(name):
    ''' Returns the metric function by name '''
    
    try:
        return globals()[name]
    except:
        raise ValueError('Invalid metric function..')