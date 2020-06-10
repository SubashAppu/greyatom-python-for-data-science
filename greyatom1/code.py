# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')

#Reading file
bank_data = pd.read_csv(path)
#Code starts here
categorical_var=bank_data.select_dtypes(include='object')
print(categorical_var)

numerical_var=bank_data.select_dtypes(include='number')
print(numerical_var)

banks=bank_data

banks.drop(['Loan_ID'],axis=1,inplace=True)

print(banks.isnull().sum())

bank_mode=banks.mode()


banks['Gender'].fillna(bank_mode['Gender'].mode()[0],inplace=True)
banks['Married'].fillna(bank_mode['Married'].mode()[0],inplace=True)
banks['Dependents'].fillna(bank_mode['Dependents'].mode()[0],inplace=True)
banks['Education'].fillna(bank_mode['Education'].mode()[0],inplace=True)
banks['Self_Employed'].fillna(bank_mode['Self_Employed'].mode()[0],inplace=True)
banks['ApplicantIncome'].fillna(bank_mode['ApplicantIncome'].mode()[0],inplace=True)
banks['CoapplicantIncome'].fillna(bank_mode['CoapplicantIncome'].mode()[0],inplace=True)
banks['LoanAmount'].fillna(bank_mode['LoanAmount'].mode()[0],inplace=True)
banks['Loan_Amount_Term'].fillna(bank_mode['Loan_Amount_Term'].mode()[0],inplace=True)
banks['Credit_History'].fillna(bank_mode['Credit_History'].mode()[0],inplace=True)
banks['Property_Area'].fillna(bank_mode['Property_Area'].mode()[0],inplace=True)
banks['Loan_Status'].fillna(bank_mode['Loan_Status'].mode()[0],inplace=True)

avg_loan_amount=pd.pivot_table(banks,index=['Gender','Married','Self_Employed'],values='LoanAmount')

loan_approved_se=0
loan_approved_nse=0

for i in banks.index:
    if(banks['Self_Employed'][i]=='Yes' and banks['Loan_Status'][i]=='Y'):
        loan_approved_se+=1
    if(banks['Self_Employed'][i]=='No' and banks['Loan_Status'][i]=='Y'):
        loan_approved_nse+=1

Loan_Status=614     #Given 
percentage_se=(loan_approved_se/Loan_Status)*100
percentage_nse=(loan_approved_nse/Loan_Status)*100

loan_term=banks['Loan_Amount_Term'].apply(lambda x:x/12)
big_loan_term=0
for i in loan_term:
    if i>=25:
        big_loan_term+=1

loan_groupby=banks.groupby('Loan_Status')

loan_groupby=loan_groupby[['ApplicantIncome','Credit_History']]

mean_values=loan_groupby.mean()


