import pandas as pd
from understanding_the_data import df

df=df[~((df['Arrival_time']=='00:00:00') & (df['Departure_Time']=='00:00:00'))]
print(df.shape)

df['Arrival_time']=pd.to_datetime(df['Arrival_time'], format='%H:%M:%S',errors='coerce')
df['Departure_Time']=pd.to_datetime(df['Departure_Time'], format='%H:%M:%S',errors='coerce')

df['Arrival_seconds']=(df['Arrival_time'].dt.hour *3600 + df['Arrival_time'].dt.minute *60 + df['Arrival_time'].dt.second)
print(df['Arrival_seconds'])

df['Departure_seconds']=(df['Departure_Time'].dt.hour *3600 + df['Departure_Time'].dt.minute *60 + df['Departure_Time'].dt.second)
print(df['Departure_seconds'])

journey_det=df.groupby('Train_No').agg(start=('Arrival_seconds','first'), end=('Departure_seconds','last'))
print(journey_det)

journey_det['Journey_duration']=journey_det['end']-journey_det['start']

journey_det.loc[journey_det['Journey_duration']<0,'Journey_duration']+=24*3600
print(journey_det)

input_features=df.groupby('Train_No')['Distance'].sum()
input_features.reset_index()
print(input_features)

input_features1=df.groupby('Train_No')['SN'].max()
input_features1.reset_index()
print(input_features1)