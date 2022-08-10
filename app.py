# -*- coding: utf-8 -*-
"""
Created on Wed Aug 10 14:58:55 2022

@author: Paurash
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

## loading Saved Models

credit_card_fraud_pred= pickle.load(open('credit_card_fraud_pred.sav', 'rb'))


## Side Bar for Navigation for Different Diseases

with st.sidebar:
    
    selected = option_menu('Credit Card Fraud Detection System',
                           ['Credit Card Prediction'],
                           icons= ['credit-card'],
                           default_index=0)
    
## credit Card Draud Predication Page

if (selected=='Credit Card Prediction'):
    
    # Page Title
    st.title("Credit Card Fraud Detection")
    
## Getting Input data from User if 1st selected
    col1, col2, col3, col4, col5 = st.columns(5)
    
    
    with col1:
        V1 = st.text_input('V1')
        
    with col2:
        V2 = st.text_input('V2')
        
    with col3:
        V3 = st.text_input('V3')
     
    with col4:
        V4 = st.text_input('V4')
        
    with col5:
        V5 = st.text_input('V5')
        
    with col1:
        V6 = st.text_input('V6')
    
    with col2:
        V7 = st.text_input('V7')
    
    with col3:
        V8 = st.text_input('V8')
        
    with col4:
         V9 = st.text_input('V9')
         
    with col5:
         V10 = st.text_input('V10')
    
    with col1:
        V11 = st.text_input('V11')
    
    with col2:
        V12 = st.text_input('V12')    
    
    with col3:
        V13 = st.text_input('V13')
        
    with col4:
         V14 = st.text_input('V14')
         
    with col5:
         V15 = st.text_input('V15')
         
    with col1:
        V16 = st.text_input('V16')
    
    with col2:
        V17 = st.text_input('V17')    
    
    with col3:
        V18 = st.text_input('V18')
        
    with col4:
         V19 = st.text_input('V19')
         
    with col5:
         V20 = st.text_input('V20')
         
    with col1:
        V21 = st.text_input('V21')
    
    with col2:
        V22 = st.text_input('V22')    
    
    with col3:
        V23 = st.text_input('V23')
        
    with col4:
         V24 = st.text_input('V24')
         
    with col5:
         V25 = st.text_input('V25')
      
    with col1:
         V26 = st.text_input('V26')
     
    with col2:
         V27 = st.text_input('V27')    
     
    with col3:
         V28 = st.text_input('V28')
         
    with col4:
         Amount = st.text_input('Amount')
         
        
## Code for Predication

    fraud_predication =''
    
## Creating a Button for Predication
    if st.button('Prediction Test Result'):
        fraud_pred = credit_card_fraud_pred.predict([[V1,V2,V3,V4,V5,V6,V7,V8,V9,V10,V11,V12,V13,V14,V15,V16,V17,V18,V19,V20,V21,V22,V23,V24,V25,V26,V27,V28,Amount]])
        
        if (fraud_pred[0] == 0):
            fraud_predication ="This is valid Trasaction"
        else:
            fraud_predication ="This is Fraudulent Transaction"
            
    st.success(fraud_predication)
        
        