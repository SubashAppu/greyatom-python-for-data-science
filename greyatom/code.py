# --------------
# Importing header files
import numpy as np
import pandas as pd
from statistics import mean
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
census=np.concatenate((data,new_record))
print(data)
print(census)
#Code starts here

age=np.array(census[:,0],dtype=np.int)
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std=np.std(age)


race=np.array(census[:,2],dtype=np.int)

race_0=[]
race_1=[]
race_2=[]
race_3=[]
race_4=[]

for elmt in race:
    if elmt==0:
        race_0.append(0)
    elif elmt==1:
        race_1.append(1)
    elif elmt==2:
        race_2.append(2)
    elif elmt==3:
        race_3.append(3)
    elif elmt==4:
        race_4.append(4)

len_0=len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)

length=[len_0,len_1,len_2,len_3,len_4]
minority_val=min(length)

if minority_val==len_0:
    minority_race=0
elif minority_val==len_1:
    minority_race=1
elif minority_val==len_2:
    minority_race=2
elif minority_val==len_3:
    minority_race=3
elif minority_val==len_4:
    minority_race=4

print(minority_race)

seniors=np.asarray(age)
senior_citizens=[]
for elmt in seniors:
    if elmt>60:
        senior_citizens.append(60)

senior_citizens_len=len(senior_citizens)

age_nd_hour=np.array(census[:,(0,6)],dtype=np.int)
working_hours_sum=0
for elmt in range(0,1001):
    if age_nd_hour[elmt,0]>60:
        working_hours_sum+=age_nd_hour[elmt,1]

print(working_hours_sum)

avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)

edu_nd_inc=np.array(census[:,(1,7)],dtype=np.int)
high,low=[],[]
for elmt in range(0,1001):
    if edu_nd_inc[elmt,0]>10:
        high.append(edu_nd_inc[elmt,1])
    elif edu_nd_inc[elmt,0]<=10:
        low.append(edu_nd_inc[elmt,1])

tot_hi,tot_lo=0,0
for elmt in high:
    tot_hi+=elmt
for elmt in low:
    tot_lo+=elmt

avg_pay_high=tot_hi/len(high)
avg_pay_low=tot_lo/len(low)

print(avg_pay_high,avg_pay_low)


