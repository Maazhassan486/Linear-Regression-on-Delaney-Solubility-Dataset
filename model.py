import pandas as pd

df=pd.read_csv(r'C:\Users\maazg\Downloads\delaney_solubility_with_descriptors.csv');
# print(df.head(10));
y=df['logS'];
# print(y.head(5));
x=df.drop('logS',axis=1);
# print(x);

from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2,random_state=100);
# print(xtrain);
# print(xtest)
# print(ytrain)
# print(ytest)

from sklearn.linear_model import LinearRegression
lr=LinearRegression();
lr.fit(xtrain,ytrain);
y_lr_train_pred=lr.predict(xtrain);
y_lr_test_pred=lr.predict(xtest);

# print(y_lr_train_pred);

from sklearn.metrics import mean_squared_error,r2_score
mse_train=mean_squared_error(ytrain,y_lr_train_pred)
r2_train=r2_score(ytrain,y_lr_train_pred)
mse_test=mean_squared_error(ytest,y_lr_test_pred)
r2_test=r2_score(ytest,y_lr_test_pred)

lr_results=pd.DataFrame(["Linear Regression",mse_train,r2_train,mse_test,r2_test]).transpose();
print(lr_results)
lr_results.columns=["method","mse_train","r2_train","mse_test","r2_test"]
print(lr_results)

import matplotlib.pyplot as plt
plt.scatter(x=ytrain,y=y_lr_train_pred,alpha=0.3);
plt.xlabel="predictlogS";
plt.ylabel="experiment_logS_train";
plt.plot();
plt.show();