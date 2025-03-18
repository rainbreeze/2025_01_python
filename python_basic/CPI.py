import time
import psutil
import cProfile

# 프로그램 성능 측정 함수
def run_program():
    total = 0
    for i in range(10000000):
        total += i
    return total

# 실행 시간과 CPU 사용량 측정
def measure_performance():
    # 프로그램 실행 전 CPU 사용량
    cpu_before = psutil.cpu_percent(interval=1)
    
    # 실행 시작 시간
    start_time = time.time()
    
    # 프로그램 실행
    run_program()  # 여기에 실행할 코드를 넣으면 됩니다
    
    # 실행 종료 시간
    end_time = time.time()

    # 프로그램 실행 후 CPU 사용량
    cpu_after = psutil.cpu_percent(interval=1)

    # 실행 시간 계산
    execution_time = end_time - start_time

    # 결과 출력
    print(f"Execution time: {execution_time:.6f} seconds")
    print(f"CPU Usage Before: {cpu_before}%")
    print(f"CPU Usage After: {cpu_after}%")
    
    return execution_time

# CPI 계산 함수
def calculate_cpi(execution_time, cpu_frequency_ghz, instruction_count):
    # CPU 주파수 (GHz)를 Hz로 변환
    cpu_frequency_hz = cpu_frequency_ghz * 1e9
    
    # 총 클럭 사이클 수 계산 (초 * Hz)
    total_cycles = execution_time * cpu_frequency_hz
    
    # CPI 계산
    cpi = total_cycles / instruction_count
    
    return cpi

# cProfile을 사용한 성능 분석
def profile_program():
    cProfile.run('run_program()')

# 실행
if __name__ == "__main__":
    print("Measuring program performance...\n")
    
    # 성능 측정 (실행 시간, CPU 사용량)
    execution_time = measure_performance()
    
    # 예시: CPU 주파수 2 GHz, 명령어 수 1억 (1e8)
    cpu_frequency = 2.0   # CPU 주파수 (GHz)
    instruction_count = 1e8  # 명령어 수 (예시 값)
    
    # CPI 계산
    cpi = calculate_cpi(execution_time, cpu_frequency, instruction_count)
    print(f"\nCalculated CPI (Cycles Per Instruction): {cpi:.2f}")
    
    # 프로그램 프로파일링
    print("\nProfiling the program...")
    profile_program()
