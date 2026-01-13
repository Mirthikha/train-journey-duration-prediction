from visuals_and_feat_analys import fin_table
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import matplotlib.pyplot as plt

X1=fin_table[['Distance']]
Y1=fin_table['Journey_duration']

X1_test, X1_train, Y1_test, Y1_train=train_test_split(X1, Y1, test_size=0.2, random_state=42)

model=LinearRegression()
model.fit(X1_train, Y1_train) 

Y1_predict=model.predict(X1_test)

mae=mean_absolute_error(Y1_test,Y1_predict)
mse=mean_squared_error(Y1_test,Y1_predict)
rmse=np.sqrt(mse)
r2=r2_score(Y1_test,Y1_predict)

print("MAE:", mae, "seconds")
print("MSE", mse)
print("RMSE:", rmse, "seconds")
print("R² score:", r2)

plt.scatter(Y1_test,Y1_predict,color='yellow')
plt.plot([Y1_test.min(),Y1_test.max()],[Y1_test.min(),Y1_test.max()],color='red')
plt.title("1 Input feature - Distance")
plt.xlabel("Y1 test")
plt.ylabel("Y1 predicted")
plt.show()



X2=fin_table[['Total_Stops']]
Y2=fin_table['Journey_duration']

X2_test, X2_train, Y2_test, Y2_train=train_test_split(X2, Y2, test_size=0.2, random_state=42)

model=LinearRegression()
model.fit(X2_train, Y2_train) 

Y2_predict=model.predict(X2_test)

mae=mean_absolute_error(Y2_test,Y2_predict)
mse=mean_squared_error(Y2_test,Y2_predict)
rmse=np.sqrt(mse)
r2=r2_score(Y2_test,Y2_predict)

print("MAE:", mae, "seconds")
print("MSE", mse)
print("RMSE:", rmse, "seconds")
print("R² score:", r2)

plt.scatter(Y2_test,Y2_predict,color='yellow')
plt.plot([Y2_test.min(),Y2_test.max()],[Y2_test.min(),Y2_test.max()],color='red')
plt.title("1 Input feature - Total Stops")
plt.xlabel("Y2 test")
plt.ylabel("Y2 predicted")
plt.show()



X3=fin_table[['Distance','Total_Stops']]
Y3=fin_table['Journey_duration']

X3_test, X3_train, Y3_test, Y3_train=train_test_split(X3, Y3, test_size=0.2, random_state=42)

model=LinearRegression()
model.fit(X3_train, Y3_train) 

Y3_predict=model.predict(X3_test)

mae=mean_absolute_error(Y3_test,Y3_predict)
mse=mean_squared_error(Y3_test,Y3_predict)
rmse=np.sqrt(mse)
r2=r2_score(Y3_test,Y3_predict)

print("MAE:", mae, "seconds")
print("MSE", mse)
print("RMSE:", rmse, "seconds")
print("R² score:", r2)


plt.scatter(Y3_test,Y3_predict,color='yellow')
plt.plot([Y3_test.min(),Y3_test.max()],[Y3_test.min(),Y3_test.max()],color='red')
plt.title("2 Input feature - Distance, Total Stops")
plt.xlabel("Y3 test")
plt.ylabel("Y3 predicted")
plt.show()

