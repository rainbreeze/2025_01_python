import numpy as np

class Perceptron:
    def __init__(self, input_length, weights=None):
        if weights is None:
            self.weights = np.ones(input_length) * 0.5  # 기본 가중치 초기화
        else:
            self.weights = weights

    def unit_step_function(self, x):
        """단위 계단 함수 (0.5 기준으로 분류)"""
        if x > 0.5:
            return 1
        return 0

    def __call__(self, in_data):
        """퍼셉트론 예측 함수"""
        weighted_input = self.weights * in_data  # 입력값과 가중치의 곱
        weighted_sum = weighted_input.sum()     # 가중합
        return self.unit_step_function(weighted_sum)

    def train(self, X_train, y_train, learning_rate=0.1, epochs=10):
        """퍼셉트론 학습 함수"""
        for epoch in range(epochs):  # 여러 epoch에 걸쳐 반복
            for x, y in zip(X_train, y_train):
                y_pred = self(x)  # 예측값
                if y_pred != y:  # 예측이 잘못되었을 때
                    self.weights = self.weights + learning_rate * (y - y_pred) * x  # 가중치 업데이트
                    print(f"Updating weights: {self.weights}")

# 예시 데이터
X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])  # AND 문제 입력
y = np.array([0, 0, 0, 1])  # AND 문제 출력 (레이블)

# 퍼셉트론 객체 생성
p = Perceptron(2)

# 모델 학습
p.train(X, y, learning_rate=0.1, epochs=10)

# 학습 후 예측 확인
for x in X:
    y_pred = p(np.array(x))
    print(f"Input: {x}, Predicted: {y_pred}")
