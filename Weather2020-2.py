#!/usr/bin/env python
# coding: utf-8

# In[83]:


"""import statements"""
#Santhosh Subasinghe HW1 
import pandas as pd
from pathlib import Path 
from sklearn import tree, linear_model
import sklearn.metrics
import datetime as datetime
from datetime import date, timedelta
import matplotlib.pyplot as plt




class weather_wrapper:
   """read method"""
   def read(infile):
       data = pd.read_csv(Path(infile))
       return data
  

   def daily_summary(self, userVar, startingdate):
       ddates = pd.DataFrame()
       dddates = pd.DataFrame()
       df = pd.read_csv('2020-2.csv')
       df['local_eastern_time'] = pd.to_datetime(df['local_eastern_time']).dt.date
       day = pd.to_datetime(startingdate).date()
       endDate = day + pd.Timedelta(days = 7 )
       daylists = df['local_eastern_time']
       bool_value = (day <= daylists) & (endDate >= daylists)
       ddates = df[bool_value]
       dddates['StationID'] = ddates['StationID']
       dddates['day'] = ddates['local_eastern_time']
       dddates[userVar] = ddates[userVar]
       desired = dddates.groupby(['StationID', 'day'])
       #wanted to print it out for yall and return it
       print(desired.agg(['min', 'mean', 'max']))
       return(desired.agg(['min', 'mean', 'max']))
   
   def plot(self,stationID, userVar, startingdatee):
       df = pd.read_csv('2020-2.csv')
       day = pd.to_datetime(startingdatee).date()
       df_final = df
       dfstat =  df[df['StationID'] == stationID]
       df_final[userVar] = dfstat[userVar]
       df_final['timestamp']= pd.to_datetime(dfstat['local_eastern_time'])
       df_final['hours'] = df_final['timestamp'].dt.hour
       df_final['days'] = df_final['timestamp'].dt.date
       plotvalues = pd.DataFrame()
       startdatee = day
       enddate = day + pd.Timedelta(days = 2 )
       ender = enddate + pd.Timedelta(days = 1 )
       day_lists = df_final['days']
       bool_value = (day_lists >= startdatee) & (day_lists <= enddate)
       plotvalues = df_final[bool_value]       
       plt.title("Station " + str(stationID) + ", "+  userVar+ "\n (" + str(startdatee) + " 00:00:00" + " to " + str(ender) + " 00:00:00)" )
       plt.plot(plotvalues['timestamp'],plotvalues[userVar])
       plt.ylabel('Observation')
       plt.xlabel('Hour')       
       temp = plotvalues['timestamp']
       ticks = temp.iloc[0::24]       
       plt.xticks(ticks, ticks.dt.hour )
       plt.show()
       
       
       
      


# In[84]:


wrapper = weather_wrapper()
df = wrapper.daily_summary("temp_air_2m_C", "2020-06-06 12:59:59")
wrapper.plot(410, "temp_air_2m_C", "2020-06-06 12:59:59")
df.head()

