import math
import random
import matplotlib.pyplot as plt

# 参数设置
lambda_val = 5
t = 10
n_trials = 1000

# 生成泊松过程
random.seed(0)
poisson_process = []
for _ in range(n_trials):
    n = 0
    time = 0
    while time < t:
        u = random.uniform(0, 1)
        time -= (1 / lambda_val) * math.log(1 - u)
        if time <= t:
            n += 1
    poisson_process.append(n)

# 计算 N(t) 的分布律
unique = list(set(poisson_process))
unique.sort()
counts = [poisson_process.count(x) for x in unique]
probabilities = [count / n_trials for count in counts]

# 绘制分布律
plt.bar(unique, probabilities)
plt.xlabel('Number of Events')
plt.ylabel('Probability')
plt.title(f'Poisson Process with Lambda={lambda_val}, t={t}')
print(plt.show())