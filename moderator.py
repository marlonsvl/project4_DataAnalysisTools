# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 10:26:42 2015

@author: marlon
"""

import numpy
import pandas
import statsmodels.formula.api as smf 
import statsmodels.stats.multicomp as multi
import seaborn
import matplotlib.pyplot as plt


data = pandas.read_csv('/Users/utpl/Documents/DataAnalysisTools/nesarc_pds.csv', low_memory=False)


data['S2BQ3B'] = data['S2BQ3B'].replace('BL', numpy.nan)
data['S2BQ3B'] = data['S2BQ3B'].replace(' ', 0) 

data['S2BQ3B'] = pandas.to_numeric(data['S2BQ3B'])

sub1 = data[(data['S2BQ3B'] >= 20) & (data['S2BQ3B'] < 99)]

#NUMBER OF EPISODES OF ALCOHOL ABUSE and OCCUPATION: CURRENT OR MOST RECENT JOB
sub2 = sub1[['S2BQ3B', 'S1Q9B']].dropna()

model1 = smf.ols(formula='S2BQ3B ~ C(S1Q9B)', data=sub2).fit()
print (model1.summary())

sub3 = data[['S2BQ3B', 'S1Q9B']].dropna()

print ("means for S2BQ3B by S1Q9B A vs. B")
m1= sub1.groupby('S1Q9B').mean()
print (m1)


print ("standard deviation for mean S2BQ3B by S1Q9B A vs. B")
st1= sub3.groupby('S1Q9B').std()
print (st1)


# bivariate bar graph
seaborn.factorplot(x="S1Q9B", y="S2BQ3B", data=sub3, kind="bar", ci=None)
plt.xlabel('NUMBER OF EPISODES OF ALCOHOL ABUSE')
plt.ylabel('OCCUPATION: CURRENT OR MOST RECENT JOB')

# PRESENT SITUATION INCLUDES WORKING FULL TIME (35+ HOURS A WEEK)
# 1 = yes
# 2 = no
sub4=data[(data['S1Q7A1']==1)]
sub5=data[(data['S1Q7A1']==2)]

print ('association between NUMBER OF EPISODES OF ALCOHOL ABUSE and OCCUPATION: CURRENT OR MOST RECENT JOB for those working full time')
model2 = smf.ols(formula='S2BQ3B ~ C(S1Q9B)', data=sub4).fit()
print (model2.summary())

print ('association between NUMBER OF EPISODES OF ALCOHOL ABUSE and OCCUPATION: CURRENT OR MOST RECENT JOB for those working half time or less')
model3 = smf.ols(formula='S2BQ3B ~ C(S1Q9B)', data=sub5).fit()
print (model3.summary())

print ("means for NUMBER OF EPISODES OF ALCOHOL ABUSE and OCCUPATION: CURRENT OR MOST RECENT JOBt A vs. B  for those working full time")
m3= sub4.groupby('S1Q9B').mean()
print (m3)
print ("Means for NUMBER OF EPISODES OF ALCOHOL ABUSE and OCCUPATION: CURRENT OR MOST RECENT JOB A vs. B for those working half time or less")
m4 = sub3.groupby('S1Q9B').mean()
print (m4)