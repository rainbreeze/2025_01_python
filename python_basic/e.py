def and_gate(x1, x2):
    w1, w2, o = 0.5, 0.6, 1
    wx_sum = w1 * x1 + w2 * x2
    if wx_sum <= o:
        return 0
    elif wx_sum > o:
        return 1
    
def nand_gate(x1, x2):
    w1, w2, o = -0.5, -0.6, -1
    wx_sum = w1 * x1 + w2 * x2
    if wx_sum <= o:
        return 0
    if wx_sum > o:
        return 1
    
def or_gate(x1,x2):
    w1, w2, o = 1, 1, 0.9
    wx_sum = w1 * x1 + w2 * x2
    if wx_sum <= o:
        return 0
    if wx_sum > o:
        return 1
    
def not_gate(x1):
    w1, o = -1, -0.5
    wx = w1 * x1
    if wx <= o:
        return 0
    if wx > o:
        return 1


if __name__ == '__main__':

    print(f'--AND GATE--')
    print(f'(x1=0) and (x2=0) = (y={and_gate(0,0)})')
    print(f'(x1=0) and (x2=1) = (y={and_gate(0,1)})')
    print(f'(x1=1) and (x2=0) = (y={and_gate(1,0)})')
    print(f'(x1=1) and (x2=1) = (y={and_gate(1,1)})')

    print(f'\n--NAND GATE--')
    print(f'(x1=0) and (x2=0) = (y={nand_gate(0,0)})')
    print(f'(x1=0) and (x2=1) = (y={nand_gate(0,1)})')
    print(f'(x1=1) and (x2=0) = (y={nand_gate(1,0)})')
    print(f'(x1=1) and (x2=1) = (y={nand_gate(1,1)})')

    print(f'\n--OR GATE--')
    print(f'(x1=0) and (x2=0) = (y={or_gate(0,0)})')
    print(f'(x1=0) and (x2=1) = (y={or_gate(0,1)})')
    print(f'(x1=1) and (x2=0) = (y={or_gate(1,0)})')
    print(f'(x1=1) and (x2=1) = (y={or_gate(1,1)})')

    print(f'\n--NOT GATE--')
    print(f'(x1=0) = (y={not_gate(0)})')
    print(f'(x1=1) = (y={not_gate(1)})')
