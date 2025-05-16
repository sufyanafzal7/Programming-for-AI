import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:,:-1].values
Y = dataset.iloc[:,-1].values


from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X,Y,test_size=1/3, random_state=0)

print(X_train)
print(" "*20)
print(Y_train)
print(" "*20)
print(X_test)
print(" "*20)
print(Y_test)
print(" "*20)


from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train,Y_train)
print(X_train)
print(" "*20)
print(Y_train)
print(" "*20)
print(X_test)
print(" "*20)
print(Y_test)
print(" "*20)


Y_pred = regressor.predict(X_test)


plt.scatter(X_train,Y_train,color='r')
plt.plot(X_train,regressor.predict(X_train), color = 'b')
plt.title('Salary vs Training Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(X_test,Y_test, color = 'red')
plt.plot(X_train,regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Training Experience(Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(X_test,Y_test,color='red')
plt.plot(X_test,Y_pred, color = 'blue')
plt.title('Salary vs Experience (Training Set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
