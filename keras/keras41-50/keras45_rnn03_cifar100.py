
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense, Conv2D, Flatten ,LSTM
import numpy as np
from sklearn.metrics import r2_score, accuracy_score
from sklearn.preprocessing  import MinMaxScaler
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.datasets import cifar100
from sklearn.preprocessing import MinMaxScaler, StandardScaler #전처리
from sklearn.preprocessing import MaxAbsScaler, RobustScaler #전처리


# 1. 데이터


(x_train,y_train),(x_test,y_test) = cifar100.load_data() # 데이터를 넣어줌
print("x_train.shape : ",x_train.shape)
print("x_test.shape : ",x_test.shape)
print("y_train.shape : ",y_train.shape)
# x_train.shape :  (50000, 32, 32, 3)
# x_test.shape :  (50000, 1)
# y_train.shape :  (50000, 1)
x_train = x_train.reshape(50000,32,96)
x_test = x_test.reshape(10000,32,96)
print("x_train.shape : ",x_train.shape)
print("x_test.shape : " ,x_test.shape)
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
print("y_train.shape : ",y_train.shape) # y_train.shape :  (50000, 100)
print("y_test.shape : ",y_test.shape) # y_test.shape :  (10000, 100)




# 2. 모델 구성


model = Sequential()
#model.add(Dense(10,input_shape=(3,)))
model.add(LSTM(32, input_shape=(32,96)))
model.add(Dense(32, activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(100, activation='softmax'))



#3.컴파일,훈련


model.compile(loss='categorical_crossentropy',optimizer='adam')
from tensorflow.python.keras.callbacks import EarlyStopping
es = EarlyStopping(monitor='loss',patience=30,mode='min',
               verbose=1,restore_best_weights=True)
model.fit(x_train,y_train,epochs= 16,batch_size=25000,
                validation_split=0.2,verbose=1,callbacks=[es])




# 4. 평가, 예측


result =model.evaluate(x_test,y_test)
print('result : ',result )
y_predict=np.round(model.predict(x_test))
acc = accuracy_score(y_test,y_predict)
print('acc : ',acc)


import matplotlib.pyplot as plt
plt.imshow(x_train[3333],'gray') # 그림 보여줌
plt.show()

