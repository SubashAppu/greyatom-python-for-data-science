# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here
loan_status=data['Loan_Status'].value_counts()
loan_status.plot()

property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar',stacked=False)

plt.xlabel('Property Area')
plt.ylabel('Loan Status')

plt.xticks(rotation=45)

education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar',stacked=True)

plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)

graduate=data[data['Education']=='Graduate']
not_graduate=data[data['Education']=='Not Graduate']

graduate['LoanAmount'].plot(kind='density',label='Graduate')

not_graduate['LoanAmount'].plot(kind='density',label='Not Graduate')

fig ,(ax_1,ax_2,ax_3)=plt.subplots(nrows=3,ncols=1)

plt.scatter(x=data['ApplicantIncome'],y=data['LoanAmount'])
ax_1.set_title('Applicant Income')

plt.scatter(x=data['CoapplicantIncome'],y=data['LoanAmount'])
ax_2.set_title('Coapplicant Income')

data['TotalIncome']=data['ApplicantIncome']+data['CoapplicantIncome']

plt.scatter(x=data['TotalIncome'],y=data['LoanAmount'])
ax_3.set_title('Total Income')


# Step 1 
#Reading the file


#Creating a new variable to store the value counts


#Plotting bar plot



# Step 2
#Plotting an unstacked bar plot




#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 3
#Plotting a stacked bar plot




#Changing the x-axis label


#Changing the y-axis label


#Rotating the ticks of X-axis


# Step 4 
#Subsetting the dataframe based on 'Education' column


#Subsetting the dataframe based on 'Education' column


#Plotting density plot for 'Graduate'


#Plotting density plot for 'Graduate'


#For automatic legend display


# Step 5
#Setting up the subplots


#Plotting scatter plot


#Setting the subplot axis title


#Plotting scatter plot


#Setting the subplot axis title


#Creating a new column 'TotalIncome'


#Plotting scatter plot



#Setting the subplot axis title



