import numpy as np  # 1. numpy 라이브러리 불러오기

def AND(x1, x2):  # 2. AND 함수 정의
    x = np.array([x1, x2, 1])  # 3. 입력 x1, x2와 편향값 1을 배열로 만듦
    w = np.array([0.5, 0.5, -0.8])  # 4. 가중치 배열 정의 (x1의 가중치 0.5, x2의 가중치 0.5, 편향의 가중치 -0.7)
    
    temp = np.dot(x, w.T)  # 5. 입력과 가중치를 곱한 후 더하여 temp에 저장 (내적 연산)
    
    if temp <= 0:  # 6. temp 값이 0 이하이면 출력은 0
        return 0
    elif temp > 0:  # 7. temp 값이 0보다 크면 출력은 1
        return 1
    
def or_gate(x1, x2):
    x = np.array([x1,x2,1])
    w = np.array([0.5,0.5,-0.3])

    wx_sum = np.dot(x, w.T)

    if wx_sum <= 0:
        return 0
    elif wx_sum > 0:
        return 1
    
def nand_gate(x1,x2):
    x = np.array([x1, x2, 1])
    w = np.array([-0.5, -0.5, 0.7])

    wx_sum = np.dot(x, w.T)

    if wx_sum <= 0:
        return 0
    elif wx_sum > 0:
        return 1
    
def xor_gate(x1,x2):
    g1 = nand_gate(x1,x2)
    g2 = or_gate(x1,x2)
    y = AND(g1,g2)
    return y


if __name__ == '__main__':  # 8. main 프로그램 실행 시작
    # AND 연산을 각 입력에 대해 계산하고 출력
    print(f"\n##AND GATE##\n")
    print('(x1=%d) and (x2=%d) = (y=%d)' % (0, 0, AND(0, 0)))  # (0, 0) 입력에 대해 AND 계산
    print('(x1=%d) and (x2=%d) = (y=%d)' % (0, 1, AND(0, 1)))  # (0, 1) 입력에 대해 AND 계산
    print('(x1=%d) and (x2=%d) = (y=%d)' % (1, 0, AND(1, 0)))  # (1, 0) 입력에 대해 AND 계산
    print('(x1=%d) and (x2=%d) = (y=%d)' % (1, 1, AND(1, 1)))  # (1, 1) 입력에 대해 AND 계산

    print(f"\n##OR GATE##\n")
    print(f"(X1=0) and (x2=0) = (y={or_gate(0,0)})")
    print(f"(X1=0) and (x2=1) = (y={or_gate(0,1)})")
    print(f"(X1=1) and (x2=0) = (y={or_gate(1,0)})")
    print(f"(X1=1) and (x2=1) = (y={or_gate(1,1)})")

    print(f"\n##NAND GATE##\n")
    print(f"(X1=0) and (x2=0) = (y={nand_gate(0,0)})")
    print(f"(X1=0) and (x2=1) = (y={nand_gate(0,1)})")
    print(f"(X1=1) and (x2=0) = (y={nand_gate(1,0)})")
    print(f"(X1=1) and (x2=1) = (y={nand_gate(1,1)})")

    
    print(f"\n##XOR GATE##\n")
    print(f"(X1=0) and (x2=0) = (y={xor_gate(0,0)})")
    print(f"(X1=0) and (x2=1) = (y={xor_gate(0,1)})")
    print(f"(X1=1) and (x2=0) = (y={xor_gate(1,0)})")
    print(f"(X1=1) and (x2=1) = (y={xor_gate(1,1)})")