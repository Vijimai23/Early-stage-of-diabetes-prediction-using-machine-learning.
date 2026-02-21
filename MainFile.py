# ====================== IMPORT PACKAGES ==============

import pandas as pd
import time
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model
from sklearn import metrics
import matplotlib.pyplot as plt
import os
import numpy as np
import warnings
warnings.filterwarnings("ignore")
from sklearn import preprocessing 


 #-------------------------- DATA SELECTION --------------------------------


dataframe=pd.read_csv("Dataset.csv")
    
print("--------------------------------")
print("Data Selection")
print("--------------------------------")
print()
print(dataframe.head(15))    

    
    

    
 #-------------------------- PRE PROCESSING --------------------------------
    
    #------ checking missing values --------
    
print("----------------------------------------------------")
print("              Handling Missing values               ")
print("----------------------------------------------------")
print()
print(dataframe.isnull().sum())

    
 

res = dataframe.isnull().sum().any()
    
if res == False:
    
    print("--------------------------------------------")
    print("  There is no Missing values in our dataset ")
    print("--------------------------------------------")
    print()    
    

    
else:

    print("--------------------------------------------")
    print(" Missing values is present in our dataset   ")
    print("--------------------------------------------")
    print()    
    

    
    dataframe = dataframe.fillna(0)
    
    resultt = dataframe.isnull().sum().any()
    
    if resultt == False:
        
        print("--------------------------------------------")
        print(" Data Cleaned !!!   ")
        print("--------------------------------------------")
        print()    
        print(dataframe.isnull().sum())



                
      # ---- LABEL ENCODING
            
print("--------------------------------")
print("Before Label Encoding")
print("--------------------------------")   

df_class=dataframe['gender']

print(dataframe['gender'].head(15))

    

    
    
    
print("--------------------------------")
print("After Label Encoding")
print("--------------------------------")            
        
label_encoder = preprocessing.LabelEncoder() 

dataframe['gender']=label_encoder.fit_transform(dataframe['gender'].astype(str))                  
dataframe['smoking_history']=label_encoder.fit_transform(dataframe['smoking_history'].astype(str))                  
   
print(dataframe['gender'].head(15))       
    

   
   
# ================== DATA SPLITTING  ====================
 
 
X=dataframe.drop('diabetes',axis=1)

y=dataframe['diabetes']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

print("---------------------------------------------")
print("             Data Splitting                  ")
print("---------------------------------------------")

print()

print("Total no of input data   :",dataframe.shape[0])
print("Total no of test data    :",X_test.shape[0])
print("Total no of train data   :",X_train.shape[0])
   
    

    
  #-------------------------- FEATURE EXTRACTION  --------------------------------
  
  
from sklearn.decomposition import PCA
#  PCA
pca = PCA(n_components=8) 
principal_components = pca.fit_transform(X_train)
  
  
print("---------------------------------------------")
print("   Feature Extraction ---> PCA               ")
print("---------------------------------------------")

print()

print(" Original Features     :",dataframe.shape[1])
print(" Reduced Features      :",principal_components.shape[1])


    
# Plot the results
plt.figure(figsize=(6, 6))
plt.scatter(principal_components[:, 0], principal_components[:, 1], c='blue', edgecolor='k', s=50)
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.title('PCA: First Two Principal Components')
plt.grid()
plt.savefig("pca.png")
plt.show()
  
    
   # ================== CLASSIFCATION  ====================
   
   # ------ RANDOM FOREST ------
   
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier()

rf.fit(X_train,y_train)

pred_rf = rf.predict(X_test)


from sklearn import metrics

acc_rf = metrics.accuracy_score(pred_rf,y_test) * 100

print("---------------------------------------------")
print("       Classification - Random Forest        ")
print("---------------------------------------------")

print()

print("1) Accuracy = ", acc_rf , '%')
print()
print("2) Classification Report")
print(metrics.classification_report(pred_rf,y_test))
print()
print("3) Error Rate = ", 100 - acc_rf, '%')


import pickle
with open('model.pickle', 'wb') as f:
      pickle.dump(rf, f)
    


import seaborn as sns
plt.figure(figsize = (6,6))
counts = y.value_counts()
plt.pie(counts, labels = counts.index, startangle = 90, counterclock = False, wedgeprops = {'width' : 0.6},autopct='%1.1f%%', pctdistance = 0.55, textprops = {'color': 'black', 'fontsize' : 15}, shadow = True,colors = sns.color_palette("Paired")[3:])
plt.text(x = -0.35, y = 0, s = 'Total Patients: {}'.format(dataframe.shape[0]))
plt.title('Disease Analysis', fontsize = 14);
plt.show()

plt.show()












