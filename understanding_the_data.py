import pandas as pd

df=pd.read_csv("Dataset1.csv")

print("Total no of elements : ", df.size)
print("No of rows and colmns : ", df.shape)

 
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())

train_table=df.groupby('Train_No').agg(
    Starting_Station=('Station_Name', 'first'),
    Ending_Station=('Station_Name', 'last')).reset_index(inplace=True)

print(train_table)

print(df['Distance'].describe())
print(df.groupby('Train_No')['Distance'].describe())

print(df['Station_Name'].describe())
print(df.groupby('Train_No')['Station_Name'].describe())

stops=df.groupby('Train_No').size()
print(stops)
print(stops.describe())

print("Missing values:", df.isnull().sum())
print("Duplicate values:", df.duplicated().sum())

print(df.groupby('Train_No')['SN'].min())
print(df.groupby('Train_No')['SN'].max())

valid_stat_codes=df['Station_Code'].unique()
print(valid_stat_codes)
print(df['Station_Code'].isin(valid_stat_codes).sum())

print((df[['1A','2A','3A','SL']] < 0).sum())

valid_stat_names=df['Station_Name'].unique()
print(valid_stat_names)
print(df['Station_Name'].isin(valid_stat_names).sum())

valid_routes=df['Route_Number'].unique()
print(valid_routes)

print(pd.to_datetime(df['Arrival_time'], format='%H:%M:%S',errors='coerce').isnull().sum())
print(pd.to_datetime(df['Departure_Time'], format='%H:%M:%S',errors='coerce').isnull().sum())

print(((df['Arrival_time']=='00:00:00') & (df['Departure_Time']=='00:00:00')).sum())