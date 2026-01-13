from visuals_and_feat_analys import fin_table
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

X=fin_table[['Distance','Total_Stops']]
Y=fin_table['Journey_duration']

X_test, X_train, Y_test, Y_train=train_test_split(X, Y, test_size=0.2, random_state=42)

model=LinearRegression()
model.fit(X_train, Y_train) 

Y_predict=model.predict(X_test)

mae=mean_absolute_error(Y_test,Y_predict)
mse=mean_squared_error(Y_test,Y_predict)
rmse=np.sqrt(mse)
r2=r2_score(Y_test,Y_predict)

print("MAE:", mae, "seconds")
print("MSE", mse)
print("RMSE:", rmse, "seconds")
print("R² score:", r2)

sns.scatterplot(x=Y_test, y=Y_predict, color='#f72585')
sns.lineplot(x=[Y_test.min(), Y_test.max()],y=[Y_test.min(), Y_test.max()],color="#9b10e6", linewidth=3)
plt.xlabel("Actual Duration")
plt.ylabel("Predicted Duration")
plt.title("Actual vs Predicted Journey Duration")
plt.show()
