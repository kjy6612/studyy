import numpy as np
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential,Model
from tensorflow.keras.layers import Dense,Flatten,GlobalAveragePooling2D,Input
from tensorflow.keras.applications import VGG16,VGG19,DenseNet121,ResNet101
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import accuracy_score
# 1. 데이터

(x_train,y_train),(x_test,y_test) = cifar10.load_data()

x_train = x_train.astype('float32')/255.
x_test = x_test.astype('float32')/255.
y_train = to_categorical(y_train)
y_test = to_categorical(y_test)
print(x_train.shape,x_test.shape) # (50000, 32, 32, 3) (10000, 32, 32, 3)
print(y_train.shape,y_test.shape) # (50000, 1) (10000, 1)

# 2. 모델 
# 함수 모델 
input1 = Input(shape=(32, 32, 3))
vgg16 = VGG16(
    weights='imagenet',
    include_top = False, )(input1)
# gap = GlobalAveragePooling2D()(vgg16)
flatten = Flatten()(vgg16)
# output1 = Dense(10,activation='softmax')(gap)
output1 = Dense(10,activation='softmax')(flatten)
model = Model(inputs = input1, outputs = output1)

# 3. 컴파일, 훈련 
model.compile(loss='categorical_crossentropy',optimizer = 'adam')
model.fit(x_train,y_train,verbose=1,epochs=16, batch_size=64)

# 4. 평가 예측

result =model.evaluate(x_test,y_test) 
print('result : ',result )
y_predict=np.argmax(model.predict(x_test),axis=1)
y_test = np.argmax(y_test,axis=1)
acc = accuracy_score(y_test,y_predict)
print('acc : ',acc)
'''
result :  0.7713070511817932
313/313 [==============================] - 2s 6ms/step
acc :  0.8069
'''
