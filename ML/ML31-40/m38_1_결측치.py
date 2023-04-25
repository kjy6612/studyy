# 보간 
# 결측치 처리하는 것
'''
결측치 처리 방법 들 
1. 삭제(행,열)
결측치 잘 못 처리하면 오염될 수 있어서 의외로 삭제가 편할 수도 있다.
2. 특정 값 ex) 0
    1) 평균 값 mean
        중간에 빠진게 꽤많다면 
        평균의 오류가 있을 수 있다.
    2) 중위값 median
    3) 0 : fillna
    4) 앞의 값 : ffill(frontfill) - 시계열 
    5) 뒤의 값 : bfiil(backfill) 뒷값 
    6) 특정 값 :
    7) 기타등등 
3. 보간 : interpolate
두 개의 포인트가 있음 
선형보간 - 선을 하나 그어서 빈 지점을 선 어디에 해당되어있다고 보는 것
4. 모델 : predict
결측치 부분을 y로 만들고 프레딕드해서 채운다. 
5. 트리/ 부스팅 계열 : 통상 결측ㅊ, 이상치에 대해서 자유롭다.
있어도 모델이 훈련이 된다. 
가능한 이유 : 좌표계 안에서 선을 그면서 분류 하기 때문에 이상치나 결측치가 걸러진다. 
결정 트리 : 스무고개 형식으로 너는 어떠냐고 계속 물어봐서 분류 
'''
