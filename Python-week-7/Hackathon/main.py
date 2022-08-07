# Program to predict the closing stock price using a databse with 60 days base

#libraries

from calendar import day_abbr
import math
import pandas_datareader as web
import numpy as np
import pandas as pd
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# stock quote

df = web.DataReader('AAPL', data_source='yahoo', start='2012-01-01', end='2019-12-17')


# shape of the dataset

print(df.shape)

#visualisation of the data (closing price of the stock)

plt.figure(figsize=(16,8))
plt.title('Close Price')
plt.plot(df['Close'])
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.show()

#creation of dataframe with close column of df and conversion np

data = df.filter(['Close'])
dataset = data.values
training_data_len = math.ceil(len(dataset) * 0.8)

#scale the data

scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(dataset)

#create the training dataset

train_data = scaled_data[0: training_data_len, ]

#split into x_train and y_train

x_train = []
y_train = []

for i in range (60, len(train_data)):
    x_train.append(train_data[i-60:i, 0])
    y_train.append(train_data[i, 0])
    if i<= 60:
        print(x_train)
        print(y_train)
        print()

#convert x_train and y_train to np

x_train, y_train = np.array(x_train), np.array(y_train)

#reshape the data because it expects 3 dimensions

x_train= np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

#build the model based on lstm

model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape = (x_train.shape[1], 1)))
model.add(LSTM(50, return_sequences=False))
model.add(Dense(25))
model.add(Dense(1))

#Compliation

model.compile(optimizer='adam', loss='mean_squared_error')

#Trainin of the model

model.fit(x_train, y_train, batch_size=1, epochs=1)
#needs to run this and then continue coding 


#//////////////////////////////////////////////////////


#create the testing dataset

test_data = scaled_data[training_data_len - 60: , :]
x_test = []
y_test = dataset[training_data_len:, :]
for i in range(60, len(test_data)):
    x_test.append(test_data[i-60:i, 0])

#convert the data to a numpy array to use in the model

x_test = np.array(x_test)

#reshaping the data to 3 dimensions

x_test= np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))

#predicted price values

predictions = model.predict(x_test)
predictions = scaler.inverse_transform(predictions)

#get the root mean squared error (measure of accuracy)

rmse = np.sqrt(np.mean( predictions - y_test )**2)

#plot the data

train = data[:training_data_len]
valid = data[training_data_len:]
valid['Predictions'] = predictions
plt.figure(figsize=(16,8))
plt.title('Model')
plt.xlabel('Date', fontsize=18)
plt.ylabel('Close Price USD ($)', fontsize=18)
plt.plot(train['Close'])
plt.plot(valid[['Close', 'Predictions']])
plt.legend(['Train', 'Val', 'Predictions'], loc='lower right')
plt.show()

# the valid and predicted values

print(valid)

#get the quote

apple_quote = web.DataReader('AAPL', data_source = 'yahoo', start = '2012-01-01', end='2019-12-17')
new_df = apple_quote(['Close'])
last_60_days = new_df[-60:].values
last_60_days_scaled = scaler.transform(last_60_days)
X_test = []
X_test.append(last_60_days_scaled)
X_test = np.array(X_test)
X_test = np.reshape(X_test, (X_test.shape[0], X_test.shape[1], 1))
pred_price = model.predict(X_test)
pred_price = scaler.inverse_transform(pred_price)
print(pred_price)

apple_quote1 = web.DataReader('AAPL', data_source = 'yahoo', start = '2019-12-18', end='2019-12-18')
print(apple_quote1['Close'])

#comparison