import numpy as np

class Perceptron:
    def __init__(self, input_length, weights=None):
        # 가중치 초기화, weights가 주어지지 않으면 0.5로 초기화
        if weights is None:
            self.weights = np.ones(input_length) * 0.5
        else:
            self.weights = weights
    
    def unit_step_function(self, x):
        # 단계 함수: x가 0.5보다 크면 1, 아니면 0을 반환
        if x > 0.5:
            return 1
        else:
            return 0

    def __call__(self, in_data):
        # 입력에 대해 가중치와 곱한 후 합산하여 단계 함수로 예측
        weighted_sum = np.dot(self.weights, in_data)
        return self.unit_step_function(weighted_sum)

# Perceptron 객체 생성 (입력 길이 2, 가중치 [0.5, 0.5])
p = Perceptron(2, np.array([0.5, 0.5]))

# 테스트 데이터
test_data = [np.array([0, 0]), np.array([0, 1]), np.array([1, 0]), np.array([1, 1])]

# 각 입력에 대해 예측 수행
for x in test_data:
    y = p(x)
    print(f"Input: {x}, Predicted Output: {y}")
