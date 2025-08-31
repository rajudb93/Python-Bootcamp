import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load data
data = pd.read_csv('employee_data.csv')

X=data[['YearsExperience']]
Y=data['Salary']

model=LinearRegression()
model.fit(X,Y)

data['PredictedSalary']=model.predict(X)
print("Model Coefficient:", round(model.coef_[0],2))
print("Model Intercept:", round(model.intercept_,2))

plt.scatter(X,Y,color='blue',label='Actual Salary')
plt.plot(X,data['PredictedSalary'],color='red',label='Predicted Salary')

plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary vs Years of Experience')
plt.legend()
plt.show()





