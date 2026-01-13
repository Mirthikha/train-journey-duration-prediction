from sklearn.linear_model import LinearRegression
from visuals_and_feat_analys import fin_table

def train_model():
    X=fin_table[['Distance','Total_Stops']]
    Y=fin_table['Journey_duration']

    model=LinearRegression()
    model.fit(X,Y)

    return model

print(fin_table)
print("Distance range:", fin_table['Distance'].min(), fin_table['Distance'].max())
print("Stops range:", fin_table['Total_Stops'].min(), fin_table['Total_Stops'].max())
print("Unique stops:", fin_table['Total_Stops'].unique())
