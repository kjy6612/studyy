import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, SimpleRNN,Dropout,LSTM, GRU


#1. 데이터
x=np.array([[1,2,3],[2,3,4],[3,4,5],[4,5,6]
           ,[5,6,7],[6,7,8],[7,8,9],[8,9,10],
           [9,10,11],[10,11,12],[20,30,40],[30,40,50],[40,50,60]])
y=np.array([4,5,6,7,8,9,10,11,12,13,50,60,70])
x_predict = np.array([50,60,70]) #아워너 80


#만들자 시작
print(x.shape,y.shape) #(13, 3) (13,)
# 리쉐이프
x=x.reshape(13,3,1)
print(x.shape,y.shape) #(13, 3,1) (13,)


#2. 모델 구성
model= Sequential()
#model.add(LSTM(200,input_length=3,input_dim=1))
#model.add(LSTM(20,activation='relu',input_shape=(3,1)))
model.add(LSTM(200,activation='relu',input_shape=(3,1),return_sequences=True)) #디폴트는 false인가봄
model.add(Dropout(0.5))
#ndim = 숫자, 숫자= 차원,LSTM 두 개 이상 사용할 때 이용 return_sequences=True
model.add(LSTM(16,return_sequences=True)) # (n,m.m)
model.add(LSTM(32,return_sequences=True))
model.add(LSTM(64,return_sequences=True))
model.add(LSTM(1280,return_sequences=True))
model.add(Dropout(0.5))
model.add(LSTM(256,return_sequences=True))
model.add(LSTM(512,return_sequences=True))
model.add(Dropout(0.2))
model.add(LSTM(256,return_sequences=True))
model.add(LSTM(128,return_sequences=True))
model.add(LSTM(64,return_sequences=True))
model.add(LSTM(32,return_sequences=True))
model.add(LSTM(16))
#model.add(Dense(10))
#model.add(GRU(10))
model.add(Dense(1))
#model.summary()
# return_sequences 성능이 나쁜 이유 : 시계열
# 2번 이상했을 때 잘 안나올 때가 많다.
# 시계열에 계산해서 다시 LSTM으로 잘 연산가능하면 좋고 안되면 별로임


#3. 컴파일 훈련
model.compile(loss='mse',optimizer='adam')
import time
start=time.time()
from tensorflow.python.keras.callbacks import EarlyStopping
es = EarlyStopping(monitor='loss',patience=200,mode='min',verbose=1,restore_best_weights=True)
model.fit(x,y,epochs=2000,batch_size=32,callbacks=[es])
end=time.time()


#4. 평가 예측
loss=model.evaluate(x,y)
x_predict = np.array([50,60,70]).reshape(1,3,1)
print(x_predict.shape)
print(x_predict)


result=model.predict(x_predict)
print('loss : ',loss)
print('[50,60,70]의 결과: ',result)
print('걸린 시간 : ',round(end-start,2))
'''
loss :  492.55078125
[50,60,70]의 결과:  [[20.304466]]
걸린 시간 :  234.84
'''