import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression, Perceptron

# 데이터 불러오기
digits = datasets.load_digits()
X, y = digits.data, digits.target

# 모델들 정의
classifiers = [
    ("Perceptron", Perceptron()),
    ("Logistic Regression", LogisticRegression(tol=1e-1, C=1e4 / X.shape[0]))
]

# 훈련 비율 (heldout)
heldout = [0.95, 0.90, 0.75, 0.50, 0.01]
xx = 1.0 - np.array(heldout)  # 훈련 데이터 비율

# 테스트를 위한 반복 횟수
rounds = 20

# 그래프 그리기
for name, clf in classifiers:
    print(f"Training {name}")
    
    yy = []
    
    for i in heldout:
        yy_ = []
        
        for r in range(rounds):
            # 데이터셋 분할
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=i, random_state=r)
            
            # 모델 학습
            clf.fit(X_train, y_train)
            
            # 예측 및 오류율 계산
            y_pred = clf.predict(X_test)
            error_rate = 1 - np.mean(y_pred == y_test)
            yy_.append(error_rate)
        
        # 평균 오류율을 yy에 추가
        yy.append(np.mean(yy_))
    
    # 결과를 그래프에 추가
    plt.plot(xx, yy, label=name)

# 그래프 꾸미기
plt.legend(loc="upper right")
plt.xlabel("Proportion Train")
plt.ylabel("Test Error Rate")
plt.show()
