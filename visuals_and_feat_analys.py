from data_clean_feat_creat import journey_det, input_features, input_features1
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from understanding_the_data import df

journey_det = journey_det.reset_index(drop=True)
input_features = input_features.reset_index(drop=True)
input_features1 = input_features1.reset_index(drop=True)

fin_table=pd.concat([journey_det, input_features, input_features1],axis=1)

fin_table=fin_table[~((fin_table['start']==0) & (fin_table['end']==0))]
fin_table.reset_index(inplace=True)

fin_table.drop(columns=['index','start','end'],inplace=True)

fin_table.rename(columns={'SN': 'Total_Stops'}, inplace=True)
print(fin_table)

fin_table=fin_table[~(fin_table['Journey_duration']>15000)]
fin_table=fin_table[~(fin_table['Distance']>1350)]

plt.boxplot([fin_table['Distance'],fin_table['Total_Stops'], fin_table['Journey_duration']])
plt.xticks([1, 2, 3], ['Distance', 'Total_Stops', 'Journey Duration'])
plt.title("Boxplot of Distance, Total stops and Journey Duration")
plt.show()

sns.set_theme(style="whitegrid")

sns.scatterplot(x='Distance',y='Journey_duration',color="teal",data=fin_table)
plt.title("Scatter plot - Distance vs JourneY Duration")
plt.xlabel("Distance")
plt.ylabel("Journey duration")
plt.show()

sns.scatterplot(x='Total_Stops',y='Journey_duration',data=fin_table,color="seagreen")
plt.title("Scatter plot - Distance vs JourneY Duration")
plt.xlabel("Total stops")
plt.ylabel("Journey duration")
plt.show()

corr = fin_table[['Distance','Total_Stops','Journey_duration']].corr()
sns.heatmap(corr, annot=True, cmap='Greys')
plt.title('Correlation Heatmap')
plt.show()

pivot=df.pivot_table(index='Train_No',values='SN',aggfunc='count')
print(pivot)