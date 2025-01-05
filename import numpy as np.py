import matplotlib.pyplot as plt
import numpy as np

# 함수 정의 (예: f(x) = x^2)
def f(x):
    return x ** 2

# 사다리꼴 법칙을 통한 수치적분
def trapezoidal_rule(f, a, b, n):
    x = np.linspace(a, b, n+1)  # 구간을 n+1개의 점으로 나누기
    y = f(x)
    area = (b - a) / (2 * n) * (y[0] + 2 * np.sum(y[1:-1]) + y[-1])  # 면적 계산
    return area

# 구간 [0, 1]에서 f(x) = x^2의 적분을 구해보자
a = 0
b = 1
n = 1000  # 구간을 나누는 점의 수
result = trapezoidal_rule(f, a, b, n)

print(f"적분값: {result}")


# 시각화
x_vals = np.linspace(a, b, 1000)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label=r'$f(x) = x^2$')
plt.fill_between(x_vals, y_vals, alpha=0.2, label='적분 면적')
plt.title('사다리꼴 법칙을 이용한 수치적분')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
