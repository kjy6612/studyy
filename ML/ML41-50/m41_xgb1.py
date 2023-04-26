    # "n_estimators" : [100,200,300,400,500,600], # 디폴트 100 / 1 ~ inf / 정수
    # "learning_rate" : [0.1,0.2,0.3,0.5,1,0.01,0.001], # 디폴트 0.3 / 0 ~ 1 / eta
    # "max_depth" : [None,2,3,4,5,6,7,8,9,10], # 디폴트 6 / 0 ~ inf / 정수
    # "gamma" : [0,1,2,3,4,5,7,8,9,10], # 디폴트 0 / 0 ~ inf 
    # "min_child_weight" : [0,0.1,0.01,0.001,0.5,1,5,10,100], # 디폴트 1 / 0 ~ inf 
    # "subsample" : [0,0.1,0.2,0.3,0.5,0.7,1], # 디폴트 1 / 0 ~ 1 
    # "colsample_bytree" : [0,0.1,0.2,0.3,0.5,0.7,1], # 디폴트 / 0 ~ 1 
    # "colsample_bylevel":[0,0.1,0.2,0.3,0.5,0.7,1], # 디폴트 / 0 ~ 1 
    # "colsample_bynode":[0,0.1,0.2,0.3,0.5,0.7,1], # 디폴트 / 0 ~ 1 
    # "reg_alpha":[0,0.1,0.01,0.001,1,2,10], # 디폴트 0 / 0 ~ inf / L1 절대값 가중치 규제 / alpha
    # "reg_lambda":[0,0.1,0.01,0.001,1,2,10], # 디폴트 1 / 0 ~ inf / L2 제곱 가중치 규제 / lambda
import numpy as np
import pandas as pd
from xgboost import XGBClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold, StratifiedKFold, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler,MinMaxScaler,MaxAbsScaler,RobustScaler

# 1.데이터 
x,y = load_breast_cancer(return_X_y=True)

x_train, x_test, y_train,y_test = train_test_split(
    x,y, random_state=337,train_size=0.8,stratify=y
)


x_train= RobustScaler().fit_transform(x_train)
x_test= RobustScaler().fit_transform(x_test)

n_split = 5
kfold = StratifiedKFold(n_splits=n_split)
parameter =  {
    "n_estimators" : [100], # 디폴트 100 / 1 ~ inf / 정수
    "learning_rate" : [0.3], # 디폴트 0.3 / 0 ~ 1 / eta
    "max_depth" : [2], # 디폴트 6 / 0 ~ inf / 정수
    "gamma" : [0], # 디폴트 0 / 0 ~ inf 
    "min_child_weight" : [1], # 디폴트 1 / 0 ~ inf 
    "subsample" : [0.3], # 디폴트 1 / 0 ~ 1 
    "colsample_bytree" : [1], # 디폴트 / 0 ~ 1 
    "colsample_bylevel":[1], # 디폴트 / 0 ~ 1 
    "colsample_bynode":[1], # 디폴트 / 0 ~ 1 
    "reg_alpha":[0], # 디폴트 0 / 0 ~ inf / L1 절대값 가중치 규제 / alpha
    "reg_lambda":[1], # 디폴트 1 / 0 ~ inf / L2 제곱 가중치 규제 / lambda
},
# 나머지 디폴트로 하고 한가지 파라미터만 여러가지 값으로 돌릴 때, 가장 좋았던 파라미터 값과
# 한꺼번에 사용 파라미터들을 돌려서 나오는 최상의 파라미터 값과 다를 가능성이 있다. 
# 효율 때문에 
# inf : 무한 
    
    
 


#2. 모델 
xgb = XGBClassifier(random_state=1234)
model = XGBClassifier(random_state=1234)
#model = GridSearchCV(xgb,parameter,cv=kfold,n_jobs=-1)

# 3. 훈련
model.fit(x_train,y_train)

# 4. 평가, 예측 
print("최상의 매개변수 : ",model.best_params_)
print("최상의 매개변수 : ",model.best_score_)
result = model.score(x_test,y_test)
print("최종점수 : ", result)

'''
파라미터 안 사용 
최종점수 :  0.8947368421052632


파라미터 사용 
최상의 매개변수 :  {'colsample_bylevel': 1, 'colsample_bynode': 
1, 'colsample_bytree': 1, 'gamma': 0, 'learning_rate': 0.3, 'max_depth': 2, 'min_child_weight': 1, 'n_estimators': 100, 'reg_alpha': 0, 'reg_lambda': 1, 'subsample': 0.3}
최상의 매개변수 :  0.9758241758241759
최종점수 :  0.9035087719298246

'''
