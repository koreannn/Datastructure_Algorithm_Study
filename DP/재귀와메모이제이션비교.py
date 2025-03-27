def fibo1(n):
	if n==0 or n==1:
		return n
	return fibo1(n-2) + fibo1(n-1)

def fibo2(n, memo):
	if n==0 or n==1:
		return n
	if n not in memo:  # 특정 값이 테이블에 없다면
		memo[n] = fibo2(n-2, memo) + fibo2(n-1, memo)
	return memo[n]

import time

# 재귀 방식 시간 측정
start_time = time.time()
result1 = fibo1(10)
end_time = time.time()
print(f"재귀 방식 결과: {result1}")
print(f"재귀 방식 실행 시간: {end_time - start_time:.6f}ms")

# 메모이제이션 방식 시간 측정
start_time = time.time()
result2 = fibo2(10, {})
end_time = time.time()
print(f"메모이제이션 방식 결과: {result2}")
print(f"메모이제이션 방식 실행 시간: {end_time - start_time:.6f}ms")