import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def plot_client(client_train):
    year=client_train.groupby(['creation_year'])['client_id'].count()
    plt.figure(figsize=(10,5))
    plt.plot(year)
    
def plot_client_per_year(client_train,E):
    E1=[i for i in E]
    groups = client_train.groupby(['creation_year','client_catg'])['client_id'].count()
    L11=[]
    L12=[]
    L51=[]
    for i in E:
        L11.append(groups[i][11])
        L12.append(groups[i][12])
        L51.append(groups[i][51])
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 5)
    ax.plot(E1, L11,label='cat_11')
    ax.plot(E1, L12,label='cat_12')
    ax.plot(E1, L51,label='cat_51')
    plt.title("Number of customers by year")
    plt.legend()
    plt.show()
    #" Logarithmic plot "
    logL11 = list(map(np.log, L11))
    logL12 = list(map(np.log, L12))
    logL51 = list(map(np.log, L51))
    fig, ax = plt.subplots()
    fig.set_size_inches(10, 5)
    ax.plot(E1, logL11,label='cat_11')
    ax.plot(E1, logL12,label='cat_12')
    ax.plot(E1, logL51,label='cat_51')
    plt.title("Logarithmic number of customers by year")
    plt.legend()
    plt.show()
    
def plot_counter_type(invoice_train):
    C=invoice_train['counter_type'].tolist()
    elec=C.count('ELEC')*100/len(C)
    gaz=C.count('GAZ')*100/len(C)
    plt.figure(figsize=(6,6))
    plt.pie([elec,gaz], labels = ['ELEC','GAZ'],autopct='%1.1f%%')
    plt.title("Proportion of Counter type (ELEC to GAZ)")
    plt.show()
    
def plot_fraud(invoice_train):
    C=invoice_train['target'].tolist()
    elec=C.count(0)*100/len(C)
    gaz=C.count(1)*100/len(C)
    plt.figure(figsize=(6,6))
    plt.pie([elec,gaz], labels = ['not fraud','fraud'],autopct='%1.1f%%')
    plt.title("Target Varaible distribution")
    plt.show()
    
def target_distribution_by(client_train,var,t):
    L=client_train.groupby([var])['client_id'].count().index.tolist()
    fraudactivities = client_train.groupby([var,'target'])['client_id'].count()
    figure, axis = plt.subplots(t[0],t[1])
    figure.set_size_inches(10, 5)
    c=0
    for i in range(t[0]):
        for j in range(t[1]):
            if(c<len(L)):
                axis[i,j].bar(x=fraudactivities[L[c]].index, height=fraudactivities[L[c]].values, tick_label = [0,1])
                axis[i,j].set_title(var+' '+str(L[c])+' fraude distribution')
                c=c+1
    plt.show() 
    
def farud_by_counter(client_train,invoice_train):
    df1=client_train[['client_id', 'target']]
    df2=invoice_train[['client_id', 'counter_type']]
    df3=pd.merge(df1, df2, on='client_id', how='left')
    df4=df3[['counter_type', 'target']].groupby(['counter_type']).mean()
    f=df4['target']['ELEC']
    plt.figure(figsize=(6,6))
    plt.pie([f*100,(1-f)*100], labels = ['fraud','not fraud'],autopct='%1.1f%%')
    plt.title("Target Varaible distribution for Electricity")
    plt.show()
    f=df4['target']['GAZ']
    plt.figure(figsize=(6,6))
    plt.pie([f*100,(1-f)*100], labels = ['fraud','not fraud'],autopct='%1.1f%%')
    plt.title("Target Varaible distribution for Gaz")
    plt.show()
    return df4