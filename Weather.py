# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# import weather data and pandas 
import pandas as pd

data = pd.read_csv(r"C:\Users\Welcome\Downloads\1. Weather Data.csv")
# Test some data structures
print(data.head(5))
print(data.index)
print(data.columns)
print(data.dtypes)
print(data['Rel Hum_%'].unique())
print(data.nunique)
print(data['Weather'].count())
print(data['Weather'].value_counts())
print(data.info())

#Find all the unique 'Wind Speed' values in the data.

TypeOfWindSpeed = data['Wind Speed_km/h'].nunique()
print('Types Of Wind Speed' +' are ' + str( TypeOfWindSpeed ))
WindSpeed = data['Wind Speed_km/h'].unique()
print('Wind Speed' +' are ' + str( WindSpeed ))

#Find the number of times when the 'Weather is exactly Clear'.

print(data.Weather.value_counts())
Clear_weather = data[data.Weather == 'Clear']
Clear_weather2 = data.groupby('Weather').get_group('Clear')  

#Find the number of times when the 'Wind Speed was exactly 4 km/h'.

FourKmPerHour = data.groupby('Wind Speed_km/h').get_group(4)

#Find out all the Null Values in the data.

NullData = data.sum().isnull()

# Rename the column name 'Weather' of the dataframe to 'Weather Condition'.

data.rename(columns = {'Weather' : 'Weather Condition', 'Temp_C': 'Temp'})


#What is the mean of 'Visibility' ?

data.Visibility_km.mean()

#What is the Standard Deviation of 'Pressure'  in this data?

data.Press_kPa.std()

#What is the Variance of 'Relative Humidity' in this data ?

data['Rel Hum_%'].var()

#Find all instances when 'Snow' was recorded.
data.groupby(['Weather Condition']).get_group('Snow') 

# 2nd Way 
data[data['Weather Condition'] == 'Snow']

# whatever contains Snow
data[data['Weather Condition'].str.contains('Snow')]

#Find all instances when 'Wind Speed is above 24' and 'Visibility is 25'.

data[(data['Wind Speed_km/h']) > 24 & (data['Visibility_km'] == 25)]

#What is the Mean value of each column against each 'Weather Condition ?

data.groupby(data['Weather Condition']).mean()

#What is the Minimum & Maximum value of each column against each 'Weather Condition ?

data.groupby('Weather Condition').min()
data.groupby('Weather Condition').max()

#Show all the Records where Weather Condition is Fog.

data[data['Weather Condition'] == 'Fog']
data[data['Weather Condition'].str.contains('Fog')]

#Find all instances when 'Weather is Clear' or 'Visibility is above 40'.
data[(data['Weather Condition'] == 'Clear') | (data['Visibility_km'] > 40)]

"""
Find all instances when :
A. 'Weather is Clear' and 'Relative Humidity is greater than 50'
or
B. 'Visibility is above 40'
"""
data[(data['Weather Condition'] == 'Clear') & (data['Rel Hum_%'] > 50) | (data['Visibility_km'] > 40) ]
